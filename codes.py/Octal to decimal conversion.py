var = input("enter the octal no.")[::-1]
result = 0
index = 0
for x in var:
    if x not in ["0","1","2","3","4","5","6","7"]:
        break
    else:
        result = result + int(x)*8**index
    index = index + 1
print(result)
