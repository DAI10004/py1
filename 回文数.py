def is_huiwenshu(num):
    s=str(num)
    if s ==s[::-1]:
        return 1
    else:
        return 0
sum=0
for i in range(10000,100000):
    if is_huiwenshu(i):
        print(i)
        sum+=1
print(f"10000-99999之间的回文数个数为：{sum}")
