import sys


# def factorial(n):
#     if(n<=1):
#         return 1
#     return n*factorial(n-1)

# result=factorial(5)
# print(result)


# def f(n=5):
#     if n <= 1:
#         return 1
#     f(n - 1)
#     print(n, end=" ")
#     f(n - 1)
#
#
# re = f()


# def sum(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         return num[0] + sum(num[1:])


# num = [1, 2, 3, 4, 5]

# re = sum(num)
# print(re)

def fib(num):
    if num<=1:
        return num
    else:
        return fib(num-1)+fib(num-2)
for i in range(10):
    print(fib(i))