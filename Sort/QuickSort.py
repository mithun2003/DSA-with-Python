def quickSort(arr, start, end):
    if start >= end:
        return arr
    left = start + 1
    right = end
    pivot = start
    while left <= right:
        while arr[left] <= arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)

    return arr


arr = [324, 53, 42, 66, 7, 46, 4, 542, 452,
       5234, 4, 55, 5, 4254, 5354, 5345, 25]
res = quickSort(arr, 0, len(arr) - 1)
print(res)
# arr=[324,53,42,66,7,46,4,67,57,6,53,2,3,56,43,52,53,6,24,33,452,4]
# res=quickSort(arr,0,len(arr)-1)
# print(res)
