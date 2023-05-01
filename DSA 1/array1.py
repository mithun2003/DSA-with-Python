# exp = [2200,2350,2600,2130,2190]


# print("Money spent in feb compare to jan : ",exp[1]-exp[0])


# print("Total expense in first three months : ",exp[0]+exp[1]+exp[2])


# for i in range(len(exp)):
#     if exp[i]==2000:
#         print("Month is",i+1)
# print("Not found")

# print("Did spend 2000 dollar in any month : ",2000 in exp)

# exp.append(1980)
# print(exp)

# exp[3] = exp[3]-200
# print("The updated expenditure : ",exp)

# def reverse(arr):
#     rev=[]
#     for i in range(len(arr)):
#         print(arr[i])
#     for i in range(len(arr)-1,-1,-1):
#         rev.append(arr[i])
#     for i in range(len(rev)):
#         print(rev[i],end=" ")

def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


arr = [i for i in range(1, 21)]
print(reverse(arr))


def reverse_string(a):
    rev = ""
    for i in range(len(a)-1, -1, -1):
        rev += a[i]
    print(rev)


a = "Mithun"
reverse_string(a)
