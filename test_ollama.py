import requests

url = "http://localhost:11434/v1/generate"
payload = {
    "model": "smollm2:135m",
    "prompt": "Hello, test LLM",
    "stream": False
}

r = requests.post(url, json=payload)
print(r.status_code)
print(r.text)
