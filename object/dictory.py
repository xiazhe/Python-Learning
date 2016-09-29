# -*- coding: UTF-8 -*-
# Python 学习手册(第四版) 第4章

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

# print D['food']

# D['quantity'] += 1

# print D['quantity']

rec = {
    'name': {
        'first': 'Bob',
        'last': 'Smith'
    },
    'job': ['dev', 'mgr'],
    'age': 40.5
}

# print rec['name']
# {'last': 'Smith', 'first': 'Bob'}

# print rec['name']['first'] + ' ' + rec['name']['last']
# Bob Smith
# Bob Smith

rec['job'].append('janitor')

# print rec
# {'age': 40.5, 'job': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith', 'first': 'Bob'}}

# destory
# rec = 0