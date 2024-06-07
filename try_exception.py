# built-in exceptions
########################################################################
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("That's not a valid number. Please try again.")

def divide_numbers():
    try:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
#########################################################################

# custom exception

class InvalidAgeError(Exception):
    """Exception raised for invalid age input."""
    
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age} -> {self.message}'

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

# divide_numbers()
# validate_age(130)