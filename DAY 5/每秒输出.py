"""
多功能定时输出器 - 时间控制输出系统
Version: 2.0
Author: wei si qi
功能: 提供多种定时输出模式、进度显示、日志记录等功能
"""

import time
import datetime
import threading
import random
import os
from typing import List, Optional, Callable
import signal
import sys

class TimedOutputManager:
    """定时输出管理器，提供多种输出模式和控制功能"""
    
    def __init__(self):
        self.is_running = False
        self.output_history = []
        self.start_time = None
        self.total_outputs = 0
        self.pause_event = threading.Event()
        self.stop_event = threading.Event()
        
        # 注册信号处理器（Ctrl+C优雅退出）
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """处理中断信号"""
        print(f"\n\n收到中断信号，正在优雅退出...")
        self.stop()
        sys.exit(0)
    
    def simple_output(self, message: str = "hello world", 
                     interval: float = 1.0, 
                     count: int = 10,
                     show_progress: bool = True) -> None:
        """
        基础定时输出功能
        
        参数:
        message: 输出消息
        interval: 时间间隔（秒）
        count: 输出次数
        show_progress: 是否显示进度
        """
        self.start_time = time.time()
        self.is_running = True
        self.total_outputs = 0
        
        print(f"开始输出: '{message}' (间隔{interval}秒, 共{count}次)")
        print("-" * 50)
        
        for i in range(count):
            if self.stop_event.is_set():
                break
                
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            output_msg = f"[{current_time}] {message}"
            
            if show_progress:
                progress = (i + 1) / count * 100
                output_msg += f" (进度: {progress:.1f}%)"
            
            print(output_msg)
            
            # 记录输出历史
            self.output_history.append({
                'timestamp': current_time,
                'message': message,
                'sequence': i + 1,
                'total': count
            })
            
            self.total_outputs += 1
            
            # 最后一次输出不需要等待
            if i < count - 1:
                time.sleep(interval)
        
        self.is_running = False
        elapsed_time = time.time() - self.start_time
        print(f"\n输出完成! 总用时: {elapsed_time:.2f}秒")
    
    def countdown_output(self, message: str = "倒计时", 
                        start_num: int = 10,
                        interval: float = 1.0) -> None:
        """倒计时输出模式"""
        self.start_time = time.time()
        self.is_running = True
        
        print(f"倒计时开始: 从 {start_num} 到 0")
        print("-" * 30)
        
        for i in range(start_num, -1, -1):
            if self.stop_event.is_set():
                break
                
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if i == 0:
                print(f"[{current_time}] 🎉 {message} 完成! 🎉")
            else:
                print(f"[{current_time}] {message}: {i}")
            
            self.total_outputs += 1
            
            if i > 0:
                time.sleep(interval)
        
        self.is_running = False
    
    def random_message_output(self, messages: List[str], 
                             interval: float = 1.0,
                             count: int = 10) -> None:
        """随机消息输出模式"""
        if not messages:
            messages = ["Hello", "World", "Python", "编程", "学习"]
        
        self.start_time = time.time()
        self.is_running = True
        
        print(f"随机消息输出 (共{count}次, 间隔{interval}秒)")
        print(f"消息库: {messages}")
        print("-" * 50)
        
        for i in range(count):
            if self.stop_event.is_set():
                break
                
            message = random.choice(messages)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] 🎲 {message}")
            
            self.total_outputs += 1
            
            if i < count - 1:
                time.sleep(interval)
        
        self.is_running = False
    
    def progress_bar_output(self, task_name: str = "处理中",
                           total_steps: int = 20,
                           interval: float = 0.5) -> None:
        """进度条输出模式"""
        self.start_time = time.time()
        self.is_running = True
        
        print(f"任务: {task_name}")
        print("=" * 50)
        
        for i in range(total_steps + 1):
            if self.stop_event.is_set():
                break
                
            progress = i / total_steps
            bar_length = 30
            filled_length = int(bar_length * progress)
            
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            percent = progress * 100
            
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            print(f"\r[{current_time}] |{bar}| {percent:.1f}% ({i}/{total_steps})", end="")
            
            self.total_outputs += 1
            
            if i < total_steps:
                time.sleep(interval)
        
        print(f"\n✅ {task_name} 完成!")
        self.is_running = False
    
    def clock_output(self, duration: int = 60) -> None:
        """时钟输出模式"""
        self.start_time = time.time()
        self.is_running = True
        end_time = time.time() + duration
        
        print(f"数字时钟运行 {duration} 秒")
        print("=" * 30)
        
        while time.time() < end_time and not self.stop_event.is_set():
            current_time = datetime.datetime.now()
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # 清除当前行并输出新时间
            print(f"\r🕐 {time_str}", end="", flush=True)
            
            self.total_outputs += 1
            time.sleep(1)
        
        print(f"\n⏰ 时钟停止运行")
        self.is_running = False
    
    def threaded_output(self, message: str = "多线程输出",
                       thread_count: int = 3,
                       interval: float = 1.0,
                       duration: int = 10) -> None:
        """多线程输出模式"""
        self.start_time = time.time()
        self.is_running = True
        
        print(f"启动 {thread_count} 个输出线程，运行 {duration} 秒")
        print("-" * 50)
        
        def worker(thread_id: int):
            end_time = time.time() + duration
            counter = 0
            
            while time.time() < end_time and not self.stop_event.is_set():
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                counter += 1
                print(f"[{current_time}] 线程{thread_id}: {message} #{counter}")
                self.total_outputs += 1
                time.sleep(interval)
        
        # 创建并启动线程
        threads = []
        for i in range(thread_count):
            thread = threading.Thread(target=worker, args=(i+1,))
            threads.append(thread)
            thread.start()
        
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        
        self.is_running = False
        print(f"\n所有线程执行完毕!")
    
    def stop(self) -> None:
        """停止输出"""
        self.stop_event.set()
        self.is_running = False
        print(f"\n输出已停止!")
    
    def pause(self) -> None:
        """暂停输出"""
        self.pause_event.clear()
        print(f"\n输出已暂停，输入 resume 恢复")
    
    def resume(self) -> None:
        """恢复输出"""
        self.pause_event.set()
        print(f"\n输出已恢复")
    
    def show_statistics(self) -> None:
        """显示统计信息"""
        if self.start_time:
            elapsed = time.time() - self.start_time
            rate = self.total_outputs / elapsed if elapsed > 0 else 0
            
            print(f"\n📊 统计信息:")
            print(f"总输出次数: {self.total_outputs}")
            print(f"运行时间: {elapsed:.2f} 秒")
            print(f"输出频率: {rate:.2f} 次/秒")
    
    def show_history(self, limit: int = 10) -> None:
        """显示输出历史"""
        print(f"\n📝 最近 {limit} 条输出历史:")
        print("-" * 40)
        
        recent_history = self.output_history[-limit:] if self.output_history else []
        
        for record in recent_history:
            print(f"[{record['timestamp']}] {record['message']} "
                  f"({record['sequence']}/{record['total']})")
    
    def save_log(self, filename: Optional[str] = None) -> None:
        """保存输出日志到文件"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output_log_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"定时输出日志\n")
                f.write(f"生成时间: {datetime.datetime.now()}\n")
                f.write(f"总输出次数: {self.total_outputs}\n")
                f.write("=" * 50 + "\n\n")
                
                for record in self.output_history:
                    f.write(f"[{record['timestamp']}] {record['message']} "
                           f"({record['sequence']}/{record['total']})\n")
            
            print(f"✅ 日志已保存到: {filename}")
        except Exception as e:
            print(f"❌ 保存日志失败: {e}")

def demonstrate_basic_functionality():
    """演示基本功能"""
    print("=== 基础演示 ===")
    manager = TimedOutputManager()
    
    # 保持原有功能
    manager.simple_output("hello world", 1.0, 5, True)

def interactive_mode():
    """交互模式"""
    manager = TimedOutputManager()
    
    while True:
        print(f"\n{'='*60}")
        print("🚀 多功能定时输出器")
        print(f"{'='*60}")
        print("1. 基础定时输出")
        print("2. 倒计时输出")
        print("3. 随机消息输出")
        print("4. 进度条输出")
        print("5. 数字时钟")
        print("6. 多线程输出")
        print("7. 查看统计信息")
        print("8. 查看输出历史")
        print("9. 保存日志")
        print("0. 退出")
        print("-" * 60)
        
        try:
            choice = input("请选择功能 (0-9): ").strip()
            
            if choice == '0':
                print("👋 感谢使用！再见！")
                break
            
            elif choice == '1':
                message = input("输入消息内容 (默认: hello world): ").strip() or "hello world"
                interval = float(input("输入时间间隔/秒 (默认: 1.0): ") or "1.0")
                count = int(input("输入输出次数 (默认: 10): ") or "10")
                show_progress = input("显示进度? (y/n, 默认: y): ").strip().lower() != 'n'
                
                manager.simple_output(message, interval, count, show_progress)
            
            elif choice == '2':
                message = input("输入倒计时消息 (默认: 倒计时): ").strip() or "倒计时"
                start_num = int(input("起始数字 (默认: 10): ") or "10")
                interval = float(input("时间间隔/秒 (默认: 1.0): ") or "1.0")
                
                manager.countdown_output(message, start_num, interval)
            
            elif choice == '3':
                messages_input = input("输入消息列表，用逗号分隔 (默认随机): ").strip()
                if messages_input:
                    messages = [msg.strip() for msg in messages_input.split(',')]
                else:
                    messages = ["Hello", "World", "Python", "编程", "学习", "代码", "程序"]
                
                interval = float(input("时间间隔/秒 (默认: 1.0): ") or "1.0")
                count = int(input("输出次数 (默认: 10): ") or "10")
                
                manager.random_message_output(messages, interval, count)
            
            elif choice == '4':
                task_name = input("任务名称 (默认: 处理中): ").strip() or "处理中"
                total_steps = int(input("总步数 (默认: 20): ") or "20")
                interval = float(input("步骤间隔/秒 (默认: 0.5): ") or "0.5")
                
                manager.progress_bar_output(task_name, total_steps, interval)
            
            elif choice == '5':
                duration = int(input("运行时长/秒 (默认: 30): ") or "30")
                manager.clock_output(duration)
            
            elif choice == '6':
                message = input("输出消息 (默认: 多线程输出): ").strip() or "多线程输出"
                thread_count = int(input("线程数量 (默认: 3): ") or "3")
                interval = float(input("时间间隔/秒 (默认: 1.0): ") or "1.0")
                duration = int(input("运行时长/秒 (默认: 10): ") or "10")
                
                manager.threaded_output(message, thread_count, interval, duration)
            
            elif choice == '7':
                manager.show_statistics()
            
            elif choice == '8':
                limit = int(input("显示条数 (默认: 10): ") or "10")
                manager.show_history(limit)
            
            elif choice == '9':
                filename = input("文件名 (留空自动生成): ").strip() or None
                manager.save_log(filename)
            
            else:
                print("❌ 无效选择，请重新输入！")
        
        except ValueError as e:
            print(f"❌ 输入格式错误: {e}")
        except KeyboardInterrupt:
            print(f"\n👋 用户中断操作")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

# 主程序
if __name__ == "__main__":
    try:
        # 保持原有基本功能演示
        demonstrate_basic_functionality()
        
        # 提供完整功能选择
        print(f"\n{'='*60}")
        choice = input("🎯 是否启动完整功能模式？(y/n): ").strip().lower()
        if choice in ['y', 'yes', '是']:
            interactive_mode()
        else:
            print("📝 程序结束，感谢使用！")
    
    except KeyboardInterrupt:
        print(f"\n\n👋 程序被用户中断，再见！")
    except Exception as e:
        print(f"❌ 程序异常: {e}")