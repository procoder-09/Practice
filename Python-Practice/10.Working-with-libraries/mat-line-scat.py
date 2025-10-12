import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, color='blue', marker='o', linestyle='--', label='Sales')
plt.title("Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.show()

x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color='red', label='Scores')
plt.title("Scatter Plot Example")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()