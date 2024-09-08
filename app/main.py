from tasks import load_csv_from_queue, analyze_data_task
from celery import Celery
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Celery
app = Celery("tasks", broker="redis://redis:6379/0")


def main():
    try:
        logger.info("Starting the data processing pipeline...")
        # Load CSV files from the queue
        load_csv_from_queue.apply_async()
        # Analyze data and generate reports
        analyze_data_task.apply_async()
        logger.info("Data processing and analysis tasks have been scheduled.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
