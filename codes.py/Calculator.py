def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
choice = 'y'
while(choice != "n"):
    print ("select an operation. Press n to exit")
    print("+")
    print("-")
    print("*")
    print("/")
    print("n")
    choice = input("select operator to use:")
    if choice == "n":
        print("Bye")
        break
    A = float(input("enter first number: "))
    B = float(input("enter second number: "))
    if choice == '+':
        print(A,"+",B,"=", add(A,B))
    elif choice == '-':
        print(A,"-",B,"=", sub(A,B))
    elif choice ==  '/':
        if B == 0:
            print("Not defined")
        else:
            print(A,"/",B,"=", divide(A,B))
    elif choice == "*":
        print(A,"*",B,"=", multiply(A,B))
    else:
        print("INVALID INPUT")
    
