import requests

# Replace this with your actual token
TOKEN = "e8e3a22c7c4b40d8cee2e755c0f82d8f8e5d704f"

# Set the request headers with the token
headers = {"Authorization": f"Token {TOKEN}"}

# Make a GET request to fetch tasks
response = requests.get("http://127.0.0.1:8000/api/tasks/", headers=headers)

# Print the response (either tasks or an error message)
print(response.json())
