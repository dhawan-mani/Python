var = input("enter the hexadecimal no.")[::-1]
result = 0
index = 0
flag = True
for x in var:
    if x not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
        flag = False
        break
    else:
        if x == 'A':
            x= 10
        elif  x == 'B':
            x = 11
        elif x == 'C':
            x = 12
        elif x == 'D':
            D = 13
        elif x == 'E':
            E = 14
        elif x == 'F':
            x = 15
        result = result + int(x)*16**index
    index = index + 1
if flag:
print(result)
