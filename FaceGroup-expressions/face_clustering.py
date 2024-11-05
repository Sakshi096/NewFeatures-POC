import os
import config
from face_model import load_model, get_face_embedding
from Clustering import cluster_faces
from utils import load_images_from_directory, log_clustering_results, convert_tiff_to_jpg
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the face clustering process.")
    
    if not os.path.exists(config.IMAGE_DIR):
        logging.error(f"Image directory does not exist: {config.IMAGE_DIR}")
        return
    else:
        logging.info(f"Image directory verified: {config.IMAGE_DIR}")

    if not os.path.exists(config.EMBEDDING_DIR):
        os.makedirs(config.EMBEDDING_DIR)
        logging.info(f"Created embeddings directory: {config.EMBEDDING_DIR}")
    else:
        logging.info(f"Embeddings directory verified: {config.EMBEDDING_DIR}")

    model = load_model()
    if model:
        logging.info("Model loaded successfully.")
    else:
        logging.error("Failed to load model.")
        return

    image_paths = load_images_from_directory(config.IMAGE_DIR)
    processed_image_paths = []
    
    for image_path in image_paths:
        if image_path.endswith(".tiff"):
            converted_path = convert_tiff_to_jpg(image_path)
            if converted_path:
                processed_image_paths.append(converted_path)
                logging.info(f"Converted {image_path} to {converted_path}")
        else:
            processed_image_paths.append(image_path)

    embeddings = []
    valid_image_paths = []
    
    for image_path in processed_image_paths:
        embedding = get_face_embedding(model, image_path)
        if embedding is not None:
            embeddings.append(embedding)
            valid_image_paths.append(image_path)
            
            embedding_file = os.path.join(config.EMBEDDING_DIR, os.path.basename(image_path) + '.npy')
            np.save(embedding_file, embedding)
            logging.info(f"Saved embedding for {image_path} to {embedding_file}")
        else:
            logging.warning(f"No face detected or embedding could not be generated for {image_path}")

    if embeddings:
        logging.info(f"Starting clustering on {len(embeddings)} embeddings.")
        labels = cluster_faces(embeddings)
        log_clustering_results(labels, valid_image_paths, config.OUTPUT_DIR)
        logging.info(f"Clustering completed with {len(set(labels))} clusters.")
    else:
        logging.warning("No embeddings available for clustering.")

    logging.info("Face clustering process completed.")
    

if __name__ == "__main__":
    main()
