def rotate_matrix(matrix):
    """
    Rotate a square matrix 90 degrees clockwise.

    Args:
    matrix (list of lists): A square matrix represented as a list of lists.

    Returns:
    list of lists: The rotated matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Swap elements from top-left to bottom-right
    for i in range(rows // 2):
        for j in range(cols // 2):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swap elements from bottom-right to top-left
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nRotated Matrix:")
for row in rotated_matrix:
    print(row)