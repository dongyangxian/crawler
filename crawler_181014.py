import re
import requests

class MeiZisprider():
    def __init__(self):
        """初始化数据"""
        self.url = 'http://www.meizitu.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Cookie': 'UM_distinctid=1663a91df220-0f5b619c6ecd7-9393265-144000-1663a91df2310d; bdshare_firstime=1538580940053; safedog-flow-item=; CNZZDATA30056528=cnzz_eid%3D629189995-1538579398-http%253A%252F%252Fwww.meizitu.com%252F%26ntime%3D1539427850',
            'If-None-Match': 'a0a37f5ddf24d41:11c6',
            # 'Host': 'www.meizitu.com',
            # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Upgrade-Insecure-Requests': '1',
        }
        self.proxies = {
              "http": "http://47.93.56.0:3128",
        }

        self.html_list = []

    # def dealHtml_list(self):
    #     """路径保存"""
    #     with open('files/html.txt', 'a') as f:
    #         for html_list in self.html_list:
    #             f.write(html_list+'\n')

    def _writePic(self, items):
        """图片处理"""
        for image_url in items:
            print(image_url)
            with open('images/' + image_url.split('/')[image_url.split('/').__len__() - 1], 'wb') as f:
                # 写入图片路径
                response1 = requests.get(image_url)
                f.write(response1.content)

    def _writeHtml(self, items):
        """html路径处理"""
        with open('files/html.txt', 'a') as f:
            for html_url in items:
                # 判断是否是移动的路径
                if re.search('http://m.meizitu.com/.*\.html', html_url):
                    continue

                # 判断是否是重复的路径
                if html_url not in self.html_list:
                    self.html_list.append(html_url)
                    print(html_url)

                    # 写入路径
                    f.write(html_url + '\n')

                    # 发送响应
                    self.url = html_url
                    self._juDge(self._sendReq())

    def _sendReq(self):
        """发送请求，获取响应"""
        # print(self.url)
        try:
            response = requests.get(self.url, headers=self.headers, verify=False, proxies=self.proxies)
        except:
            return None
        return response.text

    def _juDge(self, data):
        """页面响应内容判断，获取图片及html路径"""
        if data is None:
            return
        image_url_list = re.findall(r'src="(.*?\.[a-z]{3})"', data)
        html_url_list = re.findall(r'href="(.*?\.[a-z]{4})"', data)

        # self._writePic(image_url_list)
        self._writeHtml(html_url_list)

    def run(self):
        """运行主逻辑"""
        resp = self._sendReq()
        print(resp)
        self._juDge(resp)
        # self.dealHtml_list()

if __name__ == '__main__':
    sprider = MeiZisprider()
    sprider.run()
