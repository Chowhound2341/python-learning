"""
海象运算符
Version: 1.0
Author: Wei si qi
"""
# The following line would raise a SyntaxError because `=` cannot be used in this context:
# The line below would raise a SyntaxError because assignment using '=' is not allowed within expressions in Python.
#海象运算符: The walrus operator allows assignment within an expression.
#海象运算符
print((a := 10))
print(a)