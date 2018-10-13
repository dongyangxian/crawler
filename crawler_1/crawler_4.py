import requests

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

"""
    使用代理ip：
    1. 让服务器以为不是同一个客户端在请求
    2. 防止我们的真实地址被泄露，防止被追究
"""
proxy = {
    'http': 'https://219.150.189.212:9999'
}

resp = requests.get(url, headers=headers, proxies=proxy)

print(resp.content.decode())