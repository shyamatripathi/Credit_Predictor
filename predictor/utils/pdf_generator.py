from fpdf import FPDF
from datetime import datetime

def generate_credit_score_pdf(user_inputs, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Credit Score Prediction Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt="User Inputs:", ln=True)
    for key, value in user_inputs.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt=f"Predicted Credit Score: {prediction}", ln=True)

    pdf.ln(20)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Generated with SHYATRI.co", ln=True, align='C')

    # Save or return content
    return pdf.output(dest='S').encode('latin-1')  # Returns binary content for download
