# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Derived class (Child class) extending Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Inherit attributes from the parent class
        self.breed = breed
    
    def speak(self):  # Overriding the speak method
        return f"{self.name} barks"

# Another derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Creating instances of the child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows
