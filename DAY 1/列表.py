#!/usr/bin/python3  # 指定解释器路径

list = ['Google', 'Runoob', 1997, 2000]  # 定义一个包含字符串和整数的列表

print ("第三个元素为 : ", list[2])  # 输出列表的第三个元素（索引从0开始）
list[2] = 2001  # 修改列表中索引为2的元素的值
print ("更新后的第三个元素为 : ", list[2])  # 输出修改后的第三个元素

list1 = ['Google', 'Runoob', 'Taobao']  # 定义一个只包含字符串的列表
list1.append('Baidu')  # 使用append方法在列表末尾添加一个新元素
print ("更新后的列表 : ", list1)  # 输出添加新元素后的列表

#删除列表中的元素
list = ['google','runoob','taobao','baidu']
print("原始列表 ：", list)
del list[2]
print("删除第三个元素 ：", list)

print([1,2,3] + [4,5,6])

#引入operator模块
import operator

a = [1,2]
b = [3,4]
c = [3,4]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))