# Import necessary libraries
import random

# Function to perform Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk from {source} to {target}")
    else:
        tower_of_hanoi(n-1, source, auxiliary, target)
        print(f"Move disk from {source} to {target}")
        tower_of_hanoi(n-1, auxiliary, target, source)

# Function to perform Coin Change
def coin_change(amount):
    coins = [50, 20, 10, 5, 1]
    result = []
    
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    
    return result

# Main function to solve puzzle
def solve_puzzle():
    # Randomly select the number of disks
    num_disks = random.randint(3, 5)
    
    # Randomly choose the source and target disks
    source = random.randint(1, num_disks)
    target = random.randint(1, num_disks)
    auxiliary = random.randint(1, num_disks)
    
    # Display the initial state of the puzzle
    print(f"Initial State: Source={source}, Target={target}, Auxiliary={auxiliary}")
    
    # Perform the Tower of Hanoi
    tower_of_hanoi(num_disks, source, target, auxiliary)
    
    # Display the final state of the puzzle
    print(f"Final State: Source={source}, Target={target}, Auxiliary={auxiliary}")

# Execute the main function
solve_puzzle()