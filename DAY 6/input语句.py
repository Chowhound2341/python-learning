# 欢迎登陆小程序 - 优化版
import time


def get_user_info():
    """获取用户信息"""
    print("=" * 50)
    print("🎉 欢迎使用登录系统 🎉")
    print("=" * 50)
    
    # 获取用户名，添加输入验证
    while True:
        user_name = input("请输入您的用户名: ").strip()
        if user_name:  # 检查是否为空
            break
        print("❌ 用户名不能为空，请重新输入！")
    
    # 提供用户类型选择
    print("\n请选择您的用户类型:")
    print("1. VIP会员")
    print("2. 普通会员") 
    print("3. 体验用户")
    print("4. 自定义")
    
    user_types = {
        "1": "VIP会员",
        "2": "普通会员", 
        "3": "体验用户"
    }
    
    while True:
        choice = input("请输入选项编号(1-4): ").strip()
        if choice in user_types:
            user_type = user_types[choice]
            break
        elif choice == "4":
            user_type = input("请输入自定义用户类型: ").strip()
            if user_type:
                break
            print("❌ 用户类型不能为空！")
        else:
            print("❌ 无效选项，请输入1-4之间的数字！")
    
    return user_name, user_type


def welcome_message(user_name, user_type):
    """显示欢迎消息"""
    print("\n" + "🌟" * 20)
    print("正在为您登录...")
    
    # 添加模拟加载效果
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    
    print("\n")
    
    # 使用 f-string 格式化（更现代的方式）
    print(f"✨ 您好，{user_name}！")
    print(f"🎭 您是尊贵的 {user_type}，欢迎您的光临！")
    
    # 根据用户类型显示不同权限
    privileges = {
        "VIP会员": ["享受专属服务", "优先客服支持", "专属折扣"],
        "普通会员": ["基础服务", "标准客服支持"],
        "体验用户": ["基础试用功能"]
    }
    
    if user_type in privileges:
        print(f"🎁 您享有以下特权:")
        for privilege in privileges[user_type]:
            print(f"   • {privilege}")
    
    print("🌟" * 20)


def main():
    """主程序"""
    try:
        # 获取用户信息
        user_name, user_type = get_user_info()
        
        # 显示欢迎消息
        welcome_message(user_name, user_type)
        
        # 询问是否继续
        print(f"\n{user_name}，感谢您的使用！")
        
    except KeyboardInterrupt:
        print("\n\n👋 感谢使用，再见！")
    except Exception as e:
        print(f"\n❌ 系统错误: {e}")


if __name__ == "__main__":
    main()


# ===== 原版代码（保留作为对比）=====
# user_name = input("您好，请输入用户名：")
# user_type = input("您是尊贵的：")
# print("您好： %s, 您是尊贵的%s用户，欢迎您的光临！"% (user_name, user_type))