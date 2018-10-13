import re
string_a = '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t\t<meta http-equiv="content-type" content="text/html;charset=utf-8">\n\t\t<meta content="always" name="referrer">\n        <meta name="theme-color" content="#2932e1">'

# TODO re.match从被匹配的字符串的第一个字符开始严格匹配,只返回一个结果.group(),or None
ret1 = re.match('xxxx.*>', string_a)
ret2 = re.match('<.*>', string_a).group()
ret3 = re.match('<(.*)>', string_a).group(1)
print(ret1)
print(ret2)
print(ret3)

# TODO re.search返回匹配到的第一个结果,or None
ret4 = re.search('<.*>', string_a).group()
ret5 = re.search('xxxx.*>', string_a)
print(ret4)
print(ret5)

# TODO re.findall返回所有匹配到的[结果,...], or []
ret6 = re.findall('xxx.*>', string_a)
ret7 = re.findall('<.*>', string_a)
print(ret6)
print(ret7)

# TODO re.sub将匹配到的结果进行替换,返回替换后的字符串
ret8 = re.sub('<meta', '<xxxx', string_a)
print(ret8)

# TODO re.compile作用:在被匹配字符串很长,获取匹配次数很多的情况下,能够提升re匹配的速度
p = re.compile('<.*>')  # 定义一个匹配规则对象(先编译了匹配规则,来达到提升速度的效果)
ret = p.findall(string_a)  # 用匹配规则对象进行re.func()
print(ret)


# 测试re.compile的速度
with open('./test_re.html', 'r') as f:
    string_b = f.read()

import datetime
start_time = datetime.datetime.now()
# ret = re.search('52f7fee86ed2e97b8735527a8b6a012', string_b).group()
p = re.compile('52f7fee86ed2e97b8735527a8b6a012')
ret = p.search(string_b).group()
print(ret)
end_time = datetime.datetime.now()
print(end_time-start_time)


"""原始字符串r'xxxx'表示在机器执行的时候还是xxxx,就是我们看到的样子"""
# ret = re.search('\n\t\t', string_a).group()
# print(ret)
#
# ret = re.search(r'\n\t\t', string_a).group()
# print(ret)
#
# ret = re.search(r'\\n\\t\\t', string_a)
# print(ret)

"""匹配中文"""
# import re
#
# title = '你好，hello，世界'
# pattern = re.compile(r'[\u4e00-\u9fa5]+')
# result = pattern.findall(title)
# print(result)

"""贪婪与非贪婪"""
import re

s = '123xxxxxx456'
print(re.sub('\d+', '我', s)) # 贪婪
print(re.sub('\d+?', '我', s)) # 贪婪