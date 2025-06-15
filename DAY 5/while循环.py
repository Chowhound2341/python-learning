"""
使用while循环求和
Version: 1.0
Author: wei si qi
"""
total = 0  # 初始化总和为0
i = 1  # 初始化计数器i为1
while i <= 100:
    total += i 
    i += 1  # 计数器i自增1
print("0-100整数的和是:", total)  # 输出总和

"""
偶数求和
"""
total = 0  # 初始化总和为0
i = 2  # 初始化计数器i为0
while True:
    total += i
    i += 2  # 计数器i自增2
    if i > 100:  # 当i大于100时退出循环
        break
print("0-100偶数的和是:", total)  # 输出总和

#continue使用
total = 0
for i in range(1, 101):
    if i % 2 != 0:  # 如果i是奇数
        continue  # 跳过当前循环，继续下一个循环
    total += i  # 累加偶数到total中
print("0-100偶数的和是:", total)  # 输出总和