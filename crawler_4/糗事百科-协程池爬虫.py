import gevent.monkey
gevent.monkey.patch_all()

import time
import requests
import datetime
from lxml import etree

from gevent.pool import Pool
from queue import Queue

"""
    核心：利用线程池中的线程异步，不断的去执行:处理一个url，直到处理完毕
    思路：
        1. 构造url_list，初始化数据，初始化出一个url队列，一个线程池，两个变量，一个布尔类型
            1.1 基本初始化的数据：url，headers
            1.2 线程池队列所需的数据变量：url_q（存放url的队列），pool（线程池），请求变量数，响应变量数，布尔数
        2. 使用线程池异步，执行一个总的处理一条url的callback函数
            2.1 _callback函数。用来判断是否url已经执行完成，是否要继续处理下一个url
            2.2 总的处理函数。从url队列中获取一条url，调用其他分支的函数来处理这条url
        3. 其他分支的函数，处理具体的业务逻辑
            3.1 获取响应内容函数。根据传入的url，发送请求，获取响应，返回结果
            3.2 提取响应数据函数。根据传入的响应数据内容，提取出所需要的数据，加入列表中，并进行返回
            3.3 保存数据函数。保存传入的数据列表内容
"""

class QiushiSpider():
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        self.url_q = Queue()
        self.pool = Pool(5)
        self.total_response_nums = 0
        self.total_request_nums = 0
        self.is_running = True

    def makeUrlList(self):
        """构造所有的url放入队列"""
        for i in range(1, 14):
            self.url_q.put(self.url.format(i))
            self.total_request_nums += 1  # 请求数 + 1 (url数 + 1)

    def getHtml(self, url):
        """对一个url发送请求获取响应并返回"""
        resp = requests.get(url, headers=self.headers)
        return resp.text

    def parseItem(self, html_str):
        """提取一个响应中的数据,并返回多条数据构成的list"""
        html = etree.HTML(html_str)
        # 先分组,再提取
        div_list = html.xpath('//div[@id="content-left"]/div')
        result_list = [] # 构造最终返回的结果列表
        for div in div_list:
            item = {}
            item['name'] = div.xpath('.//h2/text()')[0].strip() # 用户昵称
            item['text'] = div.xpath('.//div[@class="content"]/span/text()') # 主要内容
            # print(item)
            result_list.append(item)
        # print(result_list)
        return result_list

    def saveResultList(self, result_list):
        """保存一个响应中的多条数据组成的列表"""
        # print(result_list)
        for item in result_list:
            print(item)

    def excute_requests_item_save(self):
        """从队列中拿出一个url,直到处理完成"""
        url = self.url_q.get()
        html_str = self.getHtml(url)
        result_list = self.parseItem(html_str)
        self.saveResultList(result_list)

        self.total_response_nums += 1 # 总响应数 + 1

    def _callback(self, xxx):  # callback指定的函数必须接收一个参数,哪怕用不上!
        print(xxx)
        # xxx就是excute_requests_item_save这个函数的返回值
        """apply_async异步执行的函数执行完毕后,会把该函数返回的结果作为参数传入callback指定的函数中"""
        if self.is_running:
            self.pool.apply_async(self.excute_requests_item_save, callback=self._callback)

    def run(self):
        """爬虫运行逻辑"""
        # 构造url队列
        self.makeUrlList()
        # 利用线程池中的线程异步的不断的去执行:处理一个url直到处理完毕
        for i in range(5):  # 这才是控制并发的规模!
            self.pool.apply_async(self.excute_requests_item_save, callback=self._callback)

        while 1:
            time.sleep(1)  # 一定也要睡一会儿!不然太快导致醒不过来!
            # 程序退出的逻辑: 总响应数 == url总数 --> 程序退出
            if self.total_response_nums >= self.total_request_nums:
                print('=')
                print(self.total_request_nums)
                print(self.total_response_nums)
                print(self.url_q.qsize())
                print('=')
                self.is_running = False
                break

        print('程序结束了!')
        # self.pool.close()

if __name__ == '__main__':

    start_time = datetime.datetime.now()
    spider = QiushiSpider()
    spider.run()
    end_time = datetime.datetime.now()
    print(end_time-start_time)