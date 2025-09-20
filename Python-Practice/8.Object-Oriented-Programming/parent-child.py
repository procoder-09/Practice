class parent():
    def sample(self):
        print("sky is blue")
class child(parent):
    def sample(self):
        print("Sky is red")

p1=child()
print(p1.sample())


class parent():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f" I am {self.name} and my age is {self.age}")
class child(parent):
    def __init__(self,job):
        super().__init__("Alsa",30)
        self.job=job
    def greet(self):
        print(f"I am {self.name} my age is {self.age} working as {self.job}")
        # print(super().greet())

# p1=parent("Amma",20)
p2=child("engineer")
print(p2.greet())