def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

ls = [
    [12, 0, 8, 9, 6, 1, 21, 46],
    [3, 88, -2, 90, 100],
    [6, -3, 9, 12, 44, 0, 50, 70, -23, 8]
]

sort1 = insert_sort(ls[0])
print(sort1)
sort2 = insert_sort(ls[1])
print(sort2)
sort3 = insert_sort(ls[2])
print(sort3)