import requests
import re

# 目标url
url = 'http://itheima.com/'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
data = response.text

# 提取网页中的图片的url
image_url_list = re.findall(r'src="(.*?\.[a-z]{3})"', data)

# 保存图片
with open('files/urls.txt', 'wb') as f:

    # 从url列表中取出所有的url
    for image_url in image_url_list:
        # 拼接完整的url
        if image_url[0] == '/':
            image_url = 'http://www.itcast.cn' + image_url

        elif image_url[0] == 'i':
            image_url = 'http://www.itcast.cn/' + image_url

        # 写入url路径
        f.write(image_url.encode())
        f.write('\n'.encode())