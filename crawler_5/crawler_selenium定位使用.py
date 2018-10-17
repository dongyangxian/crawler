from selenium import webdriver

"""
    定位常用方法：
        driver.find_element_by_id/class_name/xpath/tag_name/link_text/partial_link_text

        find_element_by_xx  : 只返回第一个可以继续提取的数据或属性的标签对象
        find_elements_by_xx : 返回所有符合条件的可以提取数据或属性的标签对象

    提取数据常用方法：
        resp = driver.find_element_by_id('xxx')
        resp[0].text  # 提取标签对象中的全部文本内容。包含后代节点的文本
        resp[0].get_attribute('属性')  # 提取标签对象中的属性值
"""

# 1. 实例化charomedriver对象
driver = webdriver.Chrome('/home/python/Desktop/driver/chromedriver')

# 2. 发送请求，打开浏览器
driver.get('https://www.douban.com/')

# <selenium.webdriver.remote.webelement.WebElement (session="7cf077a3e96da39f7900783abb3c7c04", element="0.2629439410379584-1")>
ret1 = driver.find_element_by_id("anony-nav")
print(ret1)

# [<selenium.webdriver.remote.webelement.WebElement (session="7cf077a3e96da39f7900783abb3c7c04", element="0.2629439410379584-2")>]
ret2 = driver.find_elements_by_xpath("//*[@id='anony-nav']/h1/a")
print(ret2)

# [<selenium.webdriver.remote.webelement.WebElement (session="7cf077a3e96da39f7900783abb3c7c04", element="0.2629439410379584-3")>]
ret3 = driver.find_elements_by_tag_name("h1")
print(ret3)

# [<selenium.webdriver.remote.webelement.WebElement (session="7cf077a3e96da39f7900783abb3c7c04", element="0.2629439410379584-4")>]
ret4 = driver.find_elements_by_link_text("下载豆瓣 App")
print(ret4)

# [<标签对象1>，<标签对象2>，<标签对象3>，...]
ret5 = driver.find_elements_by_partial_link_text("豆瓣")
print(ret5)

# 豆瓣
ret6 = driver.find_elements_by_xpath("//*[@id='anony-nav']/h1/a")
print(ret6[0].text)

# https://www.douban.com/
print(ret6[0].get_attribute('href'))

driver.close()
