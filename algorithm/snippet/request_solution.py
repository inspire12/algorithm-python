import requests

resp = requests.get(
    "https://api.github.com/repos/pallets/flask",
    headers={"Accept": "application/vnd.github+json"},
    timeout=3,
)
data = resp.json()
print(data["stargazers_count"])