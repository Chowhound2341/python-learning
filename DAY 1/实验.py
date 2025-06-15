# 定义一个包含多种类型元素的列表
my_list = ['abcd', 786, 2.23, 'runoob', 70.2]
# 定义一个较小的列表
tiny_list = [123, 'runoob']

# 打印整个列表
print(my_list)
# 打印列表的第一个元素
print(my_list[0])
# 打印列表的第二到第三个元素（不包含第四个元素）
print(my_list[1:3])
# 打印列表从第三个元素开始到末尾
print(my_list[2:])
# 打印tiny_list列表两次
print(tiny_list * 2)
# 打印两个列表拼接在一起的结果
print(my_list + tiny_list)