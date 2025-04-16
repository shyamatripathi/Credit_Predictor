FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies (git is needed if you install packages from git)
RUN apt-get update && apt-get install -y --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first (for better caching)
COPY requirements.txt .

# Install Python dependencies (without root user warnings)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Expose the app port
EXPOSE 8000

# Run the app
CMD ["./start.sh"]
