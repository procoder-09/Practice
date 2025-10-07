with open("file.txt", "w") as f:
    f.write("Hello World \n")
    f.write("Hello Python")

class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext() as d:
    print("Inside context")
