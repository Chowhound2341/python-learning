from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    两个数字相加的函数。
    
    Args:
        a: 第一个数字（整数或浮点数）
        b: 第二个数字（整数或浮点数）
    
    Returns:
        两个数字的和
    
    Raises:
        TypeError: 当输入不是数字类型时抛出异常
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字类型")
    return a + b


def test_add():
    """
    测试add函数的功能，包括各种边界情况。
    
    测试用例包括：
    - 正数相加
    - 负数相加
    - 零值相加
    - 浮点数相加
    - 大数相加
    - 异常情况处理
    """
    # 基础测试用例
    assert add(1, 2) == 3, "正数相加测试失败"
    assert add(-1, 1) == 0, "负数与正数相加测试失败"
    assert add(0, 0) == 0, "零值相加测试失败"
    
    # 浮点数测试
    assert abs(add(1.5, 2.5) - 4.0) < 1e-10, "浮点数相加测试失败"
    assert abs(add(-1.5, 1.5) - 0.0) < 1e-10, "浮点数相减测试失败"
    
    # 大数测试
    assert add(1000000, 2000000) == 3000000, "大数相加测试失败"
      # 异常处理测试
    try:
        add("1", 2)  # type: ignore
        assert False, "应该抛出TypeError异常"
    except TypeError:
        pass  # 预期的异常
    
    try:
        add(1, None)  # type: ignore
        assert False, "应该抛出TypeError异常"
    except TypeError:
        pass  # 预期的异常


if __name__ == "__main__":
    try:
        test_add()
        print("✓ 所有测试用例通过！")
        
        # 演示正常使用
        print("\n--- 使用示例 ---")
        print(f"add(10, 20) = {add(10, 20)}")
        print(f"add(3.14, 2.86) = {add(3.14, 2.86)}")
        print(f"add(-5, 3) = {add(-5, 3)}")
        
    except AssertionError as e:
        print(f"✗ 测试失败: {e}")
    except Exception as e:
        print(f"✗ 运行时错误: {e}")