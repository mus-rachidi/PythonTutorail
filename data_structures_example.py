# Data structures example file

# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(f"List: {fruits}")

print("=" * 50)

# Tuple
vegetables = ("carrot", "potato", "onion")
print(f"Tuple: {vegetables}")

print("=" * 50)

# Set
unique_numbers = {1, 2, 3, 4, 4, 5}
unique_numbers.add(6)
print(f"Set: {unique_numbers}")

print("=" * 50)

# Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
person["email"] = "alice@example.com"
print(f"Dictionary: {person}")

print("=" * 50)

# Stack (using list)
stack = []
stack.append("first")
stack.append("second")
stack.append("third")
print(f"Stack before pop: {stack}")
stack.pop()
print(f"Stack after pop: {stack}")

print("=" * 50)

# Queue (using collections.deque)
from collections import deque
queue = deque(["first", "second", "third"])
print(f"Queue before popleft: {queue}")
queue.popleft()
print(f"Queue after popleft: {queue}")

print("=" * 50)

# Linked List (using collections.deque)
linked_list = deque([1, 2, 3])
linked_list.appendleft(0)
linked_list.append(4)
print(f"Linked List: {linked_list}")

print("=" * 50)

# Dictionary with default values (using collections.defaultdict)
from collections import defaultdict
default_dict = defaultdict(int)
default_dict["apples"] += 1
default_dict["bananas"] += 2
print(f"Default dictionary: {default_dict}")

print("=" * 50)

# Ordered Dictionary (using collections.OrderedDict)
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["first"] = 1
ordered_dict["second"] = 2
ordered_dict["third"] = 3
print(f"Ordered dictionary: {ordered_dict}")

print("=" * 50)

# Counter (using collections.Counter)
from collections import Counter
counter = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print(f"Counter: {counter}")

print("=" * 50)

# Named Tuple (using collections.namedtuple)
from collections import namedtuple
Point = namedtuple("Point", "x y")
point = Point(10, 20)
print(f"Named Tuple: {point}, x: {point.x}, y: {point.y}")

print("=" * 50)

# Example usage in a function
def summarize_data_structures():
    # Summarizing data structures in a dictionary
    summary = {
        "List": fruits,
        "Tuple": vegetables,
        "Set": unique_numbers,
        "Dictionary": person,
        "Stack": stack,
        "Queue": list(queue),
        "Linked List": list(linked_list),
        "Default Dictionary": dict(default_dict),
        "Ordered Dictionary": dict(ordered_dict),
        "Counter": dict(counter),
        "Named Tuple": point
    }
    return summary

data_summary = summarize_data_structures()
print("Data Structures Summary:")
for key, value in data_summary.items():
    print(f"{key}: {value}")
