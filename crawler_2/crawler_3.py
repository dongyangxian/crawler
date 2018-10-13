import requests

"""requests：timeout，超时重传参数使用"""

url = 'http://www.itcast.cn'

# timeout=3表示最大等待3秒,如果没有获取响应就抛出异常
resp = requests.get(url, timeout=0.005)

print(resp.content.decode())