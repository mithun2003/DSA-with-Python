def selectionSort(arr):
    for i in range(len(arr)):
        sm = i
        for j in range(i+1, len(arr)):
            # print(arr[sm])
            # print(arr)
            if arr[j] < arr[sm]:
                sm = j
        arr[i], arr[sm] = arr[sm], arr[i]
    print(arr)


selectionSort([324, 53, 42, 66, 7, 46, 4, 542, 452,
              5234, 4, 55, 5, 4254, 5354, 5345, 25])
