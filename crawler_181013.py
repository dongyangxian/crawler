import requests
import re

def html_deal(html_url_list):
    """html处理"""
    with open('files/html.txt', 'w') as f:
        for html_url in html_url_list:
            # 写入html文件路径
            f.write(html_url)
            f.write('\n')

            # 发送请求，获取内容，并继续执行main()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Cookie': 'UM_distinctid=1663a91df220-0f5b619c6ecd7-9393265-144000-1663a91df2310d; bdshare_firstime=1538580940053; safedog-flow-item=; CNZZDATA30056528=cnzz_eid%3D629189995-1538579398-http%253A%252F%252Fwww.meizitu.com%252F%26ntime%3D1539427850',
                'If-None-Match': 'a0a37f5ddf24d41:11c6',
            }
            resp = requests.get(html_url, headers=headers, verify=False)
            main(resp.content.decode())

def image_deal(image_url_list):
    """图片处理"""
    for image_url in image_url_list:
        with open('images/'+image_url.split('/')[image_url.split('/').__len__()-1], 'wb') as f:
            # 写入图片路径
            response1 = requests.get(image_url)
            f.write(response1.content)

def main(data):
    """页面内容处理"""
    # 提取网页中的图片的url
    image_url_list = re.findall(r'src="(.*?\.[a-z]{3})"', data)
    html_url_list = re.findall(r'href="(.*?\.[a-z]{4})"', data)

    image_deal(image_url_list)
    html_deal(html_url_list)

if __name__ == '__main__':

    # 目标url
    url = 'http://www.meizitu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie': 'UM_distinctid=1663a91df220-0f5b619c6ecd7-9393265-144000-1663a91df2310d; bdshare_firstime=1538580940053; safedog-flow-item=; CNZZDATA30056528=cnzz_eid%3D629189995-1538579398-http%253A%252F%252Fwww.meizitu.com%252F%26ntime%3D1539427850',
        'If-None-Match': 'a0a37f5ddf24d41:11c6',
    }

    # 向目标url发送get请求
    response = requests.get(url, headers=headers, verify=False)

    # 打印响应内容
    data = response.text
    print(response.status_code)
    print(data)
    main(data)
