# -*- coding: UTF-8 -*-
"""
将一个值转化成布尔值，使用标准的真值测试例程。如果x为假或者没有参数，它返回False；
否则它返回True。bool也是一个类，它是int的子类。bool不能被继承。它唯一的实例就是False和True。

Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
If x is false or omitted, this returns False; otherwise it returns True. bool is also a class, which is a subclass of
int. Class bool cannot be subclassed further. Its only instances are False and True.
"""

print bool()
# False

"""
>>> bool(1)
True
>>> bool(2)
True
>>> bool(02)
True
>>> bool(0)
False
>>> bool(1==1)
True
>>> bool(1!=1)
False

"""
