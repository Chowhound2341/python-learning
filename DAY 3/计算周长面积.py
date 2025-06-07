"""
输入半径计算周长与面积
Version: 1.0
Author: Wei si qi
"""

import math

while True:
	try:
		radius = float(input('请输入半径：'))
		if radius > 0:
			# 计算周长
			perimeter = 2 * math.pi * radius
			# 计算面积
			area = math.pi * radius ** 2
			break
		else:
			print("半径必须是正数，请重新输入。")
	except ValueError:
		print("输入无效，请输入一个数字。")

print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')