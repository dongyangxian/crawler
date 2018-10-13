import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

# 方式一：将查询字符串放在url中请求
# url = 'https://www.baidu.com/s?wd=python'
# resp = requests.get(url, headers=headers)
# print(resp.content.decode())

# 方式二：使用params参数
url = 'https://www.baidu.com'

params = {
    'wd': 'python',
}

resp = requests.get(url, headers=headers, params=params)

print(resp.content.decode())