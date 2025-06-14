"""
0-100整数求和
Version: 1.0
Author: wei si qi
"""
total = 0
for i in range(101):  # range(101) 生成从0到100的整数
    total += i  # 累加每个整数到total中
print("0-100整数的和是:", total)  # 输出总和 