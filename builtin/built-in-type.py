# -*- coding: utf-8 -*
# 编写高质量代码：改善Python程序的91个建议
# 理解 built-in objects


# 古典类
class A:
    pass


class B(object):
    pass


class C(type):
    pass


# 继承自内建类型dict
class D(dict):
    pass


a = A()
b = B()
c = C(type)
d = D()

# A
# print "type<*>: {0}, *.__class__: {1}, *__bases__: {2}, isinstance(*, object): {3}, isinstance(*, type): {4}"\
#     .format(type(a), a.__class__, '()', isinstance(a, object), isinstance(a, type))

# a.__bases__
# AttributeError: A instance has no attribute '__bases__'

# type<*>: <type 'instance'>, *.__class__: __main__.A, *__bases__: (),\
# isinstance(*, object): True, isinstance(*, type): False

# B
# print "type<*>: {0}, *.__class__: {1}, *.__bases__: {2}, isinstance(*, object): {3}, isinstance(*, type): {4}"\
#     .format(type(b), b.__class__, '()', isinstance(b, object), isinstance(b, type))

# b.__bases__
# AttributeError: 'B' object has no attribute '__bases__'

# type<*>: <class '__main__.B'>, *.__class__: <class '__main__.B'>, *__bases__: (),\
# isinstance(*, object): True, isinstance(*, type): False

# C
# print "type<*>: {0}, *.__class__: {1}, *.__bases__: {2}, isinstance(*, object): {3}, isinstance(*, type): {4}"\
#     .format(type(c), c.__class__, c.__bases__, isinstance(c, object), isinstance(c, type))

# type<*>: <type 'type'>, *.__class__: <type 'type'>, *.__bases__: (<type 'object'>,),\
# isinstance(*, object): True, isinstance(*, type): True

# D
print "type<*>: {0}, *.__class__: {1}, *__bases__: {2}, isinstance(*, object): {3}, isinstance(*, type): {4}"\
    .format(type(d), d.__class__, '()', isinstance(d, object), isinstance(d, type))

# type<*>: <class '__main__.D'>, *.__class__: <class '__main__.D'>, *.__bases__: (),\
# isinstance(*, object): True, isinstance(*, type): False
