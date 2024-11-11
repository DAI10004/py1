'''
显示未来N年内（N值从键盘输入）天文学闰年（年号之间用逗号隔开，10个一行），并统计个
数，支持再玩一次
#闰年分为普通闰年和世纪闰年，主要是为了解决每年365.24219天问题
#普通闰年：公历年份是4的倍数的，且不是100的倍数，为普通闰年
#比如：2004年、2020年就是普通闰年
#世纪闰年：公历年份是整百数的，必须是400的倍数才是世纪闰年
#比如：1900年不是世纪闰年，2000年是世纪闰年
'''
import datetime
#判断闰年函数
def is_leap_year(year):
    if year % 4 == 0 and year % 100!= 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
#查找年份
while True:
    try:
        n = int(input("请输入未来的年数："))
        current_year = datetime.datetime.now().year
        count = 0
        line_count = 0
        for year in range(current_year, current_year + n):
            if is_leap_year(year):
                print(year, end=', ')
                count += 1
                line_count += 1
                if line_count == 10:
                    print()#空行
                    line_count = 0#重置
        print(f"\n未来{n}年内共有{count}个闰年。")
        choice = input("是否再玩一次？（y/n）")
        if choice.lower()!= 'y':
            break
    except ValueError:
        print("请输入有效的整数。")