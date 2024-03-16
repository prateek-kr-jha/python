class Parent:
    hair_color = "Brown"
    speaks = ["English"]
    

class Child(Parent):
    hair_color = "Purple"
    def __init__(self):
        super().__init__()
        self.speaks.append("German")
    

kid = Child()
print(kid.hair_color)