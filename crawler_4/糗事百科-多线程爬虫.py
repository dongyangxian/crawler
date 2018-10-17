import requests
import datetime
from lxml import etree
from threading import Thread
from queue import Queue

"""
思路：
    1. 构造url_lsit
    2. 构造一个线程列表，分别加入发送请求/提取数据/保存数据
        2.1 发送请求线程
            2.1.1 不断取出url，发送请求，并放入响应队列;
            2.1.2 构造url队列的计数减1
        2.2 提取数据线程：不断取出响应，提取数据，并把数据列表放入数据队列
            2.2.1 使用lxml，对响应内容HTML化
            2.2.2 先分组，再提取：先将数据提取成一个整体的列表，再对列表逐个遍历，提取
            2.2.3 返回处理后的数据
            2.2.4 发送请求的队列计数减1
        2.3 保存数据线程：不断取出响应中的多条数据组成的列表，分别处理每条数据
            2.3.1 从此线程队列中取出列表数据
            2.3.2 进行遍历输出
            2.3.3 提取数据的队列计数减1
    3. 设置线程守护。只要主线程结束，子线程无条件结束
    4. 设置主线程阻塞，当所有的线程队列计数为0,才停止阻塞
"""
class QiuShiSpider:
    def __init__(self):
        """初始化数值"""
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }
        self.num = 0  # 统计数据的总数
        self.url_q = Queue()  # url队列
        self.html_q = Queue()  # 响应的文本内容队列
        self.item_q = Queue()  # 数据队列

    def makeUrlList(self):
        """构造url并把所有url放入url队列中"""
        for i in range(1, 14):
            self.url_q.put(self.url.format(i))  # 计数+1

    def getHtml(self):
        """不断的取出url发送请求获取响应并放入响应队列"""
        while True:
            url = self.url_q.get()
            resp = requests.get(url, headers=self.headers)
            self.html_q.put(resp.text)
            self.url_q.task_done()  # 计数-1

    def parseItem(self):
        """不断取出响应,提取数据,并把数据列表放入数据队列"""
        while True:
            html_str = self.html_q.get()
            html = etree.HTML(html_str)
            # 先分组,再提取
            div_list = html.xpath('//div[@id="content-left"]/div')
            result_list = []  # 构造最终返回的结果列表
            for div in div_list:
                item = {}
                item['name'] = div.xpath('.//h2/text()')[0].strip() # 用户昵称
                item['text'] = div.xpath('.//div[@class="content"]/span/text()') # 主要内容
                result_list.append(item)
            self.item_q.put(result_list)
            self.html_q.task_done()  # 计数-1

    def saveResultList(self):
         """不断的取出一个响应中的多条数据组成的列表,分别处理每条数据"""
         while True:
            result_list = self.item_q.get()
            for item in result_list:
                print(item)
            self.item_q.task_done()  # 计数-1

    def run(self):
        """主程序逻辑"""
        # 1. 构造url_list
        self.makeUrlList()

        # 2. 构造一个线程列表!
        t_list = []

        # 2.1 发送请求获取响应线程
        for i in range(1):
            t_parse = Thread(target=self.getHtml)
            t_list.append(t_parse)

        # 2.2 提取数据线程
        for i in range(1):
            t_content = Thread(target=self.parseItem)
            t_list.append(t_content)

        # 2.3 保存或处理数据线程
        for i in range(1):
            t_save = Thread(target=self.saveResultList)
            t_list.append(t_save)

        # 3. 设置线程守护
        for t in t_list:
            t.setDaemon(True)  # 设置每一个子线程为守护线程:主进程结束,子线程跟着结束
            t.start()

        # 4. 让主线程阻塞
        for q in [self.url_q, self.html_q, self.item_q]:
            q.join()  # 让主线程阻塞在这,直到所有q队列的计数都为0,才停止阻塞

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    sprider = QiuShiSpider()
    sprider.run()
    end_time = datetime.datetime.now()
    print(end_time-start_time)