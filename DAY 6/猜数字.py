# 猜数字小游戏 - 优化版
import random
import time


def display_welcome():
    """显示游戏欢迎信息和规则"""
    print("🎮" + "=" * 40 + "🎮")
    print("🎯      欢迎来到猜数字小游戏！      🎯")
    print("🎮" + "=" * 40 + "🎮")
    print("🎲 游戏规则：")
    print("   • 系统会随机生成一个1-100之间的数字")
    print("   • 你有最多7次机会猜中这个数字")
    print("   • 每次猜错后会告诉你数字的大小提示")
    print("   • 猜中数字或用完机会后游戏结束")
    print("-" * 44)


def get_valid_input(prompt, min_val=1, max_val=100):
    """
    获取有效的用户输入
    Args:
        prompt: 输入提示信息
        min_val: 最小值
        max_val: 最大值
    Returns:
        int: 用户输入的有效整数
    """
    while True:
        try:
            user_input = int(input(prompt))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"❌ 请输入{min_val}到{max_val}之间的数字！")
        except ValueError:
            print("❌ 请输入一个有效的数字！")


def get_difficulty_level():
    """
    获取游戏难度级别
    Returns:
        tuple: (数字范围, 最大尝试次数, 难度名称)
    """
    print("\n🎯 请选择游戏难度：")
    print("1. 简单模式：1-50，最多10次机会")
    print("2. 普通模式：1-100，最多7次机会")
    print("3. 困难模式：1-200，最多5次机会")
    
    choice = get_valid_input("请选择难度 (1-3): ", 1, 3)
    
    if choice == 1:
        return 50, 10, "简单"
    elif choice == 2:
        return 100, 7, "普通"
    else:
        return 200, 5, "困难"


def play_game():
    """主游戏逻辑"""
    # 获取游戏难度设置
    max_num, max_attempts, difficulty = get_difficulty_level()
    
    # 生成随机数字
    secret_number = random.randint(1, max_num)
    
    print(f"\n🎲 {difficulty}模式已开始！")
    print(f"📊 数字范围：1-{max_num}，最多{max_attempts}次机会")
    print("🚀 开始猜数字吧！\n")
    
    # 记录游戏数据
    attempts = 0
    guessed_numbers = []  # 记录已猜过的数字
    start_time = time.time()  # 记录开始时间
    
    # 游戏主循环
    while attempts < max_attempts:
        attempts += 1
        
        # 显示当前状态
        print(f"🔢 第{attempts}次尝试 (剩余{max_attempts - attempts}次)")
        if guessed_numbers:
            print(f"💭 已猜过：{sorted(guessed_numbers)}")
        
        # 获取用户猜测
        guess = get_valid_input(f"请输入你猜的数字 (1-{max_num}): ", 1, max_num)
        
        # 检查是否重复猜测
        if guess in guessed_numbers:
            print("⚠️  你已经猜过这个数字了！")
            attempts -= 1  # 不计入尝试次数
            continue
        
        guessed_numbers.append(guess)
        
        # 判断猜测结果
        if guess == secret_number:
            # 猜对了！
            elapsed_time = time.time() - start_time
            print(f"\n🎉 恭喜你！猜对了！")
            print(f"🎯 答案就是：{secret_number}")
            print(f"📊 用时：{elapsed_time:.1f}秒，尝试次数：{attempts}")
            
            # 根据表现给出评价
            if attempts == 1:
                print("🏆 太厉害了！一次就猜中！")
            elif attempts <= max_attempts // 2:
                print("👍 表现很好！")
            else:
                print("💪 不错，坚持就是胜利！")
            
            return True  # 游戏胜利
            
        elif guess < secret_number:
            print("📈 你猜的数字太小了！往大了猜~")
        else:
            print("📉 你猜的数字太大了！往小了猜~")
        
        # 给出更精确的提示（当剩余次数较少时）
        if max_attempts - attempts <= 2:
            diff = abs(guess - secret_number)
            if diff <= 5:
                print("🔥 很接近了！")
            elif diff <= 10:
                print("🌡️  比较接近！")
            else:
                print("❄️  还差得远呢！")
        
        print("-" * 30)
    
    # 游戏失败
    print(f"\n💔 很遗憾，你没有猜中！")
    print(f"🎯 正确答案是：{secret_number}")
    print(f"💭 你猜过的数字：{sorted(guessed_numbers)}")
    return False  # 游戏失败


def show_game_stats(wins, losses):
    """显示游戏统计信息"""
    total_games = wins + losses
    if total_games > 0:
        win_rate = (wins / total_games) * 100
        print(f"\n📊 游戏统计：")
        print(f"🎮 总游戏次数：{total_games}")
        print(f"🏆 胜利次数：{wins}")
        print(f"💔 失败次数：{losses}")
        print(f"📈 胜率：{win_rate:.1f}%")


def main():
    """主程序"""
    # 显示欢迎信息
    display_welcome()
    
    # 游戏统计
    wins = 0
    losses = 0
    
    # 游戏主循环
    while True:
        try:
            # 开始游戏
            if play_game():
                wins += 1
            else:
                losses += 1
            
            # 询问是否继续
            print(f"\n🔄 是否继续游戏？")
            continue_game = input("输入 'y' 继续，其他任意键退出: ").lower().strip()
            
            if continue_game != 'y':
                break
                
            print("\n" + "="*44)
            
        except KeyboardInterrupt:
            print("\n\n👋 感谢游戏，再见！")
            break
        except Exception as e:
            print(f"\n❌ 游戏出现错误：{e}")
            break
    
    # 显示游戏统计
    show_game_stats(wins, losses)
    print("\n🎮 感谢参与猜数字小游戏！")
    print("👋 期待下次再见！")


if __name__ == "__main__":
    main()

# ===== 原版代码问题分析 =====
# 问题1: 重复调用input()导致用户需要输入多次
# 问题2: 没有循环机制，只能猜一次
# 问题3: 数字固定为5，没有随机性
# 问题4: 缺少输入验证和错误处理
# 问题5: 游戏体验较差，缺少互动性