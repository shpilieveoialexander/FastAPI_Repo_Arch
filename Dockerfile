# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install any necessary dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .
ENV PYTHONPATH=/app

# Make sure the start.sh script is executable
RUN chmod +x ./app/bash_scripts/start.sh

# Expose port 8000 to access the FastAPI app
EXPOSE 8000

# Run the app via the start.sh script
CMD ["/app/bash_scripts/start.sh"]
