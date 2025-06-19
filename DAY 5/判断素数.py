"""
输入一个大于1的整数，判断它是否是素数。
Version: 2.0 (优化版)
Author: wei si qi
"""
import math


def is_prime(num):
    """
    判断一个数是否为素数
    Args:
        num (int): 待判断的整数
    Returns:
        bool: 如果是素数返回True，否则返回False
    """
    # 处理特殊情况
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # 排除所有偶数
        return False
    
    # 只检查奇数因子，从3开始，步长为2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_valid_input():
    """
    获取有效的用户输入
    Returns:
        int: 用户输入的有效整数
    """
    while True:
        try:
            num = int(input("请输入一个大于1的整数："))
            if num <= 1:
                print("请输入大于1的整数！")
                continue
            return num
        except ValueError:
            print("请输入有效的整数！")


def main():
    """主函数"""
    num = get_valid_input()
    
    if is_prime(num):
        print(f"{num} 是素数")
    else:
        print(f"{num} 不是素数")
    
    # 可选：显示一些额外信息
    if num > 2:
        factors = []
        temp = num
        for i in range(2, int(math.sqrt(num)) + 1):
            while temp % i == 0:
                factors.append(i)
                temp //= i
        if temp > 1:
            factors.append(temp)
        
        if len(factors) > 1:
            print(f"因数分解: {num} = {' × '.join(map(str, factors))}")


if __name__ == "__main__":
    main()