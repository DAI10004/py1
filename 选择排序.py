ss=[12,0,78,66,-2,10,9,8,-1,21,-61]
def sort(ls):
    n=len(ls)
    for i in range(n):
        for j in range(n-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
ls=sort(ss)
print(ls)



