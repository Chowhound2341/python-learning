#第一种方法
total = 0
for i in range(1, 101):
    if i % 2 == 0:  # 判断i是否为偶数
        total += i
print("0-100偶数的和是:", total)  # 输出总和

# 第二种方法
total = 0
for i in range(0, 101, 2):  # range(0, 101, 2) 生成从0到100的偶数
    total += i  # 累加每个偶数到total中
print("0-100偶数的和是:", total)  # 输出总和

# 第三种方法
total = sum(range(0, 101, 2))  # 使用sum函数直接计算0到100的偶数和
print("0-100偶数的和是:", total)  # 输出总和

# 第四种方法
total = 0
for i in range(101):
    if i & 1 == 0:  # 使用位运算判断i是否为偶数
        total += i
print("0-100偶数的和是:", total)  # 输出总和

# 第五种方法
total = 0
for i in range(101):
    if not i % 2:  # 使用not判断i是否为偶数
        total += i
print("0-100偶数的和是:", total)  # 输出总和

# 第六种方法
total = 0
for i in range(101):
    if i // 2 * 2 == i:  # 使用整除判断i是否为偶数
        total += i
print("0-100偶数的和是:", total)  # 输出总和    