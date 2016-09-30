# -*- coding: UTF-8 -*-


# __new__()在__init__()之前被调用，用于生成实例对象.
# 利用这个方法和类属性的特性可以实现设计模式中的单例模式.
# 单例模式是指创建唯一对象，单例模式设计的类只能实例化一个对象.



class Singleton(object):
    __instance = None                       # 定义实例
    name = 'Singleton'

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):         # 在__init__之前调用
        if Singleton.__instance is None:    # 生成唯一实例
            Singleton.__instance = object.__new__(cls, *args, **kwd)
        return Singleton.__instance

    def sayHi(self):
        print self.__instance
        print self.name

s1 = Singleton()
s2 = Singleton()

s1.name = 'multi'
s1.sayHi()
s2.sayHi()


