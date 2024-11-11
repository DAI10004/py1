import math

def is_prime(num):
    if num<2:
        return 0
    sqrt_num = int(math.sqrt(num))
    for i in range(2,sqrt_num+1):
        if num % i==0:
            return 0
    return 1

sum=0
primes=[]
for num in range(1,1001):
    if is_prime(num):
        primes.append(num)
        sum+=1
print(primes)
print("\n1到1000中素数的个数为：",sum)
