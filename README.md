# Data Analytics with Docker

This repository provides a comprehensive example of a data analytics pipeline using Docker. It demonstrates how to integrate various technologies including Python, PostgreSQL, Redis, Celery, and PySpark to build a robust data processing and analysis workflow. The project includes functionalities for:

- **CSV File Processing**: Load and process CSV files into a PostgreSQL database.
- **Data Analysis**: Perform data analysis using PySpark and generate periodic reports.
- **Task Scheduling**: Utilize Celery for periodic and asynchronous task execution.
- **Testing**: Includes unit tests with `pytest` to ensure code reliability.

## Project Structure

Here is a brief description of the files and directories in this repository:

- **`app/`**: Contains the core application code.

  - **`__init__.py`**: Initializes the `app` package and optionally defines the package version or imports key functions.
  - **`main.py`**: The main entry point of the application that starts the data processing pipeline.
  - **`tasks.py`**: Contains Celery tasks for loading CSV files and analyzing data.
  - **`config.py`**: Configuration settings for database connections and other parameters.
  - **`queries.py`**: SQL queries used in the project.
  - **`Dockerfile`**: Defines how to build the Docker image for the application.
  - **`requirements.txt`**: Lists Python dependencies required for the application.

- **`docker-compose.yml`**: Docker Compose configuration file that defines the services (e.g., Redis, PostgreSQL, Celery, and test container) required for the application.

- **`.env.example`**: Example environment variable file. Copy this to `.env` and configure your own environment variables.

- **`.gitignore`**: Specifies files and directories to be ignored by Git.

- **`README.md`**: Provides an overview of the project, setup instructions, and usage information.

- **`test/`**: Contains unit tests for the project.
  - **`test_tasks.py`**: Unit tests for the functions defined in `tasks.py`.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd data-analytics-with-docker
   ```

2. **Create a `.env` File:**

   Copy the `.env.example` to `.env` and update the variables with your configuration.

   ```bash
   cp .env.example .env
   ```

3. **Build and Start the Containers:**

   Build and start the Docker containers using Docker Compose.

   ```bash
   docker-compose build
   docker-compose up
   ```

## Running Tests

1. **Run Unit Tests:**

   Execute the unit tests to ensure the code is working as expected.

   ```bash
   docker-compose run --rm test
   ```

2. **Check Test Results:**

   The results of the tests, including the percentage of passing tests, will be shown in the output of the command.

## Validating the Setup

1. **Check Running Containers:**

   Ensure that all the containers are running.

   ```bash
   docker-compose ps
   ```

2. **Verify Logs:**

   Check the logs of the `app` container to ensure there are no errors.

   ```bash
   docker-compose logs app
   ```

3. **Test CSV File Processing:**

   - Place a CSV file into the `pending` directory.
   - The `app` container should process the file, and you should see log entries indicating successful processing.

4. **Verify Reports:**

   - After processing CSV files, check the `reports` directory for generated analysis reports.

5. **Database Verification:**

   - Access the PostgreSQL container and verify the data in the `sales` table.

   ```bash
   docker-compose exec postgres psql -U your_username -d sales_db
   ```

## Stopping the Containers

To stop and remove the containers, run:

```bash
docker-compose down
```
