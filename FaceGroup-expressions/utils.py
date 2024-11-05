
import os

def load_images_from_directory(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.tiff'))]

def log_clustering_results(labels, image_paths):
    clusters = {}
    for label, image_path in zip(labels, image_paths):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(image_path)
    
    print("Clustering Results:")
    for cluster_id, images in clusters.items():
        print(f"Cluster {cluster_id}:")
        for img_path in images:
            print(f" - {img_path}")
            
import cv2
def convert_tiff_to_jpg(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    new_path = image_path.replace(".tiff", ".jpg")
    cv2.imwrite(new_path, img)
    return new_path

def save_clustering_results(labels, image_paths):
    clusters = {}
    for label, image_path in zip(labels, image_paths):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(image_path)
    
    print("Clustering Results:")
    for cluster_id, images in clusters.items():
        print(f"\nCluster {cluster_id}:")
        for img_path in images:
            print(f" - {img_path}")

    with open("clustering_results.txt", "w") as f:
        for cluster_id, images in clusters.items():
            f.write(f"\nCluster {cluster_id}:\n")
            for img_path in images:
                f.write(f" - {img_path}\n")
                
def log_clustering_results(labels, image_paths, output_dir):
    clusters = {}
    for label, image_path in zip(labels, image_paths):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(image_path)
    
    # Save to a file in the output directory
    output_file = os.path.join(output_dir, "clustering_results.txt")
    with open(output_file, "w") as f:
        for cluster_id, images in clusters.items():
            f.write(f"Cluster {cluster_id}:\n")
            for img_path in images:
                f.write(f" - {img_path}\n")
    
    print(f"Clustering results saved to {output_file}")