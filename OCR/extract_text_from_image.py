import pytesseract
from PIL import Image




def extract_text_from_image(image_path):

    image = Image.open(image_path)
    

    extracted_text = pytesseract.image_to_string(image)
    

    print("Extracted Text from Image:\n")
    print(extracted_text)
    return extracted_text


image_path = "/home/sakshi/Downloads/wedding_invite.png"


extracted_text = extract_text_from_image(image_path)
