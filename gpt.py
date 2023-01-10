import requests

# Set your API key
API_KEY = "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"

# Set the model and prompt
MODEL = "text-davinci-003"
PROMPT = input("ask a question \n")

# Set the request parameters
params = {
  "model": MODEL,
  "prompt": PROMPT,
  "max_tokens": 100,
  "temperature": 0.5,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
}

# Set the request headers
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}

# Make the request
response = requests.post(
  "https://api.openai.com/v1/completions",
  json=params,
  headers=headers
)

# Print the response
print(response.json()['choices'][0]['text'])