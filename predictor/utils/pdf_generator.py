from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import os
import tempfile

def generate_credit_score_pdf(user_inputs, prediction):
    # Generate chart using matplotlib
    labels = list(user_inputs.keys())
    values = list(user_inputs.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color='#4e73df')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.title('User Financial Inputs Overview')

    # Save chart to temporary file
    temp_chart = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_chart.name, format='png')
    plt.close()

    # Create PDF
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

    pdf.ln(5)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt=f"Predicted Credit Score: {prediction}", ln=True)

    # Insert chart
    pdf.ln(10)
    pdf.image(temp_chart.name, x=25, w=160)

    # Footer
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Generated with SHYATRI.co", ln=True, align='C')

    # Clean up temporary file
    temp_chart.close()
    os.unlink(temp_chart.name)

    return pdf.output(dest='S').encode('latin-1')  # Binary content for response/download
