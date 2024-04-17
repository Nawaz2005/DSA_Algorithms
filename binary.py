# Binary Search (assuming a sorted list)
arr = [3, 5, 8, 10, 12, 17]
target = 12
found = False

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        found = True
        index = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if found:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the list")
