# pep8 --show-source --show-pep8 variable-exchange.py

x = 1
y = 2

x, y = y, x

print "x = %d, y = %d" % (x, y)
