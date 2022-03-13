# encoding=utf8
"""
editor:lenovo
date:2022year03month10day
"""


# 实现选择排序select_sort

# 1.简单版本的选择排序的实现
# 长度为n的列表,遍历n次,每次选出列表中最小的元素,添加到一个新的列表里
def select_sort(lis):
    lis_new = []
    for i in range(len(lis)):
        val_min = min(lis)
        #     使用内置的min()取最小元素的函数 #def min(*args, key=None): # known special case of min
        # min(iterable, *[, default=obj, key=func]) -> value  #传参,传入可迭代对象,列表是可迭代对象
        # min(arg1, arg2, *args, *[, key=func]) -> value
        lis_new.append(val_min)  # 使用list.append()函数,将元素添加到列表中
        lis.remove(val_min)  # 使用list.remove(值)函数,将某值的元素从列表中删除<->list.pop(索引)函数,将某索引的元素从列表中删除
    return lis_new


lis = [3, 2, 4, 1, 5, 6, 8, 7, 9]
print(select_sort(lis))
