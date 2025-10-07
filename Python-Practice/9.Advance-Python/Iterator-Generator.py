my_list = [1, 2, 3]
a = iter(my_list)

print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 3
# print(next(it))  # StopIteration error

def squares(n):
    for i in range(n):
        yield i ** 2

gen = squares(5)
print("-------------")
for val in gen:
    print(val)
