import requests
import re

# 目标url
url = 'https://www.zcool.com.cn/'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
data = response.text

# 提取网页中的图片的url
image_url_list = re.findall(r'src="(.*?\.[a-z]{3})"', data)
print(image_url_list)
# 保存图片的url
with open('files/urls-zcool.txt', 'wb') as f:
    for image_url in image_url_list:
        f.write(image_url.encode())
        f.write('\n'.encode())