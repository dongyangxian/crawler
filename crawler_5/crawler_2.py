"""以下三个Queue是完全一模一样的"""
from queue import Queue
from multiprocessing.dummy import Queue
from multiprocessing.dummy import JoinableQueue

from multiprocessing import SimpleQueue  # TODO 只有三个简单的方法

"""以下两个为继承关系"""
from multiprocessing import Queue
from multiprocessing import JoinableQueue  # 在上一个的基础上多了join和task_done方法

""" 弱类型检查。参数必须为str，返回值必须为int。如果不是的话，只会标黄提示，不会报错 """
def func(a:str)->int:
    return 123