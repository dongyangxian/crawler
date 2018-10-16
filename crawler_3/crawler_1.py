from lxml import etree

""" 首先要安装 pip install lxml """

html_str = """<div> <ul>
<li class="item-1"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul> </div>"""  # 注意，此处缺少一个 </li> 闭合标签

# 1. 将字符串转化为Element对象
html = etree.HTML(html_str)  # TODO etree.HTML()会自动补全或修改html_str
print(html)

# TODO 爬虫提取数据的xpath_str要以etree.tostring()函数转换回来的结果为准!
html_trans_str = etree.tostring(html)  # 能够把html对象转换为bytes类型
print(html_trans_str)

# 2. 使用xpath进行数据提取
ret = html.xpath('//a/text()')  # 返回的是一个列表数据类型
ret_list = html.xpath('//li')  # 返回的列表对象，依旧可以继续进行xpath提取
for ret1 in ret_list:
    print(ret1.xpath('./a/@href'))