try:
     x=input("Enter a value:")
except ValueError:
     print("the value must be in positive")
else:
     print("given value is",x)
finally:
     print("sucesfully completed!")
        

