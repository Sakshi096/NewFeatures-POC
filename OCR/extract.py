import pytesseract
from pdf2image import convert_from_path
from PIL import Image


pdf_path = "/home/sakshi/Downloads/wedding_itinerary_sample.pdf"



images = convert_from_path(pdf_path)


keywords = ["Haldi", "Mehendi", "Sangeet", "Reception"]


for i, image in enumerate(images):

    text = pytesseract.image_to_string(image)
    
    print(f"--- Page {i+1} ---")
    print(text)  # Print raw OCR text for reference


    matched_events = [keyword for keyword in keywords if keyword.lower() in text.lower()]
    print("Matched Events:", matched_events)
