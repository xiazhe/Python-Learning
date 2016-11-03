# -*- coding: UTF-8 -*-
"""
__getitem__():
如果类把某个属性定义为序列，可以使用__getitem__()输出序列属性中的某个元素.
假设水果店中销售多钟水果，可以通过__getitem__()方法获取水果店中的没种水果
"""


class FruitShop:
    def __getitem__(self, i):      # 获取水果店的水果
        return self.fruits[i]

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ["apple", "banana"]
    print shop[1]
    for item in shop:               # 输出水果店的水果
        print item,

# 输出为:
# banana
# apple banana
