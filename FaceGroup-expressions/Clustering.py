
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import DBSCAN
import numpy as np
import config

def calculate_similarity(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0]

def cluster_faces(embeddings):
    clustering_model = DBSCAN(eps=config.CLUSTERING_EPS, min_samples=config.CLUSTERING_MIN_SAMPLES, metric='cosine')
    labels = clustering_model.fit_predict(embeddings)
    return labels
