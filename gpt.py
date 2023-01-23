import requests
import os


def warn(text):
  print("\033[38;5;1m" + "\033[1m" + text + "\u001b[0m ") 

try:
  # Set your API key
  API_KEY = os.environ['OPENAI_API_KEY']
except:
  warn("OPENAI_API_KEY environment variable not set on this computer") 
  exit()


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
if not response.json()['error']:
  print(response.json()['choices'])
else:
  warn(response.json()['error']['message'])