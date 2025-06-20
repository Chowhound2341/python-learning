print("🎠" + "=" * 40 + "🎠")
print("🎪   欢迎来到47游乐园！   🎪")
print("🎠" + "=" * 40 + "🎠")
print("💰 票价说明：")
print("   • 3岁以下婴幼儿：免费")
print("   • 3-17岁儿童：免费") 
print("   • 18-59岁成人：50元")
print("   • 60岁以上老人：半价25元")
print("-" * 44)

age = int(input("请输入你的年龄："))
if age < 0:
    print("❌ 年龄不能为负数，请重新输入！")
elif age > 150:
    print("❌ 年龄输入过大，请重新输入！")
elif age < 3:
    print("您是婴幼儿，免费入园！")
elif age < 18:
    print("您是儿童，免费入园！")
elif age < 60:
    print("您是成人，需付费50元入园！")
else:
    print("您是老人，享受半价25元入园！")

print("祝您游玩愉快！")