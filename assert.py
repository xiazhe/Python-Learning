# -*- coding: utf-8 -*
# 断言
# assert expression1 ["," expression2]
# https://docs.python.org/2.0/ref/assert.html

# demo
x = 1
y = 2
assert x == y, "not equals"

'''
>python assert.py
Traceback (most recent call last):
  File "assert.py", line 9, in <module>
    assert x == y, "not equals"
AssertionError: not equals
'''

# -O 禁用断言
# python -O assert.py
