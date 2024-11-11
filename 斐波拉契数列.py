#规律：f(n)=f(n-1)+f(n-2)，f1=f2=1

#编程显示斐波拉契数列的前15个数
n = 0
m = 1
list = []
count = 0
while count < 15:
    list.append(n)
    temp = n + m
    n = m
    m = temp
    count += 1
print(list)