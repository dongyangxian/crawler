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

for image_url in image_url_list:

    # 拼接完整的url
    if image_url[0] == '/':
        image_url = 'http:' + image_url
    # 拆分url
    image_url_split = image_url.split('/')

    # 保存图片
    with open('images/'+image_url_split[image_url_split.__len__()-1], 'wb') as f:
        # 写入url路径
        response1 = requests.get(image_url)
        f.write(response1.content)