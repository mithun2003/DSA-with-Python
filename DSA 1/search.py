arr=[1,2,3,4,5,6,7,8,9]
num=8
n=len(arr)
start = 0
end=n-1
while start<=end:
    mid=start+end//2
    if arr[mid]==num:
        print(mid)
    elif arr[mid]>num:
        start=mid+1
    elif arr[mid]<num:
        end = mid-1
    else:
        print("Not found")
        
    