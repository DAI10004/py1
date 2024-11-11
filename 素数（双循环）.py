sum=0
first = True
for j in range(2,1001):
    flag=1
    a=j
    for i in range(2,a):
        if (a%i ==0):
            flag = 0
            break

    if (flag==1):
        if not first:
            print(',',end='')
        print(a,end='')
        sum=sum+1
        first =False
    else:
        continue
print(f"\n1到1000中素数的个数为：{sum}")
