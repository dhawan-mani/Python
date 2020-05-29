var = input("enter  binary")[::-1]
result = 0
index = 0
for x in var:
    if x == '1':
        result = result + 2**index
    index = index + 1
print(result)

or
    Var = input("enter the binary")
length = len(Var)-1
result = 0
for x in Var:
    if x == '1':
        result = result + 2**length
    length = length-1
print(result)
