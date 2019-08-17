import math
from scipy import spatial


def average_minimals(samples):
    samples.sort()
    quartile_size = math.ceil(len(samples) / 4.0)
    return sum(samples[0:quartile_size]) / quartile_size


def compute_embedding_distances(embeddingset1, embeddingset2):
    distances = []
    for embedding1 in embeddingset1:
        for embedding2 in embeddingset2:
            distance = spatial.distance.cosine(embedding1, embedding2)
            distances.append(distance)
    return distances
