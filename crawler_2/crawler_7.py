book_dict = {
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

from jsonpath import jsonpath

"""jsonpath:用来解析多层嵌套的json数据"""

# 1. 安装：pip install jsonpath
# 2. 用法：jsonpath(要被提取的python数据类型, '提取的规则')

print(jsonpath(book_dict, '$..author'))  # 返回值为列表，如果取不到，返回False
print(jsonpath(book_dict, '$.store.bicycle.price'))

"""
$.store.book[*].author	store中的所有的book的作者
$..author	            所有的作者
$.store.*	            store下的所有的元素
$.store..price	        store中的所有的内容的价格
$..book[2]	            第三本书
$..book[(@.length-1)] | $..book[-1:]	最后一本书
$..book[0,1] | $..book[:2]	            前两本书
$..book[?(@.isbn)]	                    获取有isbn的所有数
$..book[?(@.price<10)]	                获取价格大于10的所有的书
$..*	                                获取所有的数据
"""
