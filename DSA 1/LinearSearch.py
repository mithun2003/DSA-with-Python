from random import randint


def linerSearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return("Number found at "+str(i+1)+" position")
    return("The number is not found")


arr = []
for i in range(100):
    arr.append(randint(1, 100))
print(arr)

print(linerSearch(arr, 72))
