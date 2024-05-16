#Anagrams are strings that have the same no. of characters in the string and teh same length but the order of strings are different.
a = input("enter the string")
b = input("enter the string")
def is_anagram(str1,str2):
    str1= str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if sorted(str1) == sorted(str2):
        print("Hurray!! It's anagram!!")
    else:
        print("Dang!! It's Not!")
is_anagram(a,b)
