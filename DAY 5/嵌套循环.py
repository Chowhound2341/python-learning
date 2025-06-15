"""
多功能乘法口诀表生成器
Version: 2.0
Author: wei si qi
"""

def print_multiplication_table(max_num=9, style='normal'):
    """
    打印乘法口诀表
    
    参数:
    max_num: 最大数字，默认为9
    style: 显示样式 ('normal', 'full', 'colorful')
    """
    print(f"\n{'='*50}")
    print(f"{'乘法口诀表 (1-' + str(max_num) + ')':^46}")
    print(f"{'='*50}")
    
    if style == 'full':
        # 完整的乘法表（包含重复项）
        print(f"{'':>4}", end='')
        for j in range(1, max_num + 1):
            print(f"{j:>6}", end='')
        print()
        print("-" * (6 * max_num + 4))
        
        for i in range(1, max_num + 1):
            print(f"{i:>3}|", end='')
            for j in range(1, max_num + 1):
                print(f"{i*j:>6}", end='')
            print()
    
    elif style == 'colorful':
        # 彩色输出（模拟）
        for i in range(1, max_num + 1):
            for j in range(1, i + 1):
                result = j * i
                if result < 10:
                    print(f'{j} × {i} = {result:2}', end='  ')
                else:
                    print(f'{j} × {i} = {result}', end='  ')
            print()
    
    else:  # normal style
        for i in range(1, max_num + 1):
            for j in range(1, i + 1):
                print(f'{j} × {i} = {j * i:2}', end='  ')
            print()

def get_multiplication_facts(num):
    """获取指定数字的乘法口诀"""
    print(f"\n{num} 的乘法口诀:")
    print("-" * 20)
    for i in range(1, 10):
        print(f"{i} × {num} = {i * num}")

def find_multiplication_result(target):
    """查找能得到指定结果的乘法组合"""
    print(f"\n能得到结果 {target} 的乘法组合:")
    print("-" * 30)
    combinations = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == target:
                combinations.append((i, j))
    
    if combinations:
        for combo in combinations:
            print(f"{combo[0]} × {combo[1]} = {target}")
    else:
        print(f"在1-9范围内没有找到乘积为 {target} 的组合")

def interactive_mode():
    """交互模式"""
    while True:
        print("\n" + "="*50)
        print("多功能乘法口诀表")
        print("="*50)
        print("1. 标准乘法口诀表")
        print("2. 完整乘法表")
        print("3. 格式化乘法口诀表")
        print("4. 指定数字的乘法口诀")
        print("5. 查找乘法组合")
        print("6. 自定义范围乘法表")
        print("0. 退出")
        print("-"*50)
        
        choice = input("请选择功能 (0-6): ").strip()
        
        if choice == '1':
            print_multiplication_table()
        elif choice == '2':
            print_multiplication_table(style='full')
        elif choice == '3':
            print_multiplication_table(style='colorful')
        elif choice == '4':
            try:
                num = int(input("请输入数字 (1-9): "))
                if 1 <= num <= 9:
                    get_multiplication_facts(num)
                else:
                    print("请输入1-9之间的数字！")
            except ValueError:
                print("请输入有效的数字！")
        elif choice == '5':
            try:
                target = int(input("请输入目标结果: "))
                find_multiplication_result(target)
            except ValueError:
                print("请输入有效的数字！")
        elif choice == '6':
            try:
                max_num = int(input("请输入最大数字 (1-20): "))
                if 1 <= max_num <= 20:
                    print_multiplication_table(max_num)
                else:
                    print("请输入1-20之间的数字！")
            except ValueError:
                print("请输入有效的数字！")
        elif choice == '0':
            print("感谢使用！再见！")
            break
        else:
            print("无效选择，请重新输入！")

# 主程序
if __name__ == "__main__":
    # 演示不同功能
    print("=== 基础演示 ===")
    print_multiplication_table()
    
    # 启动交互模式
    print("\n" + "="*50)
    start_interactive = input("是否启动交互模式？(y/n): ").strip().lower()
    if start_interactive in ['y', 'yes', '是']:
        interactive_mode()
    else:
        print("程序结束，感谢使用！")
    