"""BMI计算器
Version: 1.o
Author: wei si qi
"""
height = float(input('身高（cm): '))
weight = float(input('体重（kg): '))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
elif 24 <= bmi < 28:
    print('你的身材有点胖！')