from selenium import webdriver


"""
1. 首先要安装: pip install selenium
2. 下载安装PhantomJS：http://phantomjs.org/download.html
    解压并创建软连接：
    tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/
    sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

3. 下载安装Chromedriver：https://npm.taobao.org/mirrors/chromedriver
    必须与浏览器版本相对应
    直接将解压后的文件放到，新建的driver目录中即可
"""
# 指定driver的绝对路径
# driver = webdriver.Chrome('/home/python/Desktop/driver/chromedriver')
driver = webdriver.PhantomJS('/home/python/Desktop/driver/phantomjs')
# 向一个url发起请求
driver.get('http://www.itcast.cn/')

# 把网页保存为图片
driver.save_screenshot("itcast.png")

# 退出模拟浏览器
driver.quit()