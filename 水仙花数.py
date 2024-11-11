def is_shuixianhua_number(num):
    numbers = [int(n) for n in str(num)]
    m = len(numbers)
    if m!=3:
        return 0
    elif sum(n**3 for n in numbers) == num:
        return 1

num = int(input("请输入想要判断的数字："))
sxh = is_shuixianhua_number(num)
if sxh == 1:
    print(f"{num}是水仙花数。")
else:
    print(f"{num}不是水仙花数。")