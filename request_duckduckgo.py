import requests

url = "http://duckduckgo.com/html"
payload = {'q':'python'}
r = requests.get(url, payload)
print r.text.encode('utf-8')
with open("requests_results.html", "w") as f:
    f.write(r.text.encode('utf-8'))