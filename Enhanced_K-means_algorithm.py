import math

def contains_positive_and_negative(data_points):
    return any(any(attr > 0 and attr < 0 for attr in point) for point in data_points)

def find_global_min(data_points):
    return min(attr for point in data_points for attr in point)

def subtract_global_min(data_points, global_min):
    return [[attr - global_min for attr in point] for point in data_points]

def calculate_distances_from_origin(data_points):
    return [math.sqrt(sum(attr ** 2 for attr in point)) for point in data_points]

def sort_data_points(data_points, distances):
    sorted_indices = sorted(range(len(distances)), key=lambda k: distances[k])
    return [data_points[i] for i in sorted_indices]

def partition_into_clusters(sorted_data_points, k):
    cluster_size = len(sorted_data_points) // k
    remainder = len(sorted_data_points) % k
    return [sorted_data_points[i * cluster_size + min(i, remainder):(i + 1) * cluster_size + min(i + 1, remainder)] for i in range(k)]

def take_middle_as_centroids(clusters):
    return [cluster[len(cluster) // 2] for cluster in clusters]

def calculate_distances_to_centroids(data_points, centroids):
    distances = {}

    for i, point in enumerate(data_points):
        point_distances = [math.sqrt(sum((attr - cent) ** 2 for attr, cent in zip(point, centroid))) for centroid in centroids]
        distances[i] = point_distances

    return distances

def recalculate_centroids(cluster_id, data_points, k):
    new_clusters = [[] for _ in range(k)]

    for key, cluster_idx in zip(range(len(data_points)), cluster_id):
        new_clusters[cluster_idx].append(data_points[key])

    new_centroids = []
    for cluster in new_clusters:
        centroid = tuple(sum(coord) / len(cluster) for coord in zip(*cluster)) if cluster else None
        new_centroids.append(centroid)

    return new_clusters, new_centroids

# Example usage with a dataset and desired number of clusters
dataset = [
    [1, 2],
    [3, 4],
    [-1, -2],
    [-3, -4],
    [0, 0]
]

k = 2

# Step 1: Check for positive and negative attribute values
if contains_positive_and_negative(dataset):
    # Step 2-3: Find global min and subtract from each attribute
    global_min = find_global_min(dataset)
    adjusted_data = subtract_global_min(dataset, global_min)
else:
    # If no negative values, use the original data
    adjusted_data = dataset

# Step 4: Calculate distances from the origin
distances_from_origin = calculate_distances_from_origin(adjusted_data)

# Step 5: Sort data points based on distances
sorted_data_points = sort_data_points(adjusted_data, distances_from_origin)

# Step 6: Partition sorted data points into k equal sets
clusters = partition_into_clusters(sorted_data_points, k)

# Step 7: Take middle point in each set as initial centroids
initial_centroids = take_middle_as_centroids(clusters)


print("Initial Centroids:", initial_centroids)
