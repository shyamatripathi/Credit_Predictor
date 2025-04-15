from django.shortcuts import render
import joblib
import numpy as np

# Load model and scaler
model_path = os.path.join(settings.BASE_DIR, 'predictor', 'credit_score_model.pkl')
model = joblib.load(model_path)

#model = joblib.load('C:/Users/shyam/OneDrive/Desktop/dsProject1/credit_predictor/predictor/credit_score_model.pkl')
scaler = joblib.load('C:/Users/shyam/OneDrive/Desktop/dsProject1/credit_predictor/predictor/scaler.pkl')

# Only include features used in training
FEATURES_USED = [
    'Annual_Income',
    'Monthly_Inhand_Salary',
    'Num_Bank_Accounts',
    'Outstanding_Debt',
    'Credit_Utilization_Ratio'
]


def home(request):
    values = {}  # Ensure values is always a dictionary
    return render(request, 'home.html', {'fields': FEATURES_USED, 'values': values})

import os
import joblib
import urllib.request
import tempfile

def download_model_from_google_drive():
    # File ID extracted from your Google Drive link
    file_id = "1SGgdsz_eDKrdD4qw5YlQXQigwrS6frim"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    # Download to a temporary file
    with urllib.request.urlopen(download_url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response.read())
            return tmp_file.name

# Download and load the model
model_path = download_model_from_google_drive()
model = joblib.load(model_path)

def predict_credit_score(request):
    if request.method == "POST":
        try:
            input_data = []
            for field in FEATURES_USED:
                raw_val = request.POST.get(field)
                if raw_val is None:
                    raise ValueError(f"Missing input for {field}")

                # Remove non-numeric characters if accidentally entered
                clean_val = ''.join(c for c in raw_val if c.isdigit() or c == '.' or c == '-')

                try:
                    val = float(clean_val)
                    input_data.append(val)
                except ValueError:
                    raise ValueError(f"Invalid numeric value for {field}: '{raw_val}'")

            # Reshape and scale
            input_array = np.array([input_data])
            scaled_input = scaler.transform(input_array)

            # Predict
            prediction = model.predict(scaled_input)

            return render(request, 'home.html', {
                'prediction': prediction[0],
                'fields': FEATURES_USED,
                'values': dict(zip(FEATURES_USED, input_data)),  # To repopulate the form
                'annual_income': input_data[0],
                'monthly_salary': input_data[1],
                'num_accounts': input_data[2],
                'debt': input_data[3],
                'ratio': input_data[4],
            })

        except Exception as e:
            return render(request, 'home.html', {
                'error': str(e),
                'fields': FEATURES_USED
            })

    return render(request, 'home.html', {'fields': FEATURES_USED})

from django.http import HttpResponse
from .utils.pdf_generator import generate_credit_score_pdf


def download_pdf(request):
    if request.method == 'POST':
        # Extract data from the POST request
        annual_income = request.POST.get('AnnualIncome')
        monthly_salary = request.POST.get('MonthlyInhandSalary')
        num_accounts = request.POST.get('NumBankAccounts')
        debt = request.POST.get('OutstandingDebt')
        ratio = request.POST.get('CreditUtilizationRatio')
        predicted_score = request.POST.get('predicted_score')

        # Organize the data into a dictionary
        user_inputs = {
            "Annual Income": annual_income,
            "Monthly Inhand Salary": monthly_salary,
            "Num Bank Accounts": num_accounts,
            "Outstanding Debt": debt,
            "Credit Utilization Ratio": ratio,
        }

        # Generate the PDF content
        pdf_content = generate_credit_score_pdf(user_inputs, predicted_score)

        # Create an HTTP response with the PDF content
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="credit_score_report.pdf"'
        return response
    else:
        # Handle cases where the request method is not POST
        return HttpResponse("Invalid request method.", status=405)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def predict_credit_score_api(request):
    try:
        input_data = []
        for field in FEATURES_USED:
            raw_val = request.data.get(field)
            if raw_val is None:
                return Response({'error': f"Missing input for {field}"}, status=status.HTTP_400_BAD_REQUEST)

            clean_val = ''.join(c for c in str(raw_val) if c.isdigit() or c == '.' or c == '-')
            try:
                val = float(clean_val)
                input_data.append(val)
            except ValueError:
                return Response({'error': f"Invalid numeric value for {field}: '{raw_val}'"}, status=status.HTTP_400_BAD_REQUEST)

        input_array = np.array([input_data])
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)

        return Response({'predicted_score': prediction[0]}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
