ls=[12,0,10,9,8,-1,21,-6]
for j in range(len(ls)-1):
    for i in range(len(ls)-j-1):
        if (ls[j]<ls[j+i+1]):
            tmp=ls[j]
            ls[j]=ls[j+i+1]
            ls[j+i+1]=tmp
print(ls)
