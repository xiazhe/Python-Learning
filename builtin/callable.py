# -*- coding: UTF-8 -*-
"""
callable(object)
如果object参数可调用，返回True；否则返回False。如果返回真，对其调用仍有可能失败；但是如果返回假，对object的调用总是失败。
注意类是可调用的（对类调用返回一个新实例）；如果类实例有__call__()方法，则它们也是可调用的。
"""


class a(object):
    pass


print callable(a)

b = 1

print callable(b)
# False
