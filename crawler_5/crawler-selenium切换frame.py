import time
from selenium import webdriver

"""
    如果网页中出现了frame或者iframe嵌套，
        就必须先定位到frame或iframe，然后切换进去，
        再进行其他的操作
"""

driver = webdriver.Chrome(executable_path='/home/python/Desktop/driver/chromedriver')
driver.get('https://mail.qq.com/cgi-bin/loginpage')

# 定位frame标签
frame_element = driver.find_element_by_id('login_frame')
# 切换到frmae中
driver.switch_to.frame(frame_element)
time.sleep(2)

# 进行其他操作
driver.find_element_by_id('u').send_keys('xxxxxxxxxxx')
time.sleep(2)
driver.find_element_by_id('p').send_keys('xxxxxxxxxxx')
time.sleep(2)
driver.find_element_by_id('login_button').click()

# 从frame切回默认的标签页中
driver.switch_to.window(driver.window_handles[0])
ret = driver.find_element_by_class_name('login_pictures_title').text
print(ret)


driver.quit()

