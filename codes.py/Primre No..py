x = int(input("enter the no."))
flag = True
for y in range(2,x):
    if x%y  == 0:
        flag = False
        break
        # print ("The no. is a prime no.")

if(flag):
    print("prime")
else:
    print("not prime")
