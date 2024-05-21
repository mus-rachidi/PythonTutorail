# List, Tuple, and Set Example

# List Example
fruits_list = ["apple", "banana", "cherry"]
print("List Example:")
print("Initial List:", fruits_list)
fruits_list.append("orange")  # Lists are mutable, so you can modify them
print("After Adding 'orange':", fruits_list)
print("=" * 50)

# Tuple Example
vegetables_tuple = ("carrot", "potato", "onion")
print("Tuple Example:")
print("Initial Tuple:", vegetables_tuple)
# Tuples are immutable, you cannot modify them after creation
# This line will cause an error: vegetables_tuple.append("tomato")
print("Tuples cannot be modified after creation")
print("=" * 50)

# Set Example
unique_numbers_set = {1, 2, 3, 4, 4, 5}
print("Set Example:")
print("Initial Set:", unique_numbers_set)
unique_numbers_set.add(6)  # Sets are mutable, but they only contain unique elements
print("After Adding '6':", unique_numbers_set)
print("Sets ignore duplicate elements:", unique_numbers_set)
print("=" * 50)

# Conclusion
print("Conclusion:")
print("Lists are ordered, mutable collections that can contain duplicates.")
print("Tuples are ordered, immutable collections that can contain duplicates.")
print("Sets are unordered, mutable collections that only contain unique elements.")
