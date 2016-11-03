# -*- coding: UTF-8 -*-

# 字典是 Python 中的映射数据类型，工作原理类似 Perl 中的关联数组或者哈希表，由键-
# 值(key-value)对构成。几乎所有类型的 Python 对象都可以用作键，不过一般还是以数字或者
# 字符串最为常用。

aDict = {'host': 'earth'}
aDict['port'] = 80
aDict['child'] = {
    'name': 'tree'
}
# 获取键数组
print aDict.keys()
# 获取所有值
print aDict.values()

# 查看字段是否拥有键值a
# print aDict.has_key('a')   # has_key is deprecated, use in
print 'a' in aDict

# 返回整个字典列表
print aDict.items()
# [('host', 'earth'), ('port', 80), ('child', {'name': 'tree'})]

# 删除一个元素
del aDict['port']

# 遍历
for key in aDict:
    print key, aDict[key]

