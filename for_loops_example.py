# For loop example file

# Basic for loop with a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"Number: {number}")

print("=" * 50)

# For loop with a string
text = "Hello"
for char in text:
    print(f"Character: {char}")

print("=" * 50)

# For loop with a range
for i in range(5):
    print(f"Range value: {i}")

print("=" * 50)

# For loop with a range with start and stop
for i in range(1, 6):
    print(f"Range value with start: {i}")

print("=" * 50)

# For loop with a range with step
for i in range(0, 10, 2):
    print(f"Range value with step: {i}")

print("=" * 50)

# For loop with a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

print("=" * 50)

# For loop with dictionary items
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

print("=" * 50)

# Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")

print("=" * 50)

# For loop with break statement
for i in range(10):
    if i == 5:
        break
    print(f"Value before break: {i}")

print("=" * 50)

# For loop with continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd value: {i}")

print("=" * 50)

# For loop with else statement
for i in range(5):
    print(f"Value: {i}")
else:
    print("Loop completed without break")

print("=" * 50)

# For loop with else and break statement
for i in range(5):
    if i == 3:
        break
    print(f"Value before break: {i}")
else:
    print("This will not be printed because of the break")

print("=" * 50)

# For loop with enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

print("=" * 50)

# For loop with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

print("=" * 50)

# Example usage in a function
def print_even_numbers(n):
    even_numbers = []
    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(f"Even numbers up to 10: {print_even_numbers(10)}")
