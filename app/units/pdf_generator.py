from reportlab.pdfgen import canvas

def generate_pdf(name):

    pdf = canvas.Canvas(
        f"{name}.pdf"
    )

    pdf.drawString(
        100,
        750,
        "Attendance Report"
    )

    pdf.save()