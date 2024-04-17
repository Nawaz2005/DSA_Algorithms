def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the array

# Get user input for the array elements
arr = input("Enter the array elements separated by spaces: ").split()
arr = [int(x) for x in arr]

# Get user input for the target element
target = int(input("Enter the target element to search for: "))

result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")