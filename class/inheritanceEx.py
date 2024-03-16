class Dog:
    def __init__(super, name, age):
        super.name = name
        super.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
    
marvin = GoldenRetriever("Marvin", 3)

print(marvin)
print(marvin.speak())