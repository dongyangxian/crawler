import requests

"""requests：verify忽略安全认证"""

url = 'https://www.12306.cn/mormhweb/'

# 2. 隐藏所有请求以及响应的warning级别信息，一定要在发送请求之前设置
requests.packages.urllib3.disable_warnings()

resp = requests.get(url, verify=False)  # 1. verify=False 可以忽略ssl安全认证

print(resp.content.decode())