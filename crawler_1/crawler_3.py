import requests
import json

url = 'https://fanyi.baidu.com/basetrans'

# 无论是什么qingqiui，都要加上头部，这样才能尽可能的伪装成非爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

params = {
    'query': '今天天气真好啊',
    'from': 'zh',
    'to': 'en',
}

resp = requests.post(url, data=params, headers=headers)

result_json = resp.content.decode()

# 转换返回后的json结果，进行提取
result = json.loads(result_json)['trans'][0]['dst']

print(result)