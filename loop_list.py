# Example 1: Printing each element in a list
fruits = ["apple", "banana", "cherry"]
print("Example 1: Printing each element in a list")
for fruit in fruits:
    print(fruit)

print("\n")

# Example 2: Creating a list of squares
squares = [x**2 for x in range(10)]
print("Example 2: Creating a list of squares")
print(squares)

print("\n")

# Example 3: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print("Example 3: Filtering even numbers from a list")
print(evens)

print("\n")

# Example 4: Multiplication table
multiplication_table = []
for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i * j)
    multiplication_table.append(row)
print("Example 4: Multiplication table")
for row in multiplication_table:
    print(row)

print("\n")

# Example 5: Transposing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = []
for i in range(len(matrix[0])):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose.append(transpose_row)
print("Example 5: Transposing a matrix")
print(transpose)

print("\n")

# Example 6: Removing elements that meet a condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [num for num in numbers if num % 2 != 0]
print("Example 6: Removing elements that meet a condition")
print(numbers)

print("\n")

# Example 7: Calculating the sum of all elements in a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Example 7: Calculating the sum of all elements in a list")
print(total)

print("\n")

# Example 8: Finding the maximum element in a list
numbers = [1, 2, 3, 4, 5]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Example 8: Finding the maximum element in a list")
print(maximum)

print("\n")

# Example 9: Reversing a list
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for num in reversed(numbers):
    reversed_numbers.append(num)
print("Example 9: Reversing a list")
print(reversed_numbers)

print("\n")

# Example 10: Checking if a list has duplicates
numbers = [1, 2, 3, 4, 5, 2]
has_duplicates = len(numbers) != len(set(numbers))
print("Example 10: Checking if a list has duplicates")
print(has_duplicates)

print("\n")

# Example 11: Flattening a list of lists
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print("Example 11: Flattening a list of lists")
print(flattened_list)

print("\n")

# Example 12: Zipping two lists into a list of tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print("Example 12: Zipping two lists into a list of tuples")
print(zipped)

print("\n")

# Example 13: Using enumerate() to get index and value
fruits = ["apple", "banana", "cherry"]
print("Example 13: Using enumerate() to get index an
