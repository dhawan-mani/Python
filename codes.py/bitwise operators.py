choice = 'y'
while( choice != 'n'):
    a = int(input("enter the first no."))
    b = int(input("enter the second no."))
    c = input("enter the operator")
    if c == '&':
        print(a&b)
    elif c == '|':
        print(a|b)
    elif c == '~':
        print(~a)
        print(~b)
    elif c == '>>':
        print(a>>2)
        print(a>>2)
    else:
         print(a<<2)
         print(b<<2)
    choice = input("enter your choice")
else:
    print("BYE")
#it is important to avoid an infinite loop 
