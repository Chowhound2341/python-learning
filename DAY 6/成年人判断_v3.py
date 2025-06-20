# 47游乐园智能门票系统 v3.0 - 深度优化版
import datetime
import json
import os
from typing import Dict, Tuple, List, Optional
from dataclasses import dataclass
from enum import Enum


class TicketType(Enum):
    """门票类型枚举"""
    INFANT = "婴幼儿"
    CHILD = "儿童"
    STUDENT = "学生"
    ADULT = "成人"
    SENIOR = "老人"
    DISABLED = "残疾人"


@dataclass
class TicketInfo:
    """门票信息数据类"""
    age: int
    ticket_type: TicketType
    base_price: float
    discount: float = 0.0
    final_price: float = 0.0
    special_notes: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.special_notes is None:
            self.special_notes = []
        self.final_price = self.base_price * (1 - self.discount)


class TicketSystem:
    """47游乐园门票系统"""
    
    def __init__(self):
        self.ticket_prices = {
            TicketType.INFANT: 0,
            TicketType.CHILD: 0,
            TicketType.STUDENT: 30,
            TicketType.ADULT: 68,
            TicketType.SENIOR: 34,
            TicketType.DISABLED: 0
        }
        
        self.visit_history = []
        self.daily_stats = {"total_visitors": 0, "total_revenue": 0.0}
        
    def get_valid_age(self) -> int:
        """获取有效的年龄输入"""
        while True:
            try:
                age_input = input("请输入您的年龄：").strip()
                age = int(age_input)
                
                if age < 0:
                    print("❌ 年龄不能为负数，请重新输入！")
                    continue
                elif age > 150:
                    print("⚠️  年龄输入过大，请确认是否正确！")
                    confirm = input("继续使用此年龄？(y/n): ").lower()
                    if confirm != 'y':
                        continue
                        
                return age
                
            except ValueError:
                print("❌ 请输入有效的数字！")
    
    def check_special_status(self) -> Tuple[bool, bool]:
        """检查特殊身份状态"""
        print("\n🎓 身份验证：")
        
        # 学生证检查
        is_student = False
        student_input = input("您是否持有有效学生证？(y/n): ").lower().strip()
        if student_input == 'y':
            is_student = True
            print("✅ 学生身份已确认！")
        
        # 残疾证检查
        is_disabled = False
        disabled_input = input("您是否持有残疾证？(y/n): ").lower().strip()
        if disabled_input == 'y':
            is_disabled = True
            print("✅ 残疾人身份已确认，享受免费政策！")
            
        return is_student, is_disabled
    
    def determine_ticket_type(self, age: int, is_student: bool, is_disabled: bool) -> TicketType:
        """根据年龄和身份确定门票类型"""
        if is_disabled:
            return TicketType.DISABLED
        elif age < 3:
            return TicketType.INFANT
        elif age < 18:
            return TicketType.CHILD
        elif age < 25 and is_student:
            return TicketType.STUDENT
        elif age < 60:
            return TicketType.ADULT
        else:
            return TicketType.SENIOR
    
    def apply_special_discounts(self, ticket_info: TicketInfo) -> TicketInfo:
        """应用特殊折扣"""
        current_time = datetime.datetime.now()
          # 工作日折扣（周一到周四）
        if current_time.weekday() < 4:  # 0-6 代表周一到周日
            if ticket_info.ticket_type == TicketType.ADULT:
                ticket_info.discount += 0.1
                if ticket_info.special_notes is not None:
                    ticket_info.special_notes.append("工作日优惠：9折")
        
        # 早鸟优惠（上午10点前）
        if current_time.hour < 10:
            if ticket_info.base_price > 0:
                ticket_info.discount += 0.05
                if ticket_info.special_notes is not None:
                    ticket_info.special_notes.append("早鸟优惠：额外5%折扣")
        
        # 节假日涨价（周末）
        if current_time.weekday() >= 5:  # 周六日
            if ticket_info.ticket_type in [TicketType.ADULT, TicketType.STUDENT]:
                ticket_info.base_price *= 1.2
                if ticket_info.special_notes is not None:
                    ticket_info.special_notes.append("周末票价：+20%")
        
        # 重新计算最终价格
        ticket_info.final_price = ticket_info.base_price * (1 - ticket_info.discount)
        
        return ticket_info
    
    def generate_ticket(self, age: int) -> TicketInfo:
        """生成门票信息"""
        is_student, is_disabled = self.check_special_status()
        ticket_type = self.determine_ticket_type(age, is_student, is_disabled)
        base_price = self.ticket_prices[ticket_type]
        
        ticket_info = TicketInfo(
            age=age,
            ticket_type=ticket_type,
            base_price=base_price
        )
        
        # 应用特殊折扣
        ticket_info = self.apply_special_discounts(ticket_info)
        
        return ticket_info
    
    def display_ticket(self, ticket_info: TicketInfo) -> None:
        """显示门票信息"""
        print("\n" + "🎫" + "=" * 50 + "🎫")
        print("🎪           47游乐园电子门票           🎪")
        print("=" * 52)
        
        current_time = datetime.datetime.now()
        ticket_id = f"47-{current_time.strftime('%Y%m%d')}-{len(self.visit_history)+1:04d}"
        
        print(f"🆔 票号：{ticket_id}")
        print(f"👤 年龄：{ticket_info.age}岁")
        print(f"🎭 类别：{ticket_info.ticket_type.value}")
        print(f"📅 日期：{current_time.strftime('%Y年%m月%d日 %H:%M')}")
        
        if ticket_info.base_price == 0:
            print("💰 票价：🆓 免费入园")
        else:
            print(f"💰 原价：¥{ticket_info.base_price:.0f}")
            if ticket_info.discount > 0:
                print(f"🎁 折扣：{ticket_info.discount*100:.0f}%")
                print(f"💳 实付：¥{ticket_info.final_price:.0f}")
            else:
                print(f"💳 票价：¥{ticket_info.final_price:.0f}")
        
        # 显示特殊说明
        if ticket_info.special_notes:
            print("📝 优惠详情：")
            for note in ticket_info.special_notes:
                print(f"   • {note}")
        
        print("=" * 52)
        
        # 添加二维码效果（用ASCII艺术模拟）
        print("📱 请出示此票据入园：")
        self.display_qr_code()
        
    def display_qr_code(self) -> None:
        """显示ASCII二维码艺术"""
        qr_art = [
            "██████████████    ██  ██████████████",
            "██          ██  ████  ██          ██",
            "██  ██████  ██    ██  ██  ██████  ██",
            "██  ██████  ██  ██    ██  ██████  ██",
            "██  ██████  ██    ██  ██  ██████  ██",
            "██          ██  ████  ██          ██",
            "██████████████  ██  ██████████████",
            "                ██                  ",
            "██  ██    ██████    ██    ██  ████  ",
            "    ██████    ██  ████████  ██    ██",
            "██    ██  ██████    ██  ██    ██████",
            "██████████████  ██    ██████    ██  ",
            "██          ██    ██    ██  ████    ",
            "██  ██████  ██  ██████████    ██████",
            "██  ██████  ██      ██    ██████  ██",
            "██  ██████  ██  ██  ██████    ██    ",
            "██          ██    ████  ██████  ████",
            "██████████████    ██    ██  ██    ██"
        ]
        
        for line in qr_art:
            print(f"   {line}")
        print()
    
    def save_visit_record(self, ticket_info: TicketInfo) -> None:
        """保存访问记录"""
        visit_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "age": ticket_info.age,
            "ticket_type": ticket_info.ticket_type.value,
            "price": ticket_info.final_price,
            "discounts": ticket_info.special_notes
        }
        
        self.visit_history.append(visit_record)
        self.daily_stats["total_visitors"] += 1
        self.daily_stats["total_revenue"] += ticket_info.final_price
    
    def display_welcome_info(self) -> None:
        """显示欢迎信息"""
        print("🎠" + "=" * 50 + "🎠")
        print("🎪        欢迎来到47游乐园！        🎪")
        print("🎠" + "=" * 50 + "🎠")
        
        current_time = datetime.datetime.now()
        weather_emoji = "☀️" if current_time.hour < 18 else "🌙"
        
        print(f"{weather_emoji} 今天是{current_time.strftime('%Y年%m月%d日')} {self.get_weekday_name(current_time.weekday())}")
        print(f"⏰ 当前时间：{current_time.strftime('%H:%M')}")
        
        print("\n💰 票价说明：")
        print("   🍼 0-2岁婴幼儿：免费")
        print("   👶 3-17岁儿童：免费")
        print("   🎓 18-24岁学生：¥30（需学生证）")
        print("   👔 18-59岁成人：¥68")
        print("   👴 60岁以上老人：¥34")
        print("   ♿ 残疾人士：免费（需残疾证）")
        
        print("\n🎁 优惠政策：")
        print("   📅 工作日成人票9折")
        print("   🌅 早鸟优惠（10点前）额外5%折扣")
        print("   📈 周末票价上浮20%")
        
        print("-" * 54)
    
    def get_weekday_name(self, weekday: int) -> str:
        """获取星期名称"""
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        return weekdays[weekday]
    
    def display_park_info(self) -> None:
        """显示园区信息"""
        print("\n🎪 园区信息：")
        print("🕐 开园时间：08:00 - 22:00")
        print("🎢 热门项目：过山车、摩天轮、激流勇进")
        print("🍔 餐饮服务：美食广场、主题餐厅")
        print("🚗 停车信息：免费停车位充足")
        print("📞 客服热线：400-047-047")
        
    def run(self) -> None:
        """运行门票系统"""
        try:
            self.display_welcome_info()
            
            # 获取年龄
            age = self.get_valid_age()
            
            # 生成门票
            ticket_info = self.generate_ticket(age)
            
            # 显示门票
            self.display_ticket(ticket_info)
            
            # 保存记录
            self.save_visit_record(ticket_info)
            
            # 显示感谢信息
            print("🎉 购票成功！祝您在47游乐园玩得愉快！")
            print("🛡️  安全提醒：请遵守园区规定，注意人身安全！")
            
            # 显示园区信息
            self.display_park_info()
            
            # 询问是否需要更多服务
            self.additional_services()
            
        except KeyboardInterrupt:
            print("\n\n👋 感谢您的光临，期待下次再见！")
        except Exception as e:
            print(f"\n❌ 系统错误：{e}")
            print("🔧 请联系客服或重新尝试")
    
    def additional_services(self) -> None:
        """额外服务"""
        print(f"\n🔄 是否需要其他服务？")
        print("1. 查看今日统计")
        print("2. 购买更多门票") 
        print("3. 退出系统")
        
        choice = input("请选择 (1-3): ").strip()
        
        if choice == "1":
            self.show_daily_stats()
        elif choice == "2":
            print("\n" + "="*54)
            self.run()
        elif choice == "3":
            print("👋 感谢使用47游乐园门票系统！")
        else:
            print("无效选择，系统即将退出...")
    
    def show_daily_stats(self) -> None:
        """显示今日统计"""
        print(f"\n📊 今日园区统计：")
        print(f"👥 总访客数：{self.daily_stats['total_visitors']} 人")
        print(f"💰 总收入：¥{self.daily_stats['total_revenue']:.0f}")
        if self.daily_stats['total_visitors'] > 0:
            avg_price = self.daily_stats['total_revenue'] / self.daily_stats['total_visitors']
            print(f"📈 平均票价：¥{avg_price:.0f}")


def main():
    """主程序"""
    ticket_system = TicketSystem()
    ticket_system.run()


if __name__ == "__main__":
    main()


# ===== 原版代码（保留）=====
# print("欢迎来到47游乐园，儿童免费入园，成人需付费！")
# age = int(input("请输入你的年龄："))
# if age < 18:
#     print("您是儿童，免费入园！")
# elif age >= 18:
#     print("您是成人，需付费入园！")
# print("祝您游玩愉快！")
