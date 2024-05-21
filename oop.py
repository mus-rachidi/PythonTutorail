# Object-Oriented Programming (OOP) Example in Python

# Define a class
class Animal:
    # Class attribute
    species = "Mammal"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def speak(self):
        return f"{self.name} says: Hello!"

# Define a subclass
class Dog(Animal):
    # Constructor (initializer)
    def __init__(self, name, age, breed):
        # Call the superclass constructor
        super().__init__(name, age)
        # Additional instance attribute
        self.breed = breed

    # Override the speak method
    def speak(self):
        return f"{self.name} barks: Woof!"

# Main function
if __name__ == "__main__":
    # Create an instance of the Animal class
    animal = Animal("Tom", 5)
    print("Animal:", animal.name)
    print("Species:", animal.species)
    print("Age:", animal.age)
    print("Speak:", animal.speak())
    print("=" * 50)

    # Create an instance of the Dog class
    dog = Dog("Buddy", 3, "Labrador")
    print("Dog:", dog.name)
    print("Species:", dog.species)
    print("Breed:", dog.breed)
    print("Age:", dog.age)
    print("Speak:", dog.speak())
