# -*- coding: UTF-8 -*-
"""
静态方法和类方法
Python 核心编程(第二版) 第13章 13.8
"""


class TestStaticMethod:
    def foo():
        print 'calling static method foo()'

    foo = staticmethod(foo)
        

class TestClassMethod:
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__

    foo = classmethod(foo)
        

tsm = TestStaticMethod()
TestStaticMethod.foo()
# calling static method foo()

tsm.foo()
# calling static method foo()

tcm = TestClassMethod()

TestClassMethod.foo()
# calling class method foo()
# foo() is part of class: TestClassMethod

tcm.foo()
# calling class method foo()
# foo() is part of class: TestClassMethod

