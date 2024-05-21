# Mutable and Immutable Objects Example

# Function to modify a list (mutable)
def modify_list(my_list):
    my_list.append(4)
    print("Inside modify_list:", my_list)

# Function to modify an integer (immutable)
def modify_int(my_int):
    my_int += 1
    print("Inside modify_int:", my_int)

# Main function
if __name__ == "__main__":
    # Example with a list (mutable)
    original_list = [1, 2, 3]
    print("Original List:", original_list)
    modify_list(original_list)
    print("After modify_list:", original_list)
    print("=" * 50)

    # Example with an integer (immutable)
    original_int = 10
    print("Original Integer:", original_int)
    modify_int(original_int)
    print("After modify_int:", original_int)
