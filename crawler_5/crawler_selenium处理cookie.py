from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome('/home/python/Desktop/driver/chromedriver')

driver.get(url)

# 获取当前标签页的cookie数据
cookie_list = driver.get_cookies()
print(cookie_list)

# 转换成cookie_dict(使用字典推倒式)
cookie_dict = {cookie['name']: cookie['value'] for cookie in cookie_list}
print(cookie_dict)

"""删除一条cookie"""
driver.delete_cookie('BIDUPSID')
print(driver.get_cookies())

"""删除所有cookie"""
driver.delete_all_cookies()
print(driver.get_cookies())