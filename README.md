# 💳 Credit Score Predictor with PDF Report Generator

A Django-based web app that predicts a user's **credit score** based on financial inputs and generates a **PDF report** of the results.

---

## ✨ Features

- 🔍 Predicts credit score using a trained ML model (Scikit-learn)
- 🧾 Generates downloadable PDF report with user inputs and predictions
- 📋 Validates financial data input before processing
- 📡 Offers an optional JSON-based API endpoint for programmatic access
- 📊 Visualizes inputs with interactive charts using Chart.js
- 🖥️ Clean, responsive, and single-page web UI

---

## 🧰 Tech Stack

- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, NumPy, Joblib
- **PDF Generation**: FPDF
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **API Testing**: Postman

---

## 🚀 Quick Start (Local Setup)

```bash
# 1. Clone this repo
git clone https://github.com/shyamatripathi/Credit_Predictor.git
cd Credit_Predictor

# 2. Create and activate virtual environment
python -m venv venv
# For Windows
venv\Scripts\activate
# For Linux/macOS
source venv/bin/activate

# 3. Install dependencies
pip install django scikit-learn numpy joblib fpdf

# 4. Add the ML model
# Visit:[ https://www.kaggle.com/shyamatripathi](https://www.kaggle.com/shyamatripathi/datasets)
# Download: credit_score_model
# Place it inside the `predicto/` directory

# 5. Run the Django server
python manage.py runserver
