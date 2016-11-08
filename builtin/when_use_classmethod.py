# -*- coding: UTF-8 -*-
# http://stackoverflow.com/questions/10586787/when-should-i-use-classmethod-and-when-def-methodself
"""
When should I use @classmethod and when def method(self)?

While integrating a Django app I have not used before, I found two different ways used to define functions in classes. \
The author seems to use them both very intentionally. The first one is one I myself use a lot:

class Dummy(object):

    def some_function(self,*args,**kwargs):
        do something here
        self is the class instance
The other one is one I do not use, mostly because I do not understand when to use it, and what for:

class Dummy(object):

    @classmethod
    def some_function(cls,*args,**kwargs):
        do something here
        cls refers to what?
In the Python docs the classmethod decorator is explained with this sentence:

A class method receives the class as implicit first argument, just like an instance method receives the instance.
So I guess cls refers to Dummy itself (the class, not the instance). I do not exactly understand why this exists, because \
I could always do this:

type(self).do_something_with_the_class
Is this just for the sake of clarity, or did I miss the most important part: spooky and fascinating things that couldn't be\
 done without it?



be passed as 作为
"""

class Dummy(object):

    @classmethod
    def some_function(cls,*args,**kwargs):        
        print cls

#both of these will have exactly the same effect
Dummy.some_function()
Dummy().some_function()
# <class '__main__.Dummy'>
# <class '__main__.Dummy'>