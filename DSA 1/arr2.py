# import array
# def change(arr,t):
#     for i in range(0,len(arr)):
#         for j in range(len(arr)-1,i,-1):
#           if arr[j]!= t:
#               if arr[i]==t:
#                   temp = arr[i]
#                   arr[i]=arr[j]
#                   arr[j]=temp
#     return arr

    
# test = array.array('i',[1,2,3,4,3,3,5,5,6,6,5,4,5])
# target = 5
# result=change(test,target)
# print(result)



# t = int(input())
# for i in range(t):
#     N = int(input())
#     A = []
#     for i in range(N):
#         A.append(i)
#     #print the array A
#     print(A)              
#     #print only the elements from array A
#     print(*A)               
#     A.sort(reverse=True)
#     #print the array A sorted in descending order
#     print(A)                

def innersum(arr):
    n=len(arr)
    new=[]
    i=0
    # for i in range(n//2):
    #     if arr[i]==arr[n-i-1]:
    #         break
    #     if arr[i]!=arr[n-i-1]:
    #         new.append(arr[i]+arr[n-i-1])
    # if arr[i]==arr[n-i-1]:
    #     new.append(arr[i])
    #     print(arr[i],arr[n-i-1])
    while i<n//2:
        if arr[i]!=arr[n-i-1]:
            new.append(arr[i]+arr[n-i-1])
        i+=1
    if arr[i]==arr[n-i-1]:
        new.append(arr[i])
        print(arr[i],arr[n-i-1])
    print(new)
arr=[1,2,3,4,5,6,7]
innersum(arr)