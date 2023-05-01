#1st way
def twoSum(nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return num[i],num[j]
        return -1
num = [1,2,3,4,5,8]

res = twoSum(num,7)
print(res)


#2ndway
def twoSum(num,t):
    s=set()
    for i in range(0,len(num)):
        val = num[i]
        match = t-val
        if match in s:
            return val,match
        else:
            s.add(val)
    return 0

num = [1,5,5,4,5,8]
res = twoSum(num,10)
print(res)