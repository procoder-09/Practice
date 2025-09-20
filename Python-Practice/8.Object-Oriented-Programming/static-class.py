class person:
    name="Alsa"
    @classmethod
    def detail(cls):
        print(f"here person name is ",cls.name)
    @staticmethod
    def greet():
        print("this is a static method")

p1=person()

p2=person()

print(p1.detail())
print(p1.greet())

# print("printing p2 details")

# print(p2.detail())


