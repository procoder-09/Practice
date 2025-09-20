# import math

# x=math.sqrt(25)
# y=math.pi
# print(x)
# print(y)

# from math import sqrt,pi

# print(sqrt(49))

import math as m

print(m.sqrt(81))

import greeting

greeting.greet("Ramya")

import datetime

present=datetime.datetime.now()

print(present)
print(present.date())
print(present.time())
future = present + datetime.timedelta(days=20)
print(future.date())