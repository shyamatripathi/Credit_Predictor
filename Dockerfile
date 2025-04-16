FROM python:3.9-slim

# Create non-root user
RUN useradd -m appuser && mkdir /app && chown appuser:appuser /app
WORKDIR /app
USER appuser

# Install minimal system dependencies
RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends git && \
    sudo rm -rf /var/lib/apt/lists/*

# Install Python dependencies with caching optimization
COPY --chown=appuser requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=appuser . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MODEL_PATH=/app/predictor/credit_score_model.pkl

CMD ["./start.sh"]
