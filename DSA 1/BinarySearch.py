# def binarySearch(arr,num):
#     start = 0
#     end = len(arr)-1
#     while start<=end:
#         mid=(start+end)//2
#         if arr[mid]==num:
#             return("Number found at "+str(mid+1)+" position")
#         elif arr[mid]>num:
#             end = mid-1
#         elif arr[mid]<num:
#             start = mid+1
#     return("Number not found")
# arr=[1,2,3,4,5,6,7,8,9]
# print(binarySearch(arr,9))

def binarySearch(arr,num,start,end):
    mid=(start+end)//2
    if num not in arr:
        return("Number not found")
    if arr[mid]==num:
        return("Number found at "+str(mid+1)+" position")
    elif arr[mid]>num:
        return binarySearch(arr,num,start,mid-1)
    elif arr[mid]<num:
        return binarySearch(arr,num,mid+1,end)
    else:
        return("Number not found")
arr=[1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,1,0,len(arr)-1))
