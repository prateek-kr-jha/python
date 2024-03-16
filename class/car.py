class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"
    def about(self):
        return f"The {self.color} car has {self.mileage} miles"

c1 = Car("blue", 20000)
print(c1)
c2 = Car("red", 30000)
print(c2)