#定义变量
name = "九曜博客"
stock_price = 21.37
stock_code = "040731"
stock_price_daily_growth_factor = 1.2
growth_days = 7
#计算股票价格
finally_stock_price = stock_price * (stock_price_daily_growth_factor ** growth_days)
print(f"公司：{name}, 股票代码：{stock_code},当前股价：{stock_price}元")
print("每日增长系数：%.1f, 经过%d天后，股价达到了：%.2f元"% (stock_price_daily_growth_factor, growth_days, finally_stock_price))