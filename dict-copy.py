# -*- coding: UTF-8 -*-

import copy


a = {
    1: {
        1: 2,
        3: 4
    }
}

b = a

# b[1][1] = 'abc'
# print a[1][1]  # a 被改变了


# deep copy
c = copy.deepcopy(a)
a[2] = copy.deepcopy(a[1])

print c
print a

# {1: {1: 2, 3: 4}}
# {1: {1: 2, 3: 4}, 2: {1: 2, 3: 4}}

