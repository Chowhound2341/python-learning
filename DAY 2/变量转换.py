"""
   变量的类型转换
   
   Version: 1.0
   Author: Wei si qi 
    """
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello,world'
g = True
print(float(a))
print(int(b))
print(int(c))
print(int(c, base=16))
print(int(d, base=2))
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))
print(ord('d'))