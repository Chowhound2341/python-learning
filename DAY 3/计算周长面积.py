"""
输入半径计算周长与面积
Version: 1.0
Author: Wei si qi
"""

import math

while True:
	try:
		radius = float(input('请输入半径：'))
		break
	except ValueError:
		print("输入无效，请输入一个数字。")

perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')