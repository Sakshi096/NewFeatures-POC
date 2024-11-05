
import insightface
import config
import cv2

def load_model():
    model = insightface.app.FaceAnalysis(name=config.MODEL_NAME)
    ctx_id = 0 if config.USE_GPU else -1
    model.prepare(ctx_id=ctx_id)
    print("Model loaded successfully.")  # Confirm model is loaded
    return model

def get_face_embedding(model, image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = model.get(image_rgb)

    print(f"Processing {image_path}, found {len(faces)} faces.")  # Debug statement
    
    if faces:
        for i, face in enumerate(faces):
            print(f"Face {i}: {face.bbox}, embedding: {face.embedding}")  
        return faces[0].embedding  
    else:
        print(f"No faces detected in {image_path}") 
        return None