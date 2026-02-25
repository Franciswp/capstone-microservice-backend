# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for building packages
RUN apt-get update && \
    apt-get install -y build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set an environment variable to ensure Python output is logged in real-time
ENV PYTHONUNBUFFERED=1

# Expose the application's port
EXPOSE 5000

# Command to run the application
CMD ["python", "app/app.py"]