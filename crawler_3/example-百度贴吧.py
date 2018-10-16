import requests
from lxml import etree
"""
思路：
    1. 构造url_list
    2. 遍历url，发送请求，获取响应
    3. 数据提取，处理
"""

class TiebaSpider():
    def __init__(self, name, page_num):
        """初始化数值"""
        self.name = name
        self.page_nums = page_num
        self.url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=9001&lm=&pn={}'
        self.base_url = 'https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',

        }

    def makeUrlList(self):
        """构造url_list，并返回"""
        return [self.url.format(self.name, i) for i in range(self.page_nums)]

    def getHtml(self, url):
        """发送请求，获取响应，并发挥响应内容"""
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.content)

    def parseImg(self, detail_url, img_list):
        """处理详情页中所有的图片链接和下一页内容，并返回"""
        # 发送一个帖子的url,获取响应
        detail_html = self.getHtml(detail_url)

        # 提取图片的链接
        img_list += detail_html.xpath('//img[@class="BDE_Image"]/@src')

        # 判断是否是最后一页
        next_href = detail_html.xpath('//a[text()="下一页"]/@href')
        if next_href != []:
            next_href = self.base_url + next_href[0]
            self.parseImg(next_href, img_list)

        with open('img.txt', 'w') as f:
            for img in img_list:
                f.write(img+'\n')

        # 返回图片链接列表
        return img_list

    def excuteItem(self, item):
        """保存或处理一条数据"""
        print(item)

    def run(self):
        """主程序逻辑"""
        # 1. 构造url_list
        url_list = self.makeUrlList()

        # 2. 发送请求，获取响应
        for url in url_list:
            resp = self.getHtml(url)

            # 3. 数据提取
            div_list = resp.xpath('//div[contains(@class, "i")]')

            # 3.1 先分组，获取每个帖子对应的详情页url和标题
            for div in div_list:
                item = {}
                item['detail_title'] = div.xpath('./a/text()')
                item['detail_url'] = self.base_url + div.xpath('./a/@href')[0]
                item['img_list'] = self.parseImg(item['detail_url'], [])

                # 3.2 保存处理一条数据
                self.excuteItem(item)

if __name__ == '__main__':
    sprider = TiebaSpider('lol', 3)
    sprider.run()
