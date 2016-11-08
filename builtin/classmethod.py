# -*- coding: UTF-8 -*-
"""
classmethod(function)
将function包装成类方法。

类方法接受类作为隐式的第一个参数，就像实例方法接受实例作为隐式的第一个参数一样。声明一个类方法，使用这样的惯例：

class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
@classmethod是函数decorator（装饰器）参见Function definitions中的函数定义。

它即可以通过类来调用（如C.f()），也可以通过实例来调用（如C().f()）。除了实例的类，实例本身被忽略。如果在子类上调用类方法，子类对象被传递为隐式的第一个参数。

类方法不同于C++或Java中的静态方法。如果你希望静态方法，参见这节的staticmethod()。

需要类方法更多的信息，参见The standard type hierarchy中标准类型层次部分的文档。
"""


# 函数修饰符
class C(object):
    @classmethod
    def f(cls, arg1, arg2):
    	pass
       

# 内建函数
class TestClassMethod:
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

    foo = classmethod(foo)



class TestClassMethod2:
	_value = 'abc'

	@classmethod
	def foo(cls):
		print cls._value


TestClassMethod2.foo()
# abc

# Why/When use classmethod
