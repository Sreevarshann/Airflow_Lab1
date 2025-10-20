from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import configuration as conf
import sys
import os

# ✅ Ensure src folder is discoverable
SRC_PATH = os.path.join(os.path.dirname(__file__), "../src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

from lab import load_data, data_preprocessing, build_save_model, load_model_elbow

# Enable XCom pickling for passing objects between tasks
conf.set('core', 'enable_xcom_pickling', 'True')

default_args = {
    'owner': 'sreevarshan',
    'start_date': datetime(2025, 10, 20),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

# 🌍 DAG Definition: Global Earthquake–Tsunami Risk Assessment
with DAG(
    dag_id='global_earthquake_tsunami_risk_assessment',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Automated ML pipeline for Global Earthquake–Tsunami Risk Assessment dataset '
                'including data preprocessing, K-Means clustering, and elbow method evaluation.'
) as dag:

    # Task 1: Load the earthquake-tsunami dataset
    task_load_data = PythonOperator(
        task_id='load_earthquake_tsunami_data',
        python_callable=load_data
    )

    # Task 2: Clean and preprocess risk features
    task_preprocess_data = PythonOperator(
        task_id='preprocess_risk_features',
        python_callable=data_preprocessing,
        op_args=[task_load_data.output]
    )

    # Task 3: Build clustering model and save SSE values
    task_build_model = PythonOperator(
        task_id='build_kmeans_risk_clusters',
        python_callable=build_save_model,
        op_args=[task_preprocess_data.output, 'sse.pkl']
    )

    # Task 4: Determine optimal cluster count using elbow method
    task_evaluate_elbow = PythonOperator(
        task_id='evaluate_optimal_cluster_elbow',
        python_callable=load_model_elbow,
        op_args=['sse.pkl', task_build_model.output]
    )

    # Define task dependency flow
    task_load_data >> task_preprocess_data >> task_build_model >> task_evaluate_elbow
