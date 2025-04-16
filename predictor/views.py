import os
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Features used in training
FEATURES_USED = [
    'Annual_Income',
    'Monthly_Inhand_Salary',
    'Num_Bank_Accounts',
    'Outstanding_Debt',
    'Credit_Utilization_Ratio'
]

# Lazy-load model and scaler
_model = None
_scaler = None

def get_model():
    global _model
    if _model is None:
        model_path = os.path.join(settings.BASE_DIR, 'predictor', 'credit_score_model.pkl')
        _model = joblib.load(model_path)
    return _model

def get_scaler():
    global _scaler
    if _scaler is None:
        scaler_path = os.path.join(settings.BASE_DIR, 'predictor', 'scaler.pkl')
        _scaler = joblib.load(scaler_path)
    return _scaler

def home(request):
    return render(request, 'home.html', {'fields': FEATURES_USED, 'values': {}})

def predict_credit_score(request):
    if request.method == "POST":
        try:
            model = get_model()
            scaler = get_scaler()
            
            input_data = []
            for field in FEATURES_USED:
                raw_val = request.POST.get(field)
                if raw_val is None:
                    raise ValueError(f"Missing input for {field}")
                
                clean_val = ''.join(c for c in raw_val if c.isdigit() or c in '.-')
                input_data.append(float(clean_val))

            scaled_input = scaler.transform(np.array([input_data]))
            prediction = model.predict(scaled_input)[0]

            return render(request, 'home.html', {
                'prediction': prediction,
                'fields': FEATURES_USED,
                'values': dict(zip(FEATURES_USED, input_data))
            })

        except Exception as e:
            return render(request, 'home.html', {
                'error': str(e),
                'fields': FEATURES_USED
            })
    return home(request)

@api_view(['POST'])
def predict_credit_score_api(request):
    try:
        model = get_model()
        scaler = get_scaler()
        
        input_data = []
        for field in FEATURES_USED:
            raw_val = request.data.get(field)
            if raw_val is None:
                return Response({'error': f"Missing input for {field}"}, status=status.HTTP_400_BAD_REQUEST)
            
            clean_val = ''.join(c for c in str(raw_val) if c.isdigit() or c in '.-')
            try:
                input_data.append(float(clean_val))
            except ValueError:
                return Response({'error': f"Invalid value for {field}"}, status=status.HTTP_400_BAD_REQUEST)

        scaled_input = scaler.transform(np.array([input_data]))
        prediction = model.predict(scaled_input)[0]

        return Response({'predicted_score': float(prediction)}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
