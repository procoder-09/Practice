def greet():
    name="Amma"  # Local variable
    print(name)

greet()


x=10  # Global variable

def inc():
    global x  # mentioning the value in global
    x+=1
    print( "value",x)

inc()


def outer():
    x="main content"
    def inner():
        nonlocal x
        x="modified content"
    inner()
    print(x)


outer()