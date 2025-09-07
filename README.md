# Airflow Weather Demo (Kisumu)

This project demonstrates how to use **Apache Airflow** to orchestrate a simple data pipeline that fetches weather data for **Kisumu, Kenya**, converts it into a CSV file, and optionally uploads it to **Amazon S3** for storage.

## 📋 Project Contents
- **DAG file** (`weather_dag.py`)
- **Step-by-step setup guide**
- **Airflow UI access instructions**

---

##  Prerequisites

Before starting, ensure you have:
- An **AWS account**
- Basic knowledge of **EC2**
- An **SSH key pair** for connecting to your instance

---

##  Launch EC2 Instance

1. Navigate to **AWS Management Console → EC2 → Launch Instance**
2. Configure your instance:
   - **AMI**: Ubuntu 22.04 LTS
   - **Instance type**: t2.medium (recommended for Airflow standalone)
   - **Storage**: At least 20 GB
   - **Security group**:
     - Allow **SSH (22)** from your IP
     - Allow **Custom TCP (8080)** from your IP (for Airflow UI)
3. Launch the instance and note your **Public DNS**

---

## 🐍 Set Up Python Environment

SSH into your instance:
```bash
ssh -i <your-key>.pem ubuntu@<your-ec2-public-dns>
```

Install dependencies:
```bash
sudo apt update -y
sudo apt install -y python3-venv unzip curl
```

Create and activate virtual environment:
```bash
python3 -m venv airflow_venv
source airflow_venv/bin/activate
```

Install requirements (has all the dependencies):
```bash
pip install -r requirements.txt
```

---

## 📦 Install Airflow and Providers

Install required packages:
```bash
pip install apache-airflow==2.9.3 \
            apache-airflow-providers-http \
            apache-airflow-providers-amazon \
            pandas
```

---

##  Initialize Airflow

Start Airflow standalone (sets up development environment):
```bash
airflow standalone
```

**Default credentials** (printed in logs):
- **Username**: `airflow`
- **Password**: `airflow`

Airflow webserver runs on port 8080.

---

## 📝 Add the DAG

Navigate to Airflow DAGs folder:
```bash
cd ~/airflow/dags
```

Create `weather_dag.py` and add the DAG code from this repository.

Restart Airflow:
```bash
pkill -f "airflow webserver"
airflow standalone
```

---

## 🌦️ DAG Workflow

The pipeline consists of three tasks:

1. **API Health Check** - Verify weather API accessibility
2. **Fetch Weather Data** - Retrieve current weather for Kisumu
3. **Convert to CSV** - Transform JSON to timestamped CSV file

**Example output**: `current_weather_data_kisumu_20250907231130.csv`

**Optional**: Upload CSV to Amazon S3 (if configured)

---

##  S3 Upload 

To enable S3 upload functionality:

Install AWS CLI v2:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Configure AWS credentials:
```bash
aws configure
```

Update DAG to include S3 upload task:
```bash
aws s3 cp <csv_file>.csv s3://your-bucket-name/
```

---

##  Access Airflow UI

1. Open your browser
2. Navigate to: `http://<your-ec2-public-dns>:8080`
3. Login with:
   - **Username**: `airflow`
   - **Password**: `airflow`

---

## 💡 Demo Access

Since keeping EC2 instances running incurs costs, the UI may not always be online.

**For a live demo**:
- Open an issue in this repository
- I will spin up the instance and share Public DNS + login details

---

##  Repository Structure

```
airflow-weather-demo/
├── weather_dag.py    # The Airflow DAG
└── README.md         # This setup guide
```

---

##  Clean Up

To avoid AWS charges:

1. **Stop or terminate** your EC2 instance in AWS Console
2. **Delete unused S3 buckets** (if created)
3. **Release Elastic IPs** (if allocated)

> **Note**: Terminating the instance releases the public IP address.

---

##  Summary

-  EC2 instance runs Airflow standalone
-  Weather data fetched via HTTP API for Kisumu
-  Data transformed to CSV format
-  Optional S3 upload capability
-  Airflow UI accessible on port 8080
-  Live demo available on request

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve this demo!