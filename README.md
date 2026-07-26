# 🚀 Spark Data Engineering Pipeline

A production-style end-to-end data engineering pipeline built using **PySpark**, **AWS S3**, and **PostgreSQL**. The pipeline extracts raw JSON data from Amazon S3, validates and transforms it using PySpark, writes the processed data in Parquet format, and loads the final dataset into PostgreSQL.

---

## 📌 Features

- Extract JSON data from AWS S3
- Schema validation
- Data quality validation
- Data cleaning
- Data transformation with PySpark
- Store processed data as Parquet
- Load transformed data into PostgreSQL
- Logging
- Unit testing with Pytest
- GitHub Actions CI

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Processing | Apache Spark (PySpark) |
| Storage | AWS S3 |
| Database | PostgreSQL |
| Testing | Pytest |
| Version Control | Git & GitHub |
| CI/CD | GitHub Actions |

---

## 📂 Project Structure

```text
spark-data-engineering-pipeline/
│
├── configs/
├── data/
├── drivers/
├── logs/
├── notebooks/
├── sql/
├── src/
│   ├── extract/
│   ├── validation/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── terraform/
├── tests/
├── .github/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Workflow

```
AWS S3 (Raw JSON)
        │
        ▼
Schema Validation
        │
        ▼
Data Quality Checks
        │
        ▼
Data Cleaning
        │
        ▼
Data Transformation
        │
        ▼
Write Parquet to S3
        │
        ▼
Load into PostgreSQL
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Giri-25/spark-data-engineering-pipeline.git

cd spark-data-engineering-pipeline
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file.

```text
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
S3_BUCKET=

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

---

## ▶️ Run the Pipeline

```bash
python main.py
```

---

## 🧪 Run Unit Tests

```bash
pytest
```

---

## 📊 Project Highlights

- Built an end-to-end ETL pipeline using PySpark.
- Implemented schema validation and data quality checks.
- Processed data stored in efficient Parquet format.
- Loaded transformed data into PostgreSQL.
- Integrated GitHub Actions for continuous integration.
- Followed modular project architecture and logging best practices.

---

## 🚀 Future Improvements

- Docker support
- Apache Airflow orchestration
- Terraform infrastructure deployment
- AWS Glue integration
- Great Expectations for data validation
- Monitoring with Prometheus and Grafana

---

## 👩‍💻 Author

**Girija Ganesh Raskar**

GitHub: https://github.com/Giri-25

---

## ⭐ If you found this project useful, consider giving it a star!