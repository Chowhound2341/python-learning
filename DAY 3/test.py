def add(a, b):
    """This function adds two numbers."""
    return a + b

def test_add():
    """This function tests the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

if __name__ == "__main__":
    test_add()
    print("All tests passed!")