# -*- coding: utf-8 -*
import dis


def swap1():
    x = 2
    y = 3
    x, y = y, x


def swap2():
    x = 2
    y = 3
    temp = x
    y = temp

dis.dis(swap1)

dis.dis(swap2)

'''
  6           0 LOAD_CONST               1 (2)
              3 STORE_FAST               0 (x)

  7           6 LOAD_CONST               2 (3)
              9 STORE_FAST               1 (y)

  8          12 LOAD_FAST                1 (y)
             15 LOAD_FAST                0 (x)
             18 ROT_TWO
             19 STORE_FAST               0 (x)
             22 STORE_FAST               1 (y)
             25 LOAD_CONST               0 (None)
             28 RETURN_VALUE
 12           0 LOAD_CONST               1 (2)
              3 STORE_FAST               0 (x)

 13           6 LOAD_CONST               2 (3)
              9 STORE_FAST               1 (y)

 14          12 LOAD_FAST                0 (x)
             15 STORE_FAST               2 (temp)

 15          18 LOAD_FAST                2 (temp)
             21 STORE_FAST               1 (y)
             24 LOAD_CONST               0 (None)
             27 RETURN_VALUE


'''