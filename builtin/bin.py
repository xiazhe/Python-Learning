# -*- coding: UTF-8 -*-
# 将一个整数转化成一个二进制字符串。结果是一个合法的Python表达式。如果x不是一个Python int对象，它必须定义一个返回整数的__index__()方法。

print bin(1)
# 0b1

"""
>>> bin(2)
'0b10'
>>> x = 'abc'
>>> bin(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an index
>>>


"""

