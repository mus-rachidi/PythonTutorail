# Arguments and Parameters Example

# Function with positional arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")


# Function with keyword arguments and default parameter values
def greet_with_defaults(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")


# Function with variable-length arguments
def greet_all(*names, greeting="Hello"):
    for name in names:
        print(f"{greeting}, {name}!")


# Example usage
if __name__ == "__main__":
    # Using positional arguments
    print("Using positional arguments:")
    greet("Alice", "Hi")

    # Using keyword arguments
    print("\nUsing keyword arguments:")
    greet(greeting="Bonjour", name="Bob")

    # Using default parameter values
    print("\nUsing default parameter values:")
    greet_with_defaults()
    greet_with_defaults("Charlie")
    greet_with_defaults(greeting="Hola")
    greet_with_defaults(name="David")

    # Using variable-length arguments
    print("\nUsing variable-length arguments:")
    greet_all("Emily", "Frank", "Grace")
    greet_all("Henry", "Ivy", greeting="Hi")
