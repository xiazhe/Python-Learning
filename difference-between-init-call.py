# http://stackoverflow.com/questions/9663562/what-is-difference-between-init-and-call-in-python
"""
what is difference between __init__ and __call__ in python?


class test:
    def __init__(self):
        self.a = 10

    def __call__(self):
        b = 20

"""


# The first is used to initialise newly created object, and receives arguments used to do that:
class foo:
    def __init__(self, a, b, c):
        pass


f = foo(1, 2, 3)    # __init__


# The second implements function call operator.
class bar:
    def __call__(self, a, b, c):
        pass


b = bar()
b(1, 2, 3)


# http://stackoverflow.com/questions/3369640/when-is-using-call-a-good-idea


