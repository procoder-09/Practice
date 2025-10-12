import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200
print(response.json())

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)  # 201 (Created)
print(response.json())

headers = {"Authorization": "Bearer YOUR_TOKEN"}

response = requests.get("https://api.example.com/data", headers=headers)
print(response.status_code)

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.json())