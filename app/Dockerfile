# Use a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Create the log directory
RUN mkdir -p /app/log

# Copy requirements file and source code to the container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose port 5000 (if you're using Flask or a web server)
EXPOSE 5000

# Define the default command
CMD ["python", "main.py"]
