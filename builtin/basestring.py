# -*- coding: UTF-8 -*-
"""
basestring()
This abstract type is the superclass for str and unicode. It cannot be called or instantiated, but it can be used to
test whether an object is an instance of str or unicode. isinstance(obj, basestring) is equivalent to
isinstance(obj, (str, unicode)).

New in version 2.3.

这个抽象类型是str和unicode的超类。 它不能被调用或者实例化，但是可以用来测试一个对象是否是str或者unicode的实例。
isinstance(obj, basestring)等同于isinstance(obj, (str, unicode))。


http://stackoverflow.com/questions/1979004/what-is-the-difference-between-isinstanceaaa-basestring-and-isinstanceaaa
plain strings    纯字符串
unicode strings


In Python versions prior to 3.0 there are two kinds of strings "plain strings" and "unicode strings".
Plain strings (str) cannot represent characters outside of the Latin alphabet (ignoring details of code pages
for simplicity).
Unicode strings (unicode) can represent characters from any alphabet including some fictional ones like Klingon.

So why have two kinds of strings, would it not be better to just have Unicode since that would cover all the cases?
Well it is better to have only Unicode but Python was created before Unicode was the preferred method for representing
strings. It takes time to transition the string type in a language with many users, in Python 3.0 it is finally
the case that all strings are Unicode.

The inheritance hierarchy of Python strings pre-3.0 is:

          object
             |
             |
         basestring
            / \
           /   \
         str  unicode

'basestring' introduced in Python 2.3 can be thought of as a step in the direction of string unification as it can be
used to check whether an object is an instance of str or unicode


a = 'aaaa'
print isinstance(a, basestring)
# true
print isinstance(a, str)
# true

"""


string1 = "I am a plain string"
string2 = u"I am a unicode string"

print isinstance(string1, str)

print isinstance(string2, str)

print isinstance(string1, unicode)

print isinstance(string2, unicode)

print isinstance(string1, basestring)

print isinstance(string2, basestring)

# True
# False
# False
# True
# True
# True

