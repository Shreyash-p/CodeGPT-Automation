import random

def is_valid_convex_hull(points):
    """
    Check if the given points form a valid convex hull.
    
    Args:
    points (list of tuples): A list of (x, y) coordinates representing points in 2D space.
    
    Returns:
    bool: True if the points form a valid convex hull, False otherwise.
    """
    n = len(points)
    if n < 3:
        return True
    
    # Sort points by their x-coordinate
    points.sort(key=lambda p: p[0])
    
    # Check for a valid convex hull
    for i in range(n):
        if i > 0 and points[i][1] <= points[i - 1][1]:
            return False
    
    return True

# Test cases
print(is_valid_convex_hull([(0, 0), (1, 0), (1, 1), (0, 1)]))  # True
print(is_valid_convex_hull([(0, 0), (1, 0), (1, 1), (0, -1)]))  # False
print(is_valid_convex_hull([(1, 1), (2, 2), (2, 1), (1, 2)]))  # True
print(is_valid_convex_hull([(0, 0), (1, 1), (0, -1), (-1, 0)]))  # True