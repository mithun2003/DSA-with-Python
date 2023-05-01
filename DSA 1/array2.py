# heros=['spider man','thor','hulk','iron man','captain america']

# print("length of the list : ",len(heros))

# heros.append('black panther')
# print("The new list is : ",heros)

# heros.remove('black panther')
# heros.insert(3,'black panther')
# print("The new list : ",heros)


# heros[1:3]=['doctar strange']
# print(heros)

# heros.sort()
# print(heros)
# memo = {}

# def fib(n):
#     if n in memo:
#         return memo[n]
#     if n==0:
#         result=0
#     elif n <= 2:
#         result = 1
#     else:
#         result = fib(n-1) + fib(n-2)
#     print(memo)
#     memo[n] = result
#     return result
# print(fib(5))

# def is_even(n):
#     if n == 0:
#         return True
#     else:
#         print(n-1)
#         return is_odd(n-1)

# def is_odd(n):
#     if n == 0:
#         return False
#     else:
#         return is_even(n-1)
# print(is_even(900))

def getStrongest(arr, k):
    arr.sort()
    n = len(arr)
    m = arr[(n-1)//2]
    print(m)
    result = []
    for i in range(n):
        for j in range(n-1,-1,-1):
            a = abs(arr[i]-m)
            b = abs(arr[j]-m)
            if a>b or (a==b and arr[i]>arr[j]):
                result.append(arr[i]) 
            else:
                result.append(arr[j])
                
            # elif abs(arr[i]-m )<abs(arr[j]-m):
            #     result.append(arr[j])
    print(result)


arr = [6,7,11,7,6,8]
print(getStrongest(arr, 2))
