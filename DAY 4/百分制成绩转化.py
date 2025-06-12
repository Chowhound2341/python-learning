"""
百分制成绩转化
Version: 1.0
Author: Wei si qi
"""
score = float(input('请输入成绩（0-100）: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'  
else:
    grade = 'E'
print(f'{grade = }')          