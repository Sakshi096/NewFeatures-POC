from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

def create_wedding_video_invite(output_path):
    width, height = 1280, 720  # HD resolution
    duration_per_event = 3  # seconds per event
    fps = 24  # Frames per second
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path to a TTF font
    background_color = (255, 250, 240)  # Light beige background color


    events = [
        {"title": "Day 1: Haldi Ceremony", "date": "March 15, 2023", "time": "10:00 AM", "location": "Family Residence"},
        {"title": "Day 2: Mehendi Function", "date": "March 16, 2023", "time": "2:00 PM", "location": "Community Hall"},
        {"title": "Day 2 Evening: Sangeet Night", "date": "March 16, 2023", "time": "7:00 PM", "location": "Banquet Hall"},
        {"title": "Day 3: Wedding Ceremony", "date": "March 17, 2023", "time": "5:00 PM", "location": "Grand Ballroom"},
        {"title": "Day 3 Evening: Reception", "date": "March 17, 2023", "time": "7:00 PM", "location": "Grand Ballroom"}
    ]


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec for .mp4
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


    for event in events:
        text_content = (
            f"{event['title']}\n"
            f"Date: {event['date']}\n"
            f"Time: {event['time']}\n"
            f"Location: {event['location']}"
        )
        
        for _ in range(duration_per_event * fps):

            img = Image.new("RGB", (width, height), background_color)
            draw = ImageDraw.Draw(img)


            try:
                font = ImageFont.truetype(font_path, 40)
            except IOError:
                font = ImageFont.load_default()
            

            text_x, text_y = 100, 100
            draw.multiline_text((text_x, text_y), text_content, fill="black", font=font, align="left")


            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR format for OpenCV


            video_writer.write(frame)


    video_writer.release()
    print(f"Video invite saved to {output_path}")


output_path = "/home/sakshi/Downloads/wedding_invite_video_opencv.mp4"
create_wedding_video_invite(output_path)
