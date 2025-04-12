# 💳 Credit Score Predictor with PDF Report Generator

A Django-based web app that predicts a user's **credit score** based on financial inputs and generates a **PDF report**.

---

## ✨ Features

- Predicts credit score using a trained ML model
- User-friendly form to input financial details
- Generates downloadable PDF report with prediction summary
- JSON-based API support for integration
- Clean and simple UI

---

## 🧰 Tech Stack

- **Backend**: Django, Python
- **ML**: Scikit-learn, NumPy, joblib
- **PDF Generation**: FPDF
- **Frontend**: HTML, CSS
- **API Testing**: Postman 

---

## 🚀 Quick Start (Local Setup)

```bash
# Clone repo and set up environment
git clone https://github.com/your-username/credit-score-predictor.git
cd credit-score-predictor
python -m venv venv
# Activate venv: use one of the following
source venv/bin/activate       # for Linux/macOS
venv\Scripts\activate          # for Windows
pip install django scikit-learn numpy joblib fpdf

# Download model
# Visit: https://www.kaggle.com/shyamatripathi
# Download: credit_score_model.pkl
# Place it inside: predictor/

# Run the server
python manage.py runserver
credit-score-predictor/
├── credit_predictor/
├── predicto/
│   └── credit_score_model.pkl   ← Trained ML model
├── db.sqlite3
├── manage.py
└── README.md
