"""
打印乘法口诀表
Version: 1.0
Author: wei si qi
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {j * i}', end='\t')
    print()  # 每行结束后换行