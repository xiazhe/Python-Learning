# -*- coding: utf-8 -*
from timeit import Timer

time1 = Timer('temp = x; x = y; y = temp', 'x = 2; y = 3').timeit()

time2 = Timer('x, y = y, x', 'x = 2; y = 3').timeit()

print "It takes time to use intermediate values: %(time1)s, Unused: %(time2)s" \
      % {'time1': time1, 'time2': time2}

# It takes time to use intermediate values: 0.0387468547212, Unused: 0.0242510925705

