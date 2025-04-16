FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install pip install -r requirements.txt

# Copy all files
COPY . .

# Make sure start.sh is executable
RUN chmod +x start.sh

# Expose the app port
EXPOSE 8000

# Run the app
CMD ["./start.sh"]
