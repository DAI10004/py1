from turtle import TurtleGraphicsError

ls=[12,0,78,66,-2,10,9,8,-1,21,-61]
def bubble_sort(arr):
    n=len(arr)
    for j in range(n):
        swapped =False
        for i in range(n-j-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped =True
        if not swapped:
            break
    return arr
sort=bubble_sort(ls)
print(sort)

