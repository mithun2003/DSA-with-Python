# def string(string,x):
#     key = x%26
#     print(key)
#     result =""
#     for i in range(0,len(string)):
#         num = ord(string[i])+key
#         if num <=122:
#             result +=chr(num)
#         else:
#             result+=chr(96+num%122)
#     print(result)
# string("aby",3)

def duplicates(a):
    s = set()
    char = {}
    for i in range(0, len(a)):
        if a[i] in s:
            char[a[i]] += 1
            print(a[i])
        else:
            char[a[i]] = 1
            s.add(a[i])
    for key, value in char.items():
        if value > 1:
            print(f"{key} occurs {value} times")


duplicates("hhello")

















def remove_vowels(string):
    vowels ="aeiouAEIOU"
    change=""
    for i in string:
        if i not in vowels:
            change+=i
            print(change) 
    return change

print(remove_vowels("mithun"))