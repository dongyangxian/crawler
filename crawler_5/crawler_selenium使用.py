import time
from selenium import webdriver

# 1. 实例化charomedriver对象
driver = webdriver.Chrome('/home/python/Desktop/driver/chromedriver')

# 2. 发送请求，打开浏览器
driver.get('https://www.baidu.com')

time.sleep(2)
# 3. 定位到搜索栏，输入关键字
driver.find_element_by_id('kw').send_keys('python')

time.sleep(2)
# 4. 定位搜索按钮，进行点击
driver.find_element_by_id('su').click()

print(driver.current_url)
print(driver.get_cookies())
with open('text.txt', 'w') as f:
    f.write(driver.page_source)

time.sleep(4)
driver.close()  # TODO 关闭当前标签页

time.sleep(4)
driver.quit()  # TODO 关闭所有标签页