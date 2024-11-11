'''
'n'=n-(n/2+1)
now n =last n -(last n/2+1)
last n = (now n+1)*2
'''

days = int(input("请输入天数："))
total_peaches = 1
for _ in range(days - 1):
    total_peaches = (total_peaches + 1) * 2
print(f"最初有 {total_peaches} 个桃子。")
