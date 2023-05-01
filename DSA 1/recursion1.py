#Find the sum of n +ve interger numbers using recursion

def pos_sum(n):
    assert n>=0 and int(n)==n,"The input number must be a positive number"
    if n in [0,1]:
        return n
    else:
        return n+pos_sum(n-1)
print(pos_sum(9))