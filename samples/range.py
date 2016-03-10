__author__ = 'zhexia'


# print range(5)
#
# print range(1, 5)
#
# print range(0, 6, 2)

# xrange
#
# print xrange(5)
#
# print list(xrange(5))

pages = 20
page = 15


left_edge=2
left_current=2
right_current=5
right_edge=2

last = 0
for num in xrange(1, pages + 1):
    if num <= left_edge or (num > page - left_current - 1 and num < page + right_current) or num > pages - right_edge:
        if last + 1 != num:
            print None
        print num
        last = num


# 1
# 2
# 3
# 4
# 5
# 9
# 10
