from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_sample_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4


    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Wedding Itinerary")

    c.setFont("Helvetica", 10)
    c.drawString(100, height - 140, "Day 1: Haldi Ceremony")
    c.drawString(100, height - 160, "Date: March 15, 2023")
    c.drawString(100, height - 180, "Time: 10:00 AM")
    c.drawString(100, height - 200, "Location: Family Residence")

    c.drawString(100, height - 240, "Day 2: Mehendi Function")
    c.drawString(100, height - 260, "Date: March 16, 2023")
    c.drawString(100, height - 280, "Time: 2:00 PM")
    c.drawString(100, height - 300, "Location: Community Hall")

    c.drawString(100, height - 340, "Day 2 Evening: Sangeet Night")
    c.drawString(100, height - 360, "Date: March 16, 2023")
    c.drawString(100, height - 380, "Time: 7:00 PM")
    c.drawString(100, height - 400, "Location: Banquet Hall")

    c.drawString(100, height - 440, "Day 3: Wedding Ceremony & Reception")
    c.drawString(100, height - 460, "Date: March 17, 2023")
    c.drawString(100, height - 480, "Time: 5:00 PM - Ceremony")
    c.drawString(100, height - 500, "Time: 7:00 PM - Reception")
    c.drawString(100, height - 520, "Location: Grand Ballroom")


    c.showPage()
    c.save()


generate_sample_pdf("/home/sakshi/Downloads/wedding_itinerary_sample.pdf")
