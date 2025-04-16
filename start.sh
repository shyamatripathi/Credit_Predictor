#!/bin/bash
set -e

echo "Downloading model file..."
gdown https://drive.google.com/uc?id=1SGgdsz_eDKrdD4qw5YlQXQigwrS6frim -O predictor/credit_score_model.pkl

echo "Running migrations..."
python manage.py migrate --no-input

echo "Starting Gunicorn with 1 worker (memory-safe config)..."
exec gunicorn credit_predictor.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --threads 2 \
    --timeout 120 \
    --preload  # Loads app before forking workers
