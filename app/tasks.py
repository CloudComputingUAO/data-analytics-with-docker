import os
import pandas as pd
import psycopg2
from celery import Celery
from celery_config import app
from datetime import datetime
import shutil
import logging

# Logger configuration
LOG_DIR = "/app/log"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "process.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()

# Database configuration
from config import DB_CONFIG
from queries import INSERT_SALES_QUERY

# Directories
PENDING_DIR = "pending"
PROCESSED_DIR = "processed"
REPORTS_DIR = "reports"


@app.task
def load_csv_from_queue():
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    files = [f for f in os.listdir(PENDING_DIR) if f.endswith(".csv")]

    for file in files:
        file_path = os.path.join(PENDING_DIR, file)

        try:
            load_csv_task.apply_async(args=[file_path])
            shutil.move(file_path, os.path.join(PROCESSED_DIR, file))
            logger.info(f"File {file} processed and moved to {PROCESSED_DIR}")
        except Exception as e:
            logger.error(f"Failed to process file {file}. Error: {e}")

    return "CSV files loaded from queue and moved to processed."


@app.task
def load_csv_task(csv_file):
    try:
        df = pd.read_csv(csv_file)
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for index, row in df.iterrows():
            cursor.execute(
                INSERT_SALES_QUERY, (row["product"], row["amount"], row["date"])
            )

        conn.commit()
        cursor.close()
        conn.close()

        logger.info(f"Data from {csv_file} loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load data from {csv_file}. Error: {e}")


@app.task
def analyze_data_task():
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

    try:
        jdbc_url = f"jdbc:postgresql://{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
        properties = {"user": DB_CONFIG["user"], "password": DB_CONFIG["password"]}

        df_spark = spark.read.jdbc(url=jdbc_url, table="sales", properties=properties)
        df_spark.createOrReplaceTempView("sales")
        result = spark.sql(
            "SELECT product, SUM(amount) as total_amount FROM sales GROUP BY product"
        )
        pandas_df = result.toPandas()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"data_analysis_report_{timestamp}.csv"

        if not os.path.exists(REPORTS_DIR):
            os.makedirs(REPORTS_DIR)

        report_filepath = os.path.join(REPORTS_DIR, report_filename)
        pandas_df.to_csv(report_filepath, index=False)

        logger.info(f"Data analysis completed and report saved to {report_filepath}.")
    except Exception as e:
        logger.error(f"Failed to analyze data. Error: {e}")
    finally:
        spark.stop()
