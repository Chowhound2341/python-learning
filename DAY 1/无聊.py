x = 1
y = 2

# 方法1：使用条件判断比较大小
def compare(a, b):
    """比较两个数的大小，返回-1, 0, 1分别表示小于、等于、大于"""
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

result = compare(x, y)
print(f"比较结果: {result}")  # -1表示x<y, 0表示x=y, 1表示x>y

# 方法2：直接比较并输出结果
if x < y:
    print(f"{x} 小于 {y}")
elif x > y:
    print(f"{x} 大于 {y}")
else:
    print(f"{x} 等于 {y}")

# 方法3：使用operator模块（类似cmp的替代方案）
import operator
print(f"x < y: {operator.lt(x, y)}")
print(f"x > y: {operator.gt(x, y)}")
print(f"x == y: {operator.eq(x, y)}")