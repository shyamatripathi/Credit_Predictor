# 💳 Credit Score Predictor with PDF Report Generator

A Django-based web application that predicts a user's **credit score** based on financial inputs and generates a downloadable **PDF report** of the prediction.

---

## ✨ Features

- 🔍 Predict credit scores using a trained ML model
- 📋 Input financial details through a user-friendly web form
- 💾 Uses `joblib` to load the serialized model and scaler
- 🧾 Generate downloadable PDF reports with input summary and prediction
- 🖥️ Simple and clean interface for easy interaction

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS (basic styling)
- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, NumPy, joblib
- **PDF Generation**: FPDF
- **API Support**: JSON-based POST API for predictions
- **Deployment**: Local setup-ready

---

## 🚀 How to Deploy Locally

# 1. Clone or Download the Repository
--git clone https://github.com/your-username/credit-score-predictor.git
--cd credit-score-predictor
--python -m venv venv
--source venv/bin/activate     # Linux/macOS
--venv\Scripts\activate        # Windows
--pip install django scikit-learn numpy joblib fpdf
--Add the ML Model
--Visit my Kaggle profile: Shyama Tripathi's Kaggle(https://www.kaggle.com/shyamatripathi)
--Download the pinned credit_score_model.pkl file
--Place the file inside the predictor/ directory
--Run the Server:
--python manage.py runserver
--API Usage (Optional)
--You can also make predictions using the API.
--URL:-http://127.0.0.1:8000/api/predict/
--Method:POST
--Content-Type--application/json
Sample Request Body
{
  "Annual_Income": 500000,
  "Monthly_Inhand_Salary": 40000,
  "Num_Bank_Accounts": 4,
  "Outstanding_Debt": 15000,
  "Credit_Utilization_Ratio": 35
}
--Using Postman-->
--Open Postman
--Select POST method
--URL: http://127.0.0.1:8000/api/predict/
--Go to Body → Select raw → Choose JSON
--Paste the JSON body shown above
--Click Send
--You’ll get a JSON response like:
{
  "predicted_credit_score": "Good"
}
###Project Structure
credit-score-predictor/
├── credit_predictor/
├── predicto/
│   └── credit_score_model.pkl   ← trained ML model
├── db.sqlite3
├── manage.py
└── README.md
###Future Improvements
  --UI styling with Bootstrap or Tailwind CSS
  --Add user authentication
  --Deploy on platforms like Render, Heroku, or AWS
  --Containerize using Docker
###Author
--Shyama Tripathi
--🔗 Visit My Kaggle Profile: https://www.kaggle.com/shyamatripathi
