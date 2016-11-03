# -*- coding: UTF-8 -*-
# 值 和 引用
# demo 1
# def f(a):
#     a = 99
#
# b = 88
# f(b)
# print b
# 88


# demo 2
def changer(a, b):
    a = 2
    b[0] = 'spam'

X = 1
L = [1, 2]
changer(X, L)

print X, L
# 1 ['spam', 2]



