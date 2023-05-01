# # find the sum of digits using recursion
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number must be positive"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(n//10)


print(sum_of_digits(4444444444))


# find the square of numbers using recursion
# def square(base,exp):
#     if exp==0:
#         return 0
#     if exp==1:
#         return base
#     else:
#         return base*square(base,exp-1)
# res=square(2,5)
# print(res)


# greatest common divisor
# def gcd(num1, num2):
#     if num1 < 0:
#         num1 = -1*num1
#     if num2 < 0:
#         num2 = -1*num2
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1 % num2)
# print(gcd(18, 48))


# decimal to binary

# def binary(n):
#     if n//2==0:
#         return n
#     else:
#         return n%2+10*binary(n//2)
# print(binary(13))
