# -*- coding: utf-8 -*
# Python 核心编程
# __bases__类属性


class A(object):
    pass


class E(object):
    pass


class B(A):
    pass


class C(B):
    pass


class D(A, E):
    pass

# TypeError: Error when calling the metaclass bases
#     Cannot create a consistent method resolution
# order (MRO) for bases A, B
# http://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro

print A.__bases__
# (<type 'object'>,)

print C.__bases__
# (<class '__main__.B'>,)

print D.__bases__
# (<class '__main__.A'>, <class '__main__.E'>)

