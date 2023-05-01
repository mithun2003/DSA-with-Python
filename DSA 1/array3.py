# def oddnum(n):
#     for i in range(1,n+1,2):
#         print(i)
# oddnum(16)

#Get the average temperature of n days as given input

days = int(input("How many days temperature ? "))
arr=[]
total = 0
above = 0
if days<=0:
    print("the number must be +ve")
else:
    for i in range(0,days):
        temp = int(input(str(i+1)+"day's temp : "))
        arr.append(temp)
        total +=arr[i]
    avg=round(total/days,2)
    print("Average temperature is "+str(avg))
for i in arr:
    if i>avg:
        above += 1
print(str(above)+" day(s) above the average")











#Linear Search
# def linearSearch(arr,num):
#     for i in range(len(arr)):
#         if arr[i] == num:
#             return("Number found at "+str(i+1)+" position")
#     return("Number not found")
# arr = [i for i in range(50)]
# print(linearSearch(arr,99))























#Binary Search with iterative method
# def binarySearch(arr,num):
#     left = 0
#     right= len(arr)-1
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid]==num:
#             return ("Number found at "+str(mid+1)+" position")
#         elif num>arr[mid]:
#             left=mid+1
#         else:
#             right = mid-1
            
#     return("Number not found")

# arr = [i for i in range(1,51)]
# print(binarySearch(arr,34))












#Binary Search with recursive method
# def binarySearch(arr,num,left,right):
#     mid = (left+right)//2
#     if arr[mid]==num:
#         return ("Number found at "+str(mid+1)+" position")
#     elif num>arr[mid]:
#         return binarySearch(arr,num,mid+1,right)
#     else:
#         return binarySearch(arr,num,left,mid-1)            
# arr = [i for i in range(1,51)]
# print(binarySearch(arr,29,0,len(arr)-1))
