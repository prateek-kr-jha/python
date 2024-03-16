# dog.py

class Dog:
    # calss attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        # instance attributes
        # print(self)
        self.name = name
        self.age = age
    
    # special instance method __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("miles", 4)
print(miles.description())
print(miles.speak("woof woof"))
print(miles)