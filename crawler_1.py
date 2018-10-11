import requests

# 目标url
url = 'https://www.zcool.com.cn/'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
with open('files/zcool.html', 'wb') as f:
    f.write(response.content)