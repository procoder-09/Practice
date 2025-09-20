x=lambda a,b:a*b


print(x(3,4))

nums=[2,3,5,6,7]

odd = list(filter(lambda x: x % 2 == 1, nums))

print(odd)


y=lambda x:x**2   #6**2 ---> 6 ==6*6

print(y(6))


power=list(map(lambda x:x**2,nums))
print(power)

from functools import reduce

no=[1,4,6,4]
z=reduce(lambda x,y:x*y,no)
print(z)

