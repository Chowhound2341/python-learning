"""
多功能数学计算器 - 整数求和系统
Version: 2.0
Author: wei si qi
功能: 提供多种数学计算方法和统计分析
"""

import time
import math
from typing import List, Tuple, Dict

class NumberCalculator:
    """数字计算器类，提供各种数学计算功能"""
    
    def __init__(self):
        self.calculation_history = []
        self.start_time = None
        self.end_time = None
    
    def sum_range(self, start: int, end: int, method: str = 'loop') -> Dict:
        """
        计算指定范围内整数的和
        
        参数:
        start: 起始数字
        end: 结束数字
        method: 计算方法 ('loop', 'formula', 'builtin')
        
        返回: 包含结果和统计信息的字典
        """
        self.start_time = time.time()
        
        if method == 'loop':
            result = self._sum_by_loop(start, end)
        elif method == 'formula':
            result = self._sum_by_formula(start, end)
        elif method == 'builtin':
            result = self._sum_by_builtin(start, end)
        else:
            raise ValueError("方法必须是 'loop', 'formula', 或 'builtin'")
        
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        
        calculation_info = {
            'result': result,
            'method': method,
            'range': (start, end),
            'count': end - start + 1,
            'execution_time': execution_time,
            'average': result / (end - start + 1) if end >= start else 0
        }
        
        self.calculation_history.append(calculation_info)
        return calculation_info
    
    def _sum_by_loop(self, start: int, end: int) -> int:
        """使用循环计算和"""
        total = 0
        for i in range(start, end + 1):
            total += i
        return total
    
    def _sum_by_formula(self, start: int, end: int) -> int:
        """使用数学公式计算和: n*(n+1)/2 - (n-1)*n/2"""
        if start == 0:
            return end * (end + 1) // 2
        else:
            return end * (end + 1) // 2 - (start - 1) * start // 2
    
    def _sum_by_builtin(self, start: int, end: int) -> int:
        """使用内置函数计算和"""
        return sum(range(start, end + 1))
    
    def sum_even_numbers(self, start: int, end: int) -> Dict:
        """计算指定范围内偶数的和"""
        self.start_time = time.time()
        
        total = 0
        count = 0
        even_numbers = []
        
        for i in range(start, end + 1):
            if i % 2 == 0:
                total += i
                count += 1
                even_numbers.append(i)
        
        self.end_time = time.time()
        
        return {
            'result': total,
            'count': count,
            'numbers': even_numbers,
            'average': total / count if count > 0 else 0,
            'execution_time': self.end_time - self.start_time
        }
    
    def sum_odd_numbers(self, start: int, end: int) -> Dict:
        """计算指定范围内奇数的和"""
        self.start_time = time.time()
        
        total = 0
        count = 0
        odd_numbers = []
        
        for i in range(start, end + 1):
            if i % 2 != 0:
                total += i
                count += 1
                odd_numbers.append(i)
        
        self.end_time = time.time()
        
        return {
            'result': total,
            'count': count,
            'numbers': odd_numbers,
            'average': total / count if count > 0 else 0,
            'execution_time': self.end_time - self.start_time
        }
    
    def sum_multiples(self, start: int, end: int, multiple: int) -> Dict:
        """计算指定范围内某个数的倍数的和"""
        self.start_time = time.time()
        
        total = 0
        count = 0
        multiples_list = []
        
        for i in range(start, end + 1):
            if i % multiple == 0:
                total += i
                count += 1
                multiples_list.append(i)
        
        self.end_time = time.time()
        
        return {
            'result': total,
            'count': count,
            'multiple_of': multiple,
            'numbers': multiples_list,
            'average': total / count if count > 0 else 0,
            'execution_time': self.end_time - self.start_time
        }
    
    def get_statistics(self, start: int, end: int) -> Dict:
        """获取范围内数字的统计信息"""
        numbers = list(range(start, end + 1))
        
        return {
            'count': len(numbers),
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers),
            'median': numbers[len(numbers) // 2],
            'range_span': max(numbers) - min(numbers)
        }
    
    def compare_methods(self, start: int, end: int) -> None:
        """比较不同计算方法的性能"""
        print(f"\n{'='*60}")
        print(f"性能比较: {start} 到 {end} 的求和")
        print(f"{'='*60}")
        
        methods = ['loop', 'formula', 'builtin']
        results = {}
        
        for method in methods:
            result = self.sum_range(start, end, method)
            results[method] = result
            print(f"{method.upper():>8} 方法: 结果={result['result']:>10}, "
                  f"时间={result['execution_time']:.6f}秒")
        
        # 找出最快的方法
        fastest = min(results.keys(), key=lambda k: results[k]['execution_time'])
        print(f"\n最快方法: {fastest.upper()}")
    
    def show_history(self) -> None:
        """显示计算历史"""
        if not self.calculation_history:
            print("暂无计算历史记录")
            return
        
        print(f"\n{'='*50}")
        print("计算历史记录")
        print(f"{'='*50}")
        
        for i, record in enumerate(self.calculation_history, 1):
            print(f"记录 {i}: {record['method'].upper()} 方法")
            print(f"  范围: {record['range'][0]} - {record['range'][1]}")
            print(f"  结果: {record['result']}")
            print(f"  耗时: {record['execution_time']:.6f}秒")
            print("-" * 30)

