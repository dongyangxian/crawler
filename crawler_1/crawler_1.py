import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

url = 'http://www.baidu.com'

resp = requests.get(url, headers)

print(resp.text)
print('--------')
print(resp.content.decode())