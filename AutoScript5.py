# Import necessary libraries
from typing import List

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def min_binary_search_tree(arr: List[int]) -> TreeNode:
    """
    Constructs a minimal binary search tree from a given array.

    Parameters:
    arr (List[int]): A list of integers representing the array.

    Returns:
    TreeNode: The root of the constructed BST.
    """
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = min_binary_search_tree(arr[:mid])
    root.right = min_binary_search_tree(arr[mid+1:])

    return root

def priority_queue(arr: List[int]) -> List[int]:
    """
    Constructs a priority queue from a given array.

    Parameters:
    arr (List[int]): A list of integers representing the array.

    Returns:
    List[int]: The elements of the priority queue in ascending order.
    """
    from heapq import heappush, heappop

    priority_queue = []
    for num in arr:
        heappush(priority_queue, num)

    result = []
    while priority_queue:
        result.append(heappop(priority_queue))

    return result

# Example usage
if __name__ == "__main__":
    # Test cases
    print("Test Case 1:", min_binary_search_tree([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    print("Test Case 2:", priority_queue([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))