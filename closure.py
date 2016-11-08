# -*- coding: UTF-8 -*-
def counter(start_no=1):
    count = [start_no]

    def incr():
        count[0] += 1
        return count[0]

    return incr


count = counter(5)
print count()
# 6
