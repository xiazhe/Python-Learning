# -*- coding: UTF-8 -*-
'''
__getattr__()、__setattr__()和__getattribute__():
当读取对象的某个属性时，python会自动调用__getattr__()方法.
例如，fruit.color将转换为fruit.__getattr__(color).
当使用赋值语句对属性进行设置时，python会自动调用__setattr__()方法.
__getattribute__()的功能与__getattr__()类似，用于获取属性的值.
但是__getattribute__()能提供更好的控制，代码更健壮.
注意，python中并不存在__setattribute__()方法.
'''

class Fruit(object):
    def __init__(self, color = "red", price = 0):
        self.__color = color
        self.__price = price

    def __getattribute__(self, name):               # 获取属性的方法
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

if __name__ == "__main__":
    fruit = Fruit("blue", 10)
    print fruit.__dict__.get("_Fruit__color")       # 获取color属性
    fruit.__dict__["_Fruit__price"] = 5
    print fruit.__dict__.get("_Fruit__price")       # 获取price属性