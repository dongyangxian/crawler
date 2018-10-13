import requests
import json
import re
"""
豆瓣美剧数据爬取思路：
    1. 构造url_list
    2. 遍历url_list中的所有url，发送请求，获取响应
    3. 提取数据
    4. 数据处理
"""
class DouBanSpider():
    def __init__(self):
        """初始化数据"""
        # 爬取路径
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # 'Host': 'm.douban.com',
            'Referer': 'https://m.douban.com/tv/american'
        }

    def _makeUrlList(self):
        """构造url_list, 并返回"""
        url_list = []
        for i in range(0, 19, 18):
            url_list.append(self.url.format(i))
        return url_list

    def _getJson(self, url):
        """发送请求，获取响应"""
        resp = requests.get(url, headers=self.headers)
        return json.loads(resp.content.decode())

    def _writeTitle(self, data_title_dict):
        """将爬取到的title写入到文件中进行保存"""
        with open('move-title.txt', 'a', encoding='utf8') as f:
            for data_title in data_title_dict:
                f.write(data_title['title']+'\n')

    def _writeTitleByRe(self, data_title_dict):
        """re模块专门写入电视剧的名字， 写入后是原始字符串，需要进行转码"""
        title_unicode = re.findall('"title": "(.*?)",', json.dumps(data_title_dict))

        # 将unicode转为中文显示和中文写入文件
        with open('move-title-re.txt', 'a') as f:
            for title in title_unicode:
                title = title.encode('utf8').decode('unicode_escape')
                f.write(title+'\n')

    def run(self):
        """主运行逻辑"""
        # 1. 构造url_list
        url_list = self._makeUrlList()
        for url in url_list:
            # 2. 发送请求，获取响应
            resp = self._getJson(url)

            # 3. 数据提取
            data_title_dict = resp['subject_collection_items']
            self._writeTitle(data_title_dict)
            self._writeTitleByRe(data_title_dict)

if __name__ == '__main__':
    spider = DouBanSpider()
    spider.run()