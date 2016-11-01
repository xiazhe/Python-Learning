class P(object):
    def foo(self):
        print 'Hi, I am P-foo()'

    def bar(self):
        print 'P-bar()'


class C(P):
    def foo(self):
        print 'C-foo()'


p = P()
p.foo()

c = C()
c.foo()

# Hi, I am P-foo()
# C-foo()

c.bar()
# P-bar()

P.foo(c)
# Hi, I am P-foo()



