def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)


def insertionSort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while j>=0 and arr[j]>current:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current
    print(arr)
    
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)

def quickSort(arr,start,end):
    if start>=end:
        return 
    pivot = start
    left = start+1
    right=end
    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>arr[pivot]:
            right-=1
    
    arr[right],arr[pivot]=arr[pivot],arr[right]
    quickSort(arr,start,right-1)
    quickSort(arr,right+1,end)
    return arr

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    first=arr[0:mid]
    last=arr[mid:len(arr)]
    return join(mergeSort(first),mergeSort(last))
def join(first,last):
    i=j=0
    newarray=[]
    while i<len(first) and j<len(last):
        if first[i]<=last[j]:
            newarray.append(first[i])
            i+=1
        else:
            newarray.append(last[j])
            j+=1
    while i<len(first):
        newarray.append(first[i])
        i+=1
    while j<len(last):
        newarray.append(last[j])
        j+=1
    return newarray
arr=[9,5,3,7,0,2]
print(mergeSort(arr))