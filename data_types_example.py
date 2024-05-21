# Numeric Types
print("Numeric Types")
print("================")

# Integer
x = 10
print(f"x = {x}")
print(type(x))  # Output: <class 'int'>
print("----------------")

# Float
y = 3.14
print(f"y = {y}")
print(type(y))  # Output: <class 'float'>
print("----------------")

# Complex Number
z = 1 + 2j
print(f"z = {z}")
print(type(z))  # Output: <class 'complex'>
print("================\n")

# Sequence Types
print("Sequence Types")
print("================")

# String
s = "Hello, World!"
print(f"s = '{s}'")
print(type(s))  # Output: <class 'str'>
print("----------------")

# List
l = [1, 2, 3, "apple"]
print(f"l = {l}")
print(type(l))  # Output: <class 'list'>
print("----------------")

# Tuple
t = (1, 2, 3, "apple")
print(f"t = {t}")
print(type(t))  # Output: <class 'tuple'>
print("----------------")

# Range
r = range(1, 10)
print(f"r = {r}")
print(type(r))  # Output: <class 'range'>
print(list(r))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("----------------")

# Bytes
b = b'hello'
print(f"b = {b}")
print(type(b))  # Output: <class 'bytes'>
print("----------------")

# Byte Array
ba = bytearray(b'hello')
print(f"ba = {ba}")
print(type(ba))  # Output: <class 'bytearray'>
print("----------------")

# Memory View
mv = memoryview(b'hello')
print(f"mv = {mv}")
print(type(mv))  # Output: <class 'memoryview'>
print("================\n")

# Mapping Type
print("Mapping Type")
print("================")

# Dictionary
d = {"name": "Alice", "age": 25}
print(f"d = {d}")
print(type(d))  # Output: <class 'dict'>
print("================\n")

# Set Types
print("Set Types")
print("================")

# Set
set_a = {1, 2, 3, 4, 4}
print(f"set_a = {set_a}")
print(type(set_a))  # Output: <class 'set'>
print("----------------")

# Frozenset
set_b = frozenset([1, 2, 3, 4, 4])
print(f"set_b = {set_b}")
print(type(set_b))  # Output: <class 'frozenset'>
print("================\n")

# Boolean Type
print("Boolean Type")
print("================")

# Boolean
is_valid = True
print(f"is_valid = {is_valid}")
print(type(is_valid))  # Output: <class 'bool'>
print("================\n")

# None Type
print("None Type")
print("================")

# NoneType
n = None
print(f"n = {n}")
print(type(n))  # Output: <class 'NoneType'>
print("================\n")

# Other Built-in Types
print("Other Built-in Types")
print("================")

# Function
def func():
    return "Hello"

print(f"func = {func}")
print(type(func))  # Output: <class 'function'>
print("----------------")

# Lambda Function
lambda_func = lambda x: x * 2
print(f"lambda_func = {lambda_func}")
print(type(lambda_func))  # Output: <class 'function'>
print("----------------")

# Module
import math
print(f"math = {math}")
print(type(math))  # Output: <class 'module'>
print("----------------")

# Class
class MyClass:
    pass

obj = MyClass()
print(f"obj = {obj}")
print(type(obj))  # Output: <class '__main__.MyClass'>
print("----------------")

# Instance Method
class AnotherClass:
    def method(self):
        return "method"

another_obj = AnotherClass()
print(f"another_obj.method = {another_obj.method}")
print(type(another_obj.method))  # Output: <class 'method'>
print("================\n")

# Example Usage
print("Example Usage")
print("================")

name = "Alice"
age = 30
height = 5.5
is_student = False
favorites = ["reading", "coding", "hiking"]
person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
    "favorites": favorites
}

print(f"person_info = {person_info}")
print(type(person_info))  # Output: <class 'dict'>
print("================")
