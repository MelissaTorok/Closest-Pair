import math
import time
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Compute the Euclidean distance between two points
def compute_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

# Brute-force method to find the smallest distance among points
def brute_force_closest_pair(points):
    num_points = len(points)
    min_distance = float("inf")  # Initialize with a large value
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = compute_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

# Function to generate random points
def generate_random_points(n, x_range=(0, 1000), y_range=(0, 1000)):
    return [Point(random.randint(*x_range), random.randint(*y_range)) for _ in range(n)]

# Test the brute-force algorithm with different datasets
def test_brute_force_closest_pair():
    # Define datasets
    light_data = generate_random_points(100)  # 100 points
    medium_data = generate_random_points(1000)  # 1000 points
    heavy_data = generate_random_points(10000)  # 10000 points

    datasets = {
        "Light Data (100 points)": light_data,
        "Medium Data (1000 points)": medium_data,
        "Heavy Data (10000 points)": heavy_data
    }

    # Test each dataset
    for name, data in datasets.items():
        print(f"Testing {name}...")
        start_time = time.time()
        result = brute_force_closest_pair(data)
        end_time = time.time()
        print(f"Smallest distance: {result}")
        print(f"Time taken: {end_time - start_time:.6f} seconds\n")

if __name__ == "__main__":
    test_brute_force_closest_pair()
