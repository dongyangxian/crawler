import requests
import re
"""
爬虫中为什么使用cookie:
    为了能够通过爬虫获取到登录后的页面，或者是解决通过cookie的反扒，需要使用request来处理cookie相关的请求

使用requests处理cookie有三种方法：
    1. cookie字符串放在headers中
    2. 把cookie字典放传给请求方法的cookies参数接收
    3. 使用requests提供的session模块
"""

# TODO 使用requests提供的session模块

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

session = requests.session()
session.headers = headers  # 因为接下来的几个请求都会用到headers，所以直接可以写成一句

# 1. 获取登录前的token
login_page_url = 'https://github.com/login'

# 1.1 获取请求内容
resp = session.get(login_page_url)  # <input type="hidden" name="authenticity_token" value="" />
# 1.2 匹配token
authenticity_token = re.search('<input type="hidden" name="authenticity_token" value="(.*?)" />', resp.text).group(1)

# 2. 进行登录
login_url = 'https://github.com/session'
data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': '**********@qq.com',
    'password': '********',
}

session.post(login_url, data=data)

# 3. 登录验证，看是否成功
check_url = 'https://github.com/dongyangxian'
resp = session.get(check_url)
print(resp.text)
