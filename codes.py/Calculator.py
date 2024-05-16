#Make a calculator

def add(a,b):
    x = a+b
    return x
def sub(a,b):
    x = a-b
    return x
def multiply(a,b):
    x = a*b
    return x
def divide(a,b):
    x = a/b
    return x
def exp(a,b):
    x= a**b

choice = 'Y'
while choice!= 'N':
    print("Select an operation.Choose N to exit")
    print("+")
    print("-")
    print("*")
    print("/")
    print("**")
    choice = input("Enter your choice")
    if choice == 'N':
        print("Bye! See you later!")
        break
    else:
        A = float(input("enter first number: "))
        B = float(input("enter second number: "))
        if choice == "+":
            print("A+B=:"+ add(A,B))
        elif choice == "-":
            print("A-B=:",sub(A,B))
        elif choice == "/":
            print("A/B=:",divide(A,B))
        elif choice == "**":
            print("A-B=:",exp(A,B))
        elif choice == "*":
            print("A*B=:",multiply(A,B))
        else:
            print("Invalid Input")
