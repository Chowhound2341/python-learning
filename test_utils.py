# 正确，会被发现
def test_addition():
    assert 1 + 1 == 2

# 错误，会被忽略
def addition_test():
    assert 1 + 1 == 2
