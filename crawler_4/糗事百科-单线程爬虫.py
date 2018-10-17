import requests
import datetime
from lxml import etree

"""
思路：
    1. 构造url_lsit, 进行遍历，对每一条url发送请求，获取响应
    2. 对响应数据进行数据提取。
        2.1 使用lxml，对响应内容HTML化
        2.2 先分组，再提取：先将数据提取成一个整体的列表，再对列表逐个遍历，提取
        2.3 返回处理后的数据
    3. 对提取的数据进行保存。
"""
class QiuShiSpider:
    def __init__(self):
        """初始化数值"""
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }
        self.num = 0  # 统计数据的总数

    def makeUrlList(self):
        """构造url_list，并返回"""
        return [self.url.format(i) for i in range(1, 14)]

    def getHtml(self, url):
        """对一个url发送请求，获取响应，并返回"""
        resp = requests.get(url, headers=self.headers)
        return resp.text

    def parseItem(self, html_str):
        """对每一条数据的内容，进行数据提取"""
        # 1. 对html数据，先转化为Element对象
        html = etree.HTML(html_str)
        result_list = []  # 构造最终返回的结果列表

        # TODO 先分组，再提取
        # 2. 对转化后的Element对象，进行数据提取
        div_list = html.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            item = {}
            item['name'] = div.xpath('.//h2/text()')[0].strip()  # 用户昵称
            item['text'] = div.xpath('.//div[@class="content"]/span/text()')  # 主要内容
            result_list.append(item)

        return result_list

    def saveResultList(self, result_list):
        """数据保存"""
        for item in result_list:
            self.num += 1
            print(item)
            print("一共有：%d条数据" % self.num)
    def run(self):
        """主程序逻辑"""
        # 1. 构造url_list
        url_list = self.makeUrlList()

        # 2. 遍历url_list，对每一条数据进行内容的爬取，处理
        for url in url_list:
            # 2.1 发送请求，获取响应
            html = self.getHtml(url)

            # 2.2 数据提取
            result_list = self.parseItem(html)

            # 2.3 数据保存
            self.saveResultList(result_list)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    sprider = QiuShiSpider()
    sprider.run()
    end_time = datetime.datetime.now()
    print(end_time-start_time)