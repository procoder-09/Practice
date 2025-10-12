import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [250, 400, 150, 500]

plt.bar(products, sales, color='green')
plt.title("Product Sales")  # title name
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

ages = [22, 25, 30, 25, 22, 30, 35, 40]

plt.hist(ages, bins=5, color='orange', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()