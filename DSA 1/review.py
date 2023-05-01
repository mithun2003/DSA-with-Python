def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)


def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    print(arr)


def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # print(arr)
    
    while True:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        # if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            break
        
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)
    return arr


arr = [324, 53, 42, 66, 7, 46, 4, 67, 57, 6, 53, 2, 3, 56, 43, 52, 53, 6, 24, 33, 452, 4]
quickSort(arr, 0, len(arr) - 1)
print(arr)
