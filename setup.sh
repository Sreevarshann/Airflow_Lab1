#!/bin/bash

echo "🚀 Setting up Airflow Lab Environment..."

# Step 1: Create required folders
mkdir -p dags logs plugins src working_data

# Step 2: Create .env file
echo "AIRFLOW_UID=$(id -u)" > .env

# Step 3: Install dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# Step 4: Initialize Airflow
echo "🔧 Initializing Airflow..."
docker compose down --volumes --remove-orphans
docker compose up airflow-init

# Step 5: Start Airflow
echo "▶️ Starting Airflow..."
docker compose up
