class person:
    name="Amma"
    def __init__(self,age):
        self.age=age
    def greet(self):
        print(f"my name is {self.name} and age is {self.age} ")

p1=person(20)
p2=person(25)

print(p2.greet())
print(p1.greet())

print(p1.age)

p1.age=30

print(p1.age)