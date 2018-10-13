mydict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
        ],
    }
}

import json

# TODO python数据类型-->json字符串

# indent=2表示以2个空格来进行自动换行
# ensure_ascii=False表示不使用ascii编码
json_str = json.dumps(mydict, indent=2, ensure_ascii=False)
print(type(json_str))

# TODO json字符串-->python数据类型
json_dict = json.loads(json_str)
print(type(json_dict))

# TODO 把python类型写入类文件对象
with open('test.txt', 'w', encoding='utf8') as f:
    json.dump(json_dict, f, indent=2, ensure_ascii=False)

# TODO 实现类文件对象中的json字符串转化为python类型
with open('test.txt', 'r', encoding='utf8') as f:
    json_dict = json.load(f)
    print(type(json_dict))