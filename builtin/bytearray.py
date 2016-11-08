# -*- coding: UTF-8 -*-
"""
http://python.usyiyi.cn/documents/python_278/library/functions.html#bytearray
https://docs.python.org/2.7/library/functions.html#bytearray
https://www.dotnetperls.com/bytes-python
http://stackoverflow.com/questions/9099145/where-are-python-bytearrays-used
http://stackoverflow.com/questions/4490901/how-to-convert-string-to-byte-arrays
http://stackoverflow.com/questions/7380460/byte-array-in-python

bytearray([source[, encoding[, errors]]])
返回一个新的字节数组。 bytearray类型是一个可变的整数序列，整数范围为0 <= x < 256（即字节）。
它有可变序列的大多数方法，参见Mutable Sequence Types，同时它也有str类型的大多数方法，参见String Methods。

source参数可以以不同的方式来初始化数组，它是可选的：

如果是string，必须指明encoding（以及可选的errors）参数；bytearray()使用str.encode()将字符串转化为字节数组。
如果是integer，生成相应大小的数组，元素初始化为空字节。
如果是遵循buffer接口的对象，对象的只读buffer被用来初始化字节数组。
如果是iterable，它的元素必须是整数，其取值范围为0 <= x < 256，用以初始化字节数组。
如果没有参数，它创建一个大小为0的数组。
.

Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.
It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that
 the str type has, see String Methods.

The optional source parameter can be used to initialize the array in a few different ways:

If it is unicode, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the
unicode to bytes using unicode.encode().
If it is an integer, the array will have that size and will be initialized with null bytes.
If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the
bytes array.
If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial
contents of the array.
Without an argument, an array of size 0 is created.
"""

# Convert string to byte arrays
print list(bytearray("hello"))
# [104, 101, 108, 108, 111]

"""
>>> bytearray()
bytearray(b'')
>>> bytearray(5)
bytearray(b'\x00\x00\x00\x00\x00')
>>> bytearray('abc')
bytearray(b'abc')
>>> bytearray(1.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object is not iterable
>>>

"""

keys = bytearray([0x13, 0x00, 0x00, 0x00, 0x08, 0x00])
# print key

print keys[0]
# 19

keys[1] = 0xff
# print key

for key in keys:
    print key

# 19
# 255
# 0
# 0
# 8
# 0


