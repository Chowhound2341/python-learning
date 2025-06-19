"""
输入两个正整数求他们的最大公约数和最小公倍数
Version: 2.0 (优化版)
Author: wei si qi
"""
import math


def gcd_euclidean(a, b):
    """
    使用欧几里得算法求最大公约数 - 最高效的方法
    时间复杂度: O(log(min(a,b)))
    Args:
        a, b (int): 两个正整数
    Returns:
        int: 最大公约数
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    计算最小公倍数
    公式: lcm(a,b) = (a * b) / gcd(a,b)
    Args:
        a, b (int): 两个正整数
    Returns:
        int: 最小公倍数
    """
    return abs(a * b) // gcd_euclidean(a, b)


def gcd_brute_force(a, b):
    """
    暴力法求最大公约数 - 你原来的方法的优化版
    从较小数开始向下查找，提高效率
    Args:
        a, b (int): 两个正整数
    Returns:
        int: 最大公约数
    """
    # 从较小的数开始查找，而不是从x开始
    start = min(a, b)
    for i in range(start, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1  # 理论上不会到达这里


def get_valid_input(prompt):
    """
    获取有效的正整数输入
    Args:
        prompt (str): 输入提示
    Returns:
        int: 用户输入的正整数
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入正整数！")
                continue
            return value
        except ValueError:
            print("请输入有效的整数！")


def compare_algorithms(x, y):
    """
    比较不同算法的效率
    Args:
        x, y (int): 两个正整数
    """
    import time
    
    # 测试暴力法
    start_time = time.time()
    gcd1 = gcd_brute_force(x, y)
    brute_time = time.time() - start_time
    
    # 测试欧几里得算法
    start_time = time.time()
    gcd2 = gcd_euclidean(x, y)
    euclidean_time = time.time() - start_time
    
    # 测试内置函数
    start_time = time.time()
    gcd3 = math.gcd(x, y)
    builtin_time = time.time() - start_time
    
    print(f"\n算法效率对比:")
    print(f"暴力法:      {gcd1} (耗时: {brute_time*1000000:.2f} 微秒)")
    print(f"欧几里得:    {gcd2} (耗时: {euclidean_time*1000000:.2f} 微秒)")
    print(f"内置函数:    {gcd3} (耗时: {builtin_time*1000000:.2f} 微秒)")


def main():
    """主函数"""
    print("🔢 最大公约数和最小公倍数计算器")
    print("=" * 40)
    
    # 获取用户输入
    x = get_valid_input('请输入第一个正整数 x = ')
    y = get_valid_input('请输入第二个正整数 y = ')
    
    # 计算结果
    gcd_result = gcd_euclidean(x, y)
    lcm_result = lcm(x, y)
    
    # 显示结果
    print(f"\n📊 计算结果:")
    print(f"最大公约数(GCD): {gcd_result}")
    print(f"最小公倍数(LCM): {lcm_result}")
    
    # 验证结果
    print(f"\n✅ 验证:")
    print(f"{x} = {gcd_result} × {x // gcd_result}")
    print(f"{y} = {gcd_result} × {y // gcd_result}")
    print(f"LCM × GCD = {lcm_result} × {gcd_result} = {lcm_result * gcd_result}")
    print(f"x × y = {x} × {y} = {x * y}")
    print(f"验证通过: {lcm_result * gcd_result == x * y}")
    
    # 性能比较（可选）
    if max(x, y) < 10000:  # 只在数字不太大时进行比较
        compare_algorithms(x, y)


if __name__ == "__main__":
    main()