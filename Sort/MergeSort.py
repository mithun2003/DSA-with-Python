def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    firsthalf = arr[:mid]
    secondhalf=arr[mid:]
    return join(mergeSort(firsthalf),
    mergeSort(secondhalf))
def join(first,second):
    i=j=0
    newarray=[]
    while i<len(first) and j<len(second):
        if first[i]<=second[j]:
            newarray.append(first[i])
            i+=1
        else:
            newarray.append(second[j])
            j+=1
    while i<len(first):
        newarray.append(first[i])
        i+=1
    while j<len(second):
        newarray.append(second[j])
        j+=1
    return newarray
            
print(mergeSort([2,5,1,5,-3,7,3,56,53,99]))