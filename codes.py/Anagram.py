#Anagrams are strings that have the same no. of characters in the string and teh same length but the order of strings are different.
a = input("enter the string")
b = input("enter the string")
index = 0
result = 1
flag = 1
n1 = len(a)
n2 = len(b)
if(n1==n2):
    for x in a:
        if x not in b:
            flag=0
            break
    if flag == 1:
        print("string is anagram")
    else:
        print("not ")
