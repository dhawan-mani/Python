string = input("Enter the string fore palindrome")
def is_palindrome(s):
    s =''.join(x.lower() for x in s if x.isalnum())
    if s == s[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
is_palindrome(string)
