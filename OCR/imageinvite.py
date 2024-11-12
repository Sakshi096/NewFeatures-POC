from PIL import Image, ImageDraw, ImageFont

def generate_wedding_invite(file_path):

    width, height = 800, 1000
    background_color = (255, 250, 240)  # light beige for a classy look
    title_color = (139, 69, 19)  # dark brown for text
    text_color = (85, 85, 85)    # dark grey for text


    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)


    try:
        title_font = ImageFont.truetype("arial.ttf", 32)
        subtitle_font = ImageFont.truetype("arial.ttf", 20)
        text_font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()


    y_offset = 60


    draw.text((width // 2 - 100, y_offset), "Wedding Invitation", font=title_font, fill=title_color)
    y_offset += 60


    events = [
        {"title": "Day 1: Haldi Ceremony", "date": "March 15, 2023", "time": "10:00 AM", "location": "Family Residence"},
        {"title": "Day 2: Mehendi Function", "date": "March 16, 2023", "time": "2:00 PM", "location": "Community Hall"},
        {"title": "Day 2 Evening: Sangeet Night", "date": "March 16, 2023", "time": "7:00 PM", "location": "Banquet Hall"},
        {"title": "Day 3: Wedding Ceremony & Reception", "date": "March 17, 2023", "time": "5:00 PM - Ceremony", "location": "Grand Ballroom"},
        {"title": "Day 3 Evening: Reception", "date": "March 17, 2023", "time": "7:00 PM", "location": "Grand Ballroom"}
    ]


    for event in events:
        draw.text((50, y_offset), event["title"], font=subtitle_font, fill=title_color)
        y_offset += 30
        draw.text((70, y_offset), f"Date: {event['date']}", font=text_font, fill=text_color)
        y_offset += 25
        draw.text((70, y_offset), f"Time: {event['time']}", font=text_font, fill=text_color)
        y_offset += 25
        draw.text((70, y_offset), f"Location: {event['location']}", font=text_font, fill=text_color)
        y_offset += 50  # Add space between events


    image.save(file_path)
    print(f"Wedding invite image saved to {file_path}")


generate_wedding_invite("/home/sakshi/Downloads/wedding_invite.png")
