import requests
from retrying import retry

"""retry异常重试的使用"""

headers = {}

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print(1)
    # 超时的时候会报错并重试
    resp = requests.get(url, headers=headers, timeout=0.005)

    # 状态码不是200,也会报错重试
    assert resp.status_code == 200
    return resp

def parse_url(url):
    try:
        resp = _parse_url(url)
    except:
        resp = None

    return resp

if __name__ == '__main__':
    url = 'http://www.itcast.cn'
    parse_url(url)

