"""
比较运算符和逻辑运算符
Version: 1.0
Author: Wei si qi
# Python 中的比较运算符用于比较两个值的大小关系，逻辑运算符用于连接多个条件表达式。
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =',flag0)
print('flag1 =',flag1)
print('flag2 =',flag2)
print('flag3 =',flag3)
print('flag4 =',flag4)
print('flag5 =',flag5)
print(flag1 and not flag2)
print(1 > 2 or 2 == 3)