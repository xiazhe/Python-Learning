# -*- coding: utf-8 -*


class C(object):
    foo = 100

    def __init__(self):
        pass

    def instanceFun(self):
        print('instance function', self.foo)

    # @staticmethod                      # 静态方法
    # def f(arg1, arg2):
    #     pass

    @staticmethod
    def staticFunc():
        print('static method', C.foo)

    # @classmethod                       # 类方法
    # def f2(cls, arg1, arg2):
    #     pass

    @classmethod
    def classFunc(cls):
        print('class method', cls.__name__, cls.foo)

    # TypeError: func() takes no arguments (1 given)
    def func():
        print('Common Method')


# C.f()

# C().staticFunc()

# 区别是什么， 应用场景
# 类调用静态方法
C.func()

# 实例调用静态方法
C().staticFunc()

# 类调用类方法
C.classFunc()

# 实例调用类方法
C().classFunc()

# 类调用实例方法需要自己穿self 参数(C类本身)
# C.instanceFun()
# TypeError: unbound method instanceFun() must be called with C instance as first argument (got nothing instead)

C.instanceFun(C)

# 实例化实例 c
c = C()
c.classFunc()

c.instanceFun()

# 类/实例属性改变， 调用静态方法， 类方法， 实例方法
#
# C.foo = 200
c.foo = 200

C.staticFunc()

C.classFunc()

c.staticFunc()

c.classFunc()

c.instanceFun()


print(c.foo)


# static method 100
# static method 100
# class method C 100
# class method C 100
# class method C 100
# instance function 100
# 类属性改变 print C.foo改变
# static method 200
# class method C 200
# static method 200
# class method C 200

# 实例同名属性改变， 调用类／实例／静态方法实际取的是类的属性, 只有实例方法取的实例的属性，
# 因为self 取的实例对象。 其他取类对象，
# 静态方法根据实际情况判断，这里使用的类对象的属性。静态方法如何动态取类或实例对象？
# static method 100
# class method C 100
# static method 100
# class method C 100
# 200





# c.func() error
C.func()      # Python 3.5.2 允许运行  Common Method
# python 2.7 中 TypeError: unbound method func() must be called with C instance as first argument (got nothing instead)



