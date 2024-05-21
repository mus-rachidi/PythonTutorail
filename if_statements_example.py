# If statement example file

# Basic if statement
number = 10
if number > 0:
    print("Number is positive")

# If-else statement
number = -5
if number > 0:
    print("Number is positive")
else:
    print("Number is non-positive")

# If-elif-else statement
number = 0
if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")

# Nested if statement
number = 15
if number > 0:
    print("Number is positive")
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# If statement with logical operators
number = 20
if number > 0 and number < 50:
    print("Number is positive and less than 50")

if number > 0 or number == -20:
    print("Number is positive or it is exactly -20")

# If statement with membership operators
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print("Fruit is in the list")

if "a" in fruit:
    print("Fruit contains the letter 'a'")

# If statement with comparison operators
a = 10
b = 20

if a < b:
    print("a is less than b")

if a != b:
    print("a is not equal to b")

# If statement with identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

if x is z:
    print("x and z are the same object")

if x is not y:
    print("x and y are not the same object")

if x == y:
    print("x and y have the same content")

# Example usage in a function
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

result = check_number(10)
print(f"check_number(10): {result}")

result = check_number(-5)
print(f"check_number(-5): {result}")

result = check_number(0)
print(f"check_number(0): {result}")
