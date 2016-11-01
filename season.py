# -*- coding: utf-8 -*
# 实现枚举


# 类
class Seasons:
    Spring, Summer, Autumn, Winter = range(4)

print Seasons.Spring


def enum(*posarg, **keysarg):
    return type("Enum", (object,), dict(zip(posarg, xrange(len(posarg))), **keysarg))

Seasons = enum("Spring", "Summer", "Autumn", Winter =1)
print Seasons.Spring