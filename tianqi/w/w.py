import requests

h = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
url = 'https://www.tianqi.com/wenzhou/'
html = requests.get(url,headers=h)
print(html.text)
