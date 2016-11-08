# -*- coding: UTF-8 -*-
# TestClassMethod.foo()

# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
# Python @classmethod and @staticmethod for beginner?
"""
Could someone explain to me the meaning of @classmethod and @staticmethod in python? I need to know the difference and the meaning.

As far as I understand, @classmethod tells a class that it's a method which should be inherited into subclasses, or... something. 
However, what's the point of that? Why not just define the class method without adding @classmethod or @staticmethod or any @ definitions?

tl;dr: when should I use them, why should I use them, and how should I use them?

I'm pretty advanced with C++, so using more advanced programming concepts shouldn't be a problem. Feel free giving me a corresponding 
C++ example if possible.

explain 解释
beginner 初学者


And for you as C++ developer: @classmethod is similar to a static method in C++ and a @staticmethod is similar to a function (like 
you'd declare it outside the class) – Mene Aug 29 '12 at 13:45

similar to 类似


Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.

Let's look at all that was said in real examples.

Boilerplate

Let's assume an example of a class, dealing with date information (this is what will be our boilerplate to cook on):

class Date(object):

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
This class obviously could be used to store information about certain dates (without timezone information; let's assume all dates are presented in UTC).

Here we have __init__, a typical initializer of Python class instances, which receives arguments as a typical instancemethod, having the first non-optional argument (self) that holds reference to a newly created instance.

Class Method

We have some tasks that can be nicely done using classmethods.

Let's assume that we want to create a lot of Date class instances having date information coming from outer source encoded as a string of next format ('dd-mm-yyyy'). We have to do that in different places of our source code in project.

So what we must do here is:

Parse a string to receive day, month and year as three integer variables or a 3-item tuple consisting of that variable.
Instantiate Date by passing those values to initialization call.
This will look like:

day, month, year = map(int, string_date.split('-'))
date1 = Date(day, month, year)
For this purpose, C++ has such feature as overloading, but Python lacks that feature- so here's when  classmethod applies. Lets create another "constructor".

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

date2 = Date.from_string('11-09-2012')
Let's look more carefully at the above implementation, and review what advantages we have here:

We've implemented date string parsing in one place and it's reusable now.
Encapsulation works fine here (if you think that you could implement string parsing as a single function elsewhere, this solution fits OOP paradigm far better).
cls is an object that holds class itself, not an instance of the class. It's pretty cool because if we inherit our Date class, all children will have from_string defined also.
Static method

What about staticmethod? It's pretty similar to classmethod but doesn't take any obligatory parameters (like a class method or instance method does).

Let's look at the next use case.

We have a date string that we want to validate somehow. This task is also logically bound to Date class we've used so far, but still doesn't require instantiation of it.

Here is where staticmethod can be useful. Let's look at the next piece of code:

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    # usage:
    is_date = Date.is_date_valid('11-09-2012')
So, as we can see from usage of staticmethod, we don't have any access to what the class is- it's basically just a function, called syntactically like a method, but without access to the object and it's internals (fields and another methods), while classmethod does.

Though 虽然
quite similar 非常相似
slight difference 轻微差异
usage for 用法
assume 假设
dealing with 处理
boilerplate 样板
certain 确定/某些
presented 呈现


"""

class Date(object):

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print is_date  # True