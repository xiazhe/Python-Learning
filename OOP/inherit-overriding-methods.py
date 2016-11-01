class P(object):
    def foo(self):
        print 'Hi, I am P-foo()'

    @classmethod
    def bar(self):
        print 'P-bar()'


class C(P):
    def foo(self):
        print 'C-foo()'


class D(P):
    def foo(self):
        P.foo(self)
        # super(D, self).foo()
        print 'child-foo()'


#
# p = P()
# p.foo()

# c = C()
# c.foo()

# Hi, I am P-foo()
# C-foo()

# c.bar()
# P-bar()

# P.foo(c)
# Hi, I am P-foo()

# d = D()
# d.foo()

# Hi, I am P-foo()
# child-foo()





