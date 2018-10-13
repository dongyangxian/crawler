import requests

"""requests模块中cookie字典和cookieJar对象相互转换"""

url = 'https://www.baidu.com/'

resp = requests.get(url)

# 打印一个cookieJar对象:响应和请求的cookies
print(resp.cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(resp.request._cookies)  # <RequestsCookieJar[]>

# cookieJar-->cookies_dict
cookie_dict = requests.utils.dict_from_cookiejar(resp.cookies)
print(cookie_dict)

# cookies_dict-->cookieJar
cookie_Jar = requests.utils.cookiejar_from_dict(cookie_dict)
print(cookie_Jar)