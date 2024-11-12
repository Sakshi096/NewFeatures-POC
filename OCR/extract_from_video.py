import cv2
import pytesseract




def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get the video frame rate
    frame_interval = int(fps * 3)  # Capture one frame every 3 seconds

    extracted_texts = []

    frame_count = 0
    success, frame = cap.read()
    while success:

        if frame_count % frame_interval == 0:

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            

            text = pytesseract.image_to_string(gray_frame)
            
            if text.strip():  # If any text is detected, add it to results
                extracted_texts.append(text.strip())
                print(f"Extracted text from frame {frame_count}:")
                print(text.strip())
                print("=" * 50)


        frame_count += 1
        success, frame = cap.read()


    cap.release()

    return extracted_texts


video_path = "/home/sakshi/Downloads/wedding_invite_video_opencv.mp4"
extracted_texts = extract_text_from_video(video_path)


print("\nConsolidated extracted text:")
for i, text in enumerate(extracted_texts, start=1):
    print(f"\nText Block {i}:")
    print(text)
