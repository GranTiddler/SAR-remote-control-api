import requests


# Set the model and prompt
text = input("kill me")
# Set the request parameters
params = {
    "text":text,
    "layer":"DefaultTextLayer"
}

# Set the request headers
headers = {
  "Content-Type": "application/json"
}

# Make the request
response = requests.post(
  f"http://172.22.174.74/api/text/display?text={text}&layer=DefaultTextLayer",
  json=params,
  headers=headers
)

# Print the response
print(response.json())