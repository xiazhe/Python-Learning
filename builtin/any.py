# -*- coding: UTF-8 -*-

# 如果iterable的任一元素为真，返回True。如果iterable为空，返回False。
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
a = 1
b = 1
print any([1 == 1, a == b, a == 1, b == 1, 1 == 2])
# True

# any all 区别 http://stackoverflow.com/questions/19389490/how-do-pythons-any-and-all-functions-work
