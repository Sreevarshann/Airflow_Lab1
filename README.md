# 🌍 MLOps Airflow Lab – Global Earthquake–Tsunami Risk Assessment 🌊

> **Automated Machine Learning Pipeline using Apache Airflow**  
> A complete MLOps workflow for **Earthquake–Tsunami Risk Clustering** and **Elbow Method Evaluation** using Airflow DAG orchestration inside Docker.

---

<p align="center">
  <img src="https://img.shields.io/badge/Airflow-2.5.1-017CEE?logo=apacheairflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?logo=python" />
  <img src="https://img.shields.io/badge/ML-ScikitLearn%20%7C%20KMeans-blue" />
  <img src="https://img.shields.io/badge/Automation-Docker%20%7C%20Airflow-green" />
</p>

---

## 🎯 **Objective**

To design a **modular, automated data pipeline** that processes the real-world  
**[Global Earthquake–Tsunami Risk Assessment Dataset](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset?resource=download)**,  
performs **clustering analysis using K-Means**, and determines the **optimal cluster count via the Elbow Method** — all orchestrated by **Apache Airflow**.

---

## ⚙️ **Pipeline Overview**

The DAG, named **`global_earthquake_tsunami_risk_assessment`**, automates a 4-stage ML workflow:

| 🧩 **Task ID** | 🔍 **Description** | 📦 **Output / Artifact** |
|----------------|-------------------|---------------------------|
| `load_earthquake_tsunami_data` | Loads raw seismic and tsunami risk data (`data.csv`) into Airflow | Pandas DataFrame |
| `preprocess_risk_features` | Cleans, normalizes, and prepares data for clustering | Preprocessed DataFrame |
| `build_kmeans_risk_clusters` | Applies **K-Means Clustering** across multiple `k` values and stores the **SSE scores** | `sse.pkl` |
| `evaluate_optimal_cluster_elbow` | Uses the **Elbow Method** to find the best number of clusters | Visual plot (`elbow_plot.png`) & optimal K printed in logs |

Each task runs as an independent **PythonOperator** in Airflow for modularity and scalability.

---

## 🧠 **ML Model Used – K-Means Clustering**

- **Algorithm:** K-Means (Unsupervised Learning)  
- **Metric:** Sum of Squared Errors (SSE)  
- **Purpose:** Identify natural global risk zones based on seismic intensity, depth, and tsunami frequency.  
- **Evaluation:** Elbow Method — where the rate of SSE decline slows significantly, indicating the optimal number of clusters `k`.

---

## 🏗️ **System Architecture**

```text
┌────────────────────────────────────────┐
│           Apache Airflow (Docker)      │
│────────────────────────────────────────│
│ DAG: global_earthquake_tsunami_risk_assessment │
│ ├── load_earthquake_tsunami_data()     │
│ ├── preprocess_risk_features()         │
│ ├── build_kmeans_risk_clusters()       │
│ └── evaluate_optimal_cluster_elbow()   │
└────────────────────────────────────────┘
````

**Data Flow:**
`data.csv → preprocess → cluster → sse.pkl → elbow_plot.png`

---

## 🧰 **Tech Stack**

| Category             | Tools / Libraries           |
| -------------------- | --------------------------- |
| **Orchestration**    | Apache Airflow (Dockerized) |
| **Programming**      | Python 3.9+                 |
| **Data Processing**  | Pandas, NumPy               |
| **Modeling**         | scikit-learn (KMeans)       |
| **Visualization**    | Matplotlib                  |
| **Persistence**      | Pickle (`sse.pkl`)          |
| **Containerization** | Docker Compose              |

---

## ⚙️ **Setup Instructions**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sreevarshann/Airflow_Lab1.git
cd Airflow_Lab1
```

### 2️⃣ Run the Setup Script

```bash
./setup.sh
```

This script will:

* Create all necessary folders (`dags`, `logs`, `src`, `working_data`)
* Install Python dependencies from `requirements.txt`
* Initialize and start Airflow via Docker Compose

---

## 🌐 **Access the Airflow UI**

Once containers are running, visit:
👉 [http://localhost:8080](http://localhost:8080)

**Default Login:**

```bash
Username: airflow
Password: airflow
```

---

## ▶️ **Trigger the DAG**

1. Go to **DAGs → global_earthquake_tsunami_risk_assessment**
2. Turn the DAG **ON**
3. Click **Trigger DAG**
4. Monitor execution in **Graph View**

When all tasks turn 🟢 green, your pipeline completed successfully ✅.

---

## 📊 **Output & Results**

| Output File      | Location        | Description                     |
| ---------------- | --------------- | ------------------------------- |
| `data.csv`       | `working_data/` | Original dataset                |
| `sse.pkl`        | `working_data/` | Stored SSE values for K=1 to 10 |
| `elbow_plot.png` | `working_data/` | Elbow curve showing optimal K   |

**Example Elbow Curve Visualization:**

<p align="center">
  <img src="https://raw.githubusercontent.com/Sreevarshann/Airflow_Lab1/refs/heads/main/working_data/elbow_plot.png" width="700" alt="Elbow Method Plot">
  <br>
  <em>Figure: Elbow Curve showing optimal cluster count (K ≈ 4–5)</em>
</p>

Optimal **K ≈ 4–5**, indicating distinct global seismic–tsunami risk zones 🌏.

---

## 📦 **Repository Structure**

```
Airflow_Lab1/
├── dags/
│   └── airflow.py
├── src/
│   └── lab.py
├── working_data/
│   ├── data.csv
│   ├── sse.pkl
│   └── elbow_plot.png
├── docker-compose.yaml
├── requirements.txt
├── setup.sh
└── .env
```

---

## 📸 **Screenshots**

### ✅ DAG Overview

![Airflow DAG Success](https://raw.githubusercontent.com/Sreevarshann/Airflow_Lab1/refs/heads/main/Result/DAG-Successful.png)

---

## 🧩 **Key Learnings**

* Built an end-to-end **automated ML pipeline** with Airflow DAGs
* Implemented **K-Means clustering** for geospatial risk segmentation
* Applied the **Elbow Method** for unsupervised evaluation
* Designed a **Dockerized orchestration workflow** for reproducibility
* Gained hands-on experience in **MLOps automation and pipeline modularity**

---

## 🧱 **References**

* [Apache Airflow Documentation](https://airflow.apache.org/docs/)
* [Scikit-Learn KMeans API](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
* [Global Earthquake & Tsunami Risk Dataset (Kaggle)](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset?resource=download)

---

## 🙌 **Author**

**Sreevarshan Sathiyamurthy**
🎓 *MS in Data Analytics Engineering, Northeastern University (Boston)*
🔗 [LinkedIn](https://www.linkedin.com/in/sreevarshansathiyamurthy/) • [GitHub](https://github.com/Sreevarshann)

---
