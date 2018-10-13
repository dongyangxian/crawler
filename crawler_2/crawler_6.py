import urllib.request

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

url = 'http://www.baidu.com'

# 1. 构造post请求的参数对象
data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

# 2. 对请求数据字典编码为bytes类型
data = urllib.parse.urlencode(data).encode('utf8')

# 3. 构造请求对象（如果有data参数，就是好发送post请求）
request = urllib.request.Request(url, headers=headers, data=data)

# 4. 发送请求，获取响应
resp = urllib.request.urlopen(request)

print(resp.read().decode())