# 47动物园门票购买系统 - 基于身高的票价计算
print("欢迎来到47动物园！")  # 显示欢迎信息

# 获取用户身高输入并转换为浮点数
身高 = float(input("请输入您的身高（单位：米）："))

# 使用多重条件判断确定票价
if 身高 < 0:  # 检查输入是否有效（身高不能为负数）
    print("❌ 身高不能为负数，请重新输入！")
elif 身高 < 1.2:  # 儿童票：身高1.2米以下免费
    print("您是儿童，免费入园！")
elif 身高 < 1.5:  # 青少年票：身高1.2-1.5米之间
    print("您是青少年，需付费20元入园！")
elif 身高 < 1.8:  # 成人票：身高1.5-1.8米之间
    print("您是成人，需付费50元入园！")
elif 身高 < 2.0:  # 高个子成人票：身高1.8-2.0米之间
    print("您是高个子成人，需付费70元入园！")
else:  # 巨人票：身高2.0米以上
    print("您是巨人，需付费100元入园！")        

print("祝您游玩愉快！")  # 显示祝福信息