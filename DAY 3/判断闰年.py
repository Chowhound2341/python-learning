"""
判断闰年，闰年输出True,平年输出False

Version: 1.2
Author: wei si qi
"""

def is_leap_year(year: int) -> bool:
    """
    判断是否为闰年

    Args:
        year (int): 要判断的年份
    Returns:
        bool: 闰年返回True，平年返回False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    while True:
        year_input = input('请输入年份（输入q退出）：').strip()
        if year_input.lower() == 'q':
            print('程序已退出。')
            break
        if not year_input.isdigit():
            print('输入错误，请输入有效的年份数字')
            continue
        year = int(year_input)
        if year <= 0:
            print('请输入正整数年份')
            continue

        result = is_leap_year(year)
        print(f'{year}年是{"闰" if result else "平"}年')
        print(f'is_leap = {result}')

if __name__ == "__main__":
    main()