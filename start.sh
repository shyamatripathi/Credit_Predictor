#!/bin/bash

echo "Installing gdown..."
pip install gdown

echo "Downloading model file from Google Drive..."
gdown https://drive.google.com/uc?id=1SGgdsz_eDKrdD4qw5YlQXQigwrS6frim

echo "Moving model to predictor folder..."
mv credit_score_model.pkl predictor/

echo "Running Django migrations..."
python manage.py migrate

echo "Starting Django app with Gunicorn..."
gunicorn credit_predictor.wsgi:application --bind 0.0.0.0:$PORT
