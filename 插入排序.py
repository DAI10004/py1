ls=[12,0,78,66,-2,10,9,8,-1,21,-61]
def insert_sort(arr):
    for i in range(1,len(ls)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
sort=insert_sort(ls)
print(sort)
