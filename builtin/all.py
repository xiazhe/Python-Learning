# -*- coding: UTF-8 -*-

# 如果iterable的所有元素为真（或者iterable为空）， 返回True。
a = 1
b = 1
print all([1 == 1, a == b, a == 1, b == 1, 1 == 2])
# False


# 等同于 / Equivalent to：
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

