import time
from selenium import webdriver
import random

driver = webdriver.Chrome(executable_path='/home/python/Desktop/driver/chromedriver')
driver.get("http://www.itcast.cn/")
time.sleep(1)
total = 0

for i in range(10):
    time.sleep(1)
    num = random.randint(100, 1000)  # 每次随机移动的距离

    js = 'window.scrollTo(%d, %d)' % (total, total+num)
    driver.execute_script(js)  # 执行js的方法
    total += num
    print("移动距离：%d,距顶部：%d" % (num, total))

time.sleep(5)
driver.quit()