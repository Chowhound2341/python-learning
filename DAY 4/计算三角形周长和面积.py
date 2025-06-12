# 计算三角形的周长和面积
import math

a = float(input('请输入第一条边a: '))
b = float(input('请输入第二条边b: '))
c = float(input('请输入第三条边c: '))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'三角形的周长为: {perimeter}')
    print(f'三角形的面积为: {area}')
else:
    print('不能构成三角形')
