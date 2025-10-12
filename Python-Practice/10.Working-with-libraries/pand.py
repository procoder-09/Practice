import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "Chicago"],
    "Job":["engineer","Arctect","Doctor"]
}

df = pd.DataFrame(data)
print(df)

print("-----------------")
print(df["Name"])
print(df.Job[1])

# Save to CSV which is a comma sepaerated value
df.to_csv("employees.csv", index=False)

# Read CSV
df2 = pd.read_csv("employees.csv")
print(df2)