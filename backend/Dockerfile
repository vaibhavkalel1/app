# Use Python 3.9 base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies (add any other dependencies your app may require)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean

# Copy the requirements file first for better caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask server
CMD ["python", "blockchain.py"]