def demonstrate_basic_functionality():
    """演示基本功能"""
    print("=== 基础演示 ===")
    calc = NumberCalculator()
    
    # 原始功能 - 0到100求和
    result = calc.sum_range(0, 100, 'loop')
    print(f"0-100整数的和是: {result['result']}")
    print(f"计算用时: {result['execution_time']:.6f}秒")
    print(f"平均值: {result['average']:.2f}")

def interactive_mode():
    """交互模式"""
    calc = NumberCalculator()
    
    while True:
        print(f"\n{'='*50}")
        print("多功能数学计算器")
        print(f"{'='*50}")
        print("1. 整数求和")
        print("2. 偶数求和")
        print("3. 奇数求和")
        print("4. 倍数求和")
        print("5. 数字统计")
        print("6. 性能比较")
        print("7. 查看历史记录")
        print("8. 清除历史记录")
        print("0. 退出")
        print("-" * 50)
        
        try:
            choice = input("请选择功能 (0-8): ").strip()
            
            if choice == '0':
                print("感谢使用！再见！")
                break
            
            elif choice in ['1', '2', '3', '4', '5', '6']:
                start = int(input("请输入起始数字: "))
                end = int(input("请输入结束数字: "))
                
                if start > end:
                    print("起始数字不能大于结束数字！")
                    continue
                
                if choice == '1':
                    method = input("选择计算方法 (loop/formula/builtin): ").strip()
                    if method not in ['loop', 'formula', 'builtin']:
                        method = 'loop'
                    result = calc.sum_range(start, end, method)
                    print(f"\n结果: {result['result']}")
                    print(f"方法: {result['method']}")
                    print(f"数量: {result['count']}")
                    print(f"平均值: {result['average']:.2f}")
                    print(f"执行时间: {result['execution_time']:.6f}秒")
                
                elif choice == '2':
                    result = calc.sum_even_numbers(start, end)
                    print(f"\n偶数和: {result['result']}")
                    print(f"偶数个数: {result['count']}")
                    print(f"平均值: {result['average']:.2f}")
                    print(f"偶数列表: {result['numbers'][:10]}{'...' if len(result['numbers']) > 10 else ''}")
                
                elif choice == '3':
                    result = calc.sum_odd_numbers(start, end)
                    print(f"\n奇数和: {result['result']}")
                    print(f"奇数个数: {result['count']}")
                    print(f"平均值: {result['average']:.2f}")
                    print(f"奇数列表: {result['numbers'][:10]}{'...' if len(result['numbers']) > 10 else ''}")
                
                elif choice == '4':
                    multiple = int(input("请输入倍数: "))
                    result = calc.sum_multiples(start, end, multiple)
                    print(f"\n{multiple}的倍数和: {result['result']}")
                    print(f"倍数个数: {result['count']}")
                    print(f"平均值: {result['average']:.2f}")
                    print(f"倍数列表: {result['numbers'][:10]}{'...' if len(result['numbers']) > 10 else ''}")
                
                elif choice == '5':
                    stats = calc.get_statistics(start, end)
                    print(f"\n统计信息:")
                    print(f"数量: {stats['count']}")
                    print(f"总和: {stats['sum']}")
                    print(f"平均值: {stats['average']:.2f}")
                    print(f"最小值: {stats['min']}")
                    print(f"最大值: {stats['max']}")
                    print(f"中位数: {stats['median']}")
                    print(f"范围跨度: {stats['range_span']}")
                
                elif choice == '6':
                    calc.compare_methods(start, end)
            
            elif choice == '7':
                calc.show_history()
            
            elif choice == '8':
                calc.calculation_history.clear()
                print("历史记录已清除！")
            
            else:
                print("无效选择，请重新输入！")
        
        except ValueError:
            print("请输入有效的数字！")
        except Exception as e:
            print(f"发生错误: {e}")

# 主程序
if __name__ == "__main__":
    # 保持原有基本功能
    demonstrate_basic_functionality()
    
    # 提供交互模式选择
    print(f"\n{'='*50}")
    choice = input("是否启动完整功能模式？(y/n): ").strip().lower()
    if choice in ['y', 'yes', '是']:
        interactive_mode()
    else:
        print("程序结束，感谢使用！")