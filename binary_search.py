def binary_search(arr, target):
    # Initial boundaries of the search
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Find the middle element
        mid = (left + right) // 2

        # Check if the target is at the mid index
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Ignore the left half
        else:
            right = mid - 1  # Ignore the right half

    # If the target is not found
    return -1

# Example usage
if __name__ == "__main__":
    # Sorted array
    array = [2, 4, 7, 10, 13, 18, 20, 22, 29, 31, 33, 37]
    target = int(input("Enter the target value to search for: "))
    
    # Perform binary search
    result = binary_search(array, target)
    
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")
