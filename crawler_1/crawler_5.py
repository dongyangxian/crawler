import requests
"""
爬虫中为什么使用cookie:
    为了能够通过爬虫获取到登录后的页面，或者是解决通过cookie的反扒，需要使用request来处理cookie相关的请求

使用requests处理cookie有三种方法：
    1. cookie字符串放在headers中
    2. 把cookie字典放传给请求方法的cookies参数接收
    3. 使用requests提供的session模块
"""

# TODO cookie字符串放在headers中
url = 'https://github.com/dongyangxian'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': '_ga=GA1.2.655960664.1524368071; _octo=GH1.1.159220089.1524368071; user_session=tePQa3D0mT4IAHd3w-tyT_y2loLW8vrz1Zv5z2RiMJDjFeX3; __Host-user_session_same_site=tePQa3D0mT4IAHd3w-tyT_y2loLW8vrz1Zv5z2RiMJDjFeX3; logged_in=yes; dotcom_user=dongyangxian; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=dUU2bGhBZkNTMmsxbnByZ2VLLzlMeW9TQmsyN2F3WCt0U0MyYWxQT2hDOFZnc3pvamg2UWVGQTVIUjJuNGRTMXJINkw4ekFBL0dUMnVQcTdoaDJUejFqWUxQd3pwMWRnNWtBT3ExcHhlc1Rrb1A0cDdsZXg5aGtjcWdoNmczUC9oVXNFMXY3ZTd0L3dmbWtEbW0vd0NBPT0tLUlMV1Z1RktZNENqMVd0eEFnLzRENVE9PQ%3D%3D--9757ddd51f0a40219377c0b83cbea5694816cf54',
}

resp = requests.get(url, headers)
print(resp.content.decode())