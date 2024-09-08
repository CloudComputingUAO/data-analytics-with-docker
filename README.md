# Data Analytics with Docker

This project demonstrates how to perform data analytics with Docker using Python, PostgreSQL, Redis, Celery, and PySpark. The project processes CSV files, loads data into a PostgreSQL database, performs data analysis with PySpark, and generates periodic reports.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd your_project
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
