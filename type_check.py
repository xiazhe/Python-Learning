# -*- coding: utf-8 -*
# 编写高质量代码–改善python程序的建议
# 建议十一：不推荐使用type来进行类型检查
import types


class UserInt(int):                            # int为UserInt 的基类
    def __init__(self, val=0):
        self._val = int(val)

    # 实现整数的加法
    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val + val._val)

        return self._val + val

    def __iadd__(self, val):
        # UserInt 不支持+=操作
        raise NotImplementedError("not support operation")

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return 'Integer(%s)' % self._val


n = UserInt()
print n

m = UserInt(2)
print m

print n+m
print type(n) is types.IntType

'''
0
2
2
False
'''
# 基于内建类型扩展的用户自定义类型，type函数并不能准确的返回结果。
# 如果类型有对应的工厂函数，可以使用工厂函数对类型做相应转换，如list(listing)、str(name)等。
# 否则可以使用isinstance()函数来检测
# isinstance(object, classinfo)

print isinstance(2, float)

print isinstance('a', (str, unicode))

print isinstance((2, 3), (str, list, tuple))

print isinstance(n, int)


