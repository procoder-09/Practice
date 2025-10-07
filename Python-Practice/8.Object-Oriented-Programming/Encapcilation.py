class Sample:
    def __init__(self,name,age,job):
        self.name=name  #public
        self._age=age   #protected
        self.__job=job  #private
    def get_job(self):
        return self.__job
    def set_job(self,job):
        self.__job=job
        return self.__job
    def __str__(self):
       print(f"my name is{self.name} and age {self._age}working in {self.__job}")

b=Sample("Asma",20,"developer")
print(b.name)

b.name="Amma"
print(b.name)
print(b._age)
b._age=25
print(b._age)

# print(b.__job)

print(b.get_job())
b.set_job("engineer")
print(b.get_job())
