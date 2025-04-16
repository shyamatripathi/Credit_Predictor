#!/bin/bash

set -e  # Exit immediately if any command fails

echo "Installing gdown..."
pip install --no-cache-dir gdown

echo "Downloading model file from Google Drive..."
gdown https://drive.google.com/uc?id=1SGgdsz_eDKrdD4qw5YlQXQigwrS6frim -O predictor/credit_score_model.pkl

echo "Running Django migrations..."
python manage.py migrate --no-input

echo "Starting Django app with Gunicorn..."
exec gunicorn credit_predictor.wsgi:application --bind 0.0.0.0:8000 --workers 2
