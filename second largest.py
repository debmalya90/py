# Input list
numbers = [10, 20, 4, 45, 99]

# Remove duplicates to handle cases like [10, 10, 20]
unique_numbers = list(set(numbers))

# Sort in descending order
unique_numbers.sort(reverse=True)

# Second largest is at index 1
if len(unique_numbers) >= 2:
    print("Second largest element is:", unique_numbers[1])
else:
    print("Not enough elements to find second largest.")
