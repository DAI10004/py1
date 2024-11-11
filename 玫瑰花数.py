def is_meiguihua(num):
    n=num
    sum=0
    digits=len(str(num))
    while n>0:
        digit=n%10
        sum+=digit**digits
        n //= 10
    return sum==num
sum=0
meiguihuas=[]
for num in range(1000,10000):
    if is_meiguihua(num):
        meiguihuas.append(num)
        sum+=1

print("1000到9999之间的玫瑰花数有：")
print(meiguihuas)
print("1000到9999之间共有玫瑰花数：",sum)