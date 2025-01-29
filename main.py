import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Compute the Euclidean distance between two points
def compute_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

# Brute force method to find the smallest distance among points
def brute_force(points):
    num_points = len(points)
    min_distance = float("inf")
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = compute_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

# Find the smallest distance in the strip (sorted by y-coordinate)
def closest_in_strip(strip, min_distance):
    strip.sort(key=lambda point: point.y)  # Sort by y-coordinate
    size = len(strip)
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) >= min_distance:
                break
            distance = compute_distance(strip[i], strip[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

# Recursive function to find the smallest distance
def closest_recursive(points_sorted_by_x):
    num_points = len(points_sorted_by_x)

    # Base case: Use brute force for small number of points
    if num_points <= 3:
        return brute_force(points_sorted_by_x)

    # Divide the points into two halves
    mid = num_points // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]
    midpoint = points_sorted_by_x[mid]

    # Recursively find the smallest distance in both halves
    min_left = closest_recursive(left_half)
    min_right = closest_recursive(right_half)
    min_distance = min(min_left, min_right)

    # Create a strip of points near the dividing line
    strip = [point for point in points_sorted_by_x if abs(point.x - midpoint.x) < min_distance]

    # Find the smallest distance in the strip
    return min(min_distance, closest_in_strip(strip, min_distance))

# Main function to find the closest pair of points
def closest_pair(points):
    # Sort points by x-coordinate
    points_sorted_by_x = sorted(points, key=lambda point: point.x)
    return closest_recursive(points_sorted_by_x)

if __name__ == "__main__":
    points = [Point(20, 35), Point(15, 35), Point(67, 80), Point(3, 4), Point(121, 110), Point(1, 0)]
    result = closest_pair(points)
    print("The smallest distance is", result)
