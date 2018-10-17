import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/python/Desktop/driver/chromedriver')
driver.get("https://www.baidu.com/")

time.sleep(2)
# 定位搜索输入，并点击
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()

time.sleep(2)
# 通过执行内js，来新开一个标签页
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)

time.sleep(2)
# 获取当前所有的窗口
windows = driver.window_handles
print(windows)

time.sleep(2)
# 根据窗口进行切换
print(len(windows))  # 当前窗口的标签栏个数

# 切换
# print(driver.current_url)
driver.switch_to.window(windows[0])
# print(driver.current_url)

time.sleep(2)
driver.switch_to.window(windows[1])
# print(driver.current_url)

time.sleep(2)
driver.quit()
