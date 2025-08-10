def is_sorted(arr):
    # Loop through each element and check if the next one is smaller
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
if is_sorted(arr):
    print("The array is sorted.")
else:
    print("The array is not sorted.")
