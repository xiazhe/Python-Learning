# -*- coding: UTF-8 -*-
'''
__call__():
在类中实现__call__()方法，可以在对象创建时直接返回__call__()的内容.使用该方法可以模拟静态方法
'''

class Fruit:
    class Growth:        # 内部类
        def __call__(self):
            print "grow ..."

    grow = Growth()      # 调用Growth()，此时将类Growth作为函数返回,即为外部类Fruit定义方法grow(),grow()将执行__call__()内的代码
if __name__ == '__main__':
    fruit = Fruit()
    fruit.grow()         # 输出结果：grow ...
    Fruit.grow()         # 输出结果：grow ...