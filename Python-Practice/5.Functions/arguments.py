def fun(*nums): # Args
        print(nums)
    

fun(3,5,6)
fun(4,6,7,8,4,3)

def todo(**kwargs):
        print(kwargs)

todo(name="amma",age=20)
todo(name="bobby",age=15,job="teacher")

def person(name,age,*hobbies,**details):
        print(name)
        print(age)
        print(hobbies)
        print(details)

person("Alsa", 17, "cricket","painting", job="singer", location="hyd")
