"""
输入半径计算周长与面积
Version: 2.0
Author: Wei si qi
"""

import math

def calculate_circle_properties(radius):
	"""根据半径计算圆的周长和面积"""
	if radius <= 0:
		raise ValueError("半径必须是正数。")
	perimeter = 2 * math.pi * radius
	area = math.pi * radius ** 2
	return perimeter, area

def get_radius_from_user():
	"""从用户处获取有效的半径输入"""
	while True:
		try:
			radius_str = input('请输入半径：')
			radius = float(radius_str)
			if radius > 0:
				return radius
			else:
				print("半径必须是正数，请重新输入。")
		except ValueError:
			print("输入无效，请输入一个数字。")

def main():
	"""主函数，执行程序逻辑"""
	radius = get_radius_from_user()
	try:
		perimeter, area = calculate_circle_properties(radius)
		print(f'周长: {perimeter:.2f}')
		print(f'面积: {area:.2f}')
	except ValueError as e:
		print(f"错误: {e}")

if __name__ == '__main__':
	main()