import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle

def load_data():
    df = pd.read_csv('/opt/airflow/working_data/data.csv')
    return df

def data_preprocessing(df):
    df = df.dropna()
    return df

def build_save_model(df, filename):
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df)
        sse.append(kmeans.inertia_)
    with open(f'/opt/airflow/working_data/{filename}', 'wb') as f:
        pickle.dump(sse, f)
    return sse

def load_model_elbow(filename, sse):
    with open(f'/opt/airflow/working_data/{filename}', 'rb') as f:
        sse = pickle.load(f)
    kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")
    return kl.elbow
