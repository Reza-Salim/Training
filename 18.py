a = int (input("Enter 1st:"))
b = int(input("Enter 2sd:"))
c = int(input("Enter 3rd:"))
if a>b :
    temp= a
    a = b
    b= temp
if a>c:
    temp = a
    a = c
    c = temp
if b>c :
    temp = b
    b = c
    c = temp
print ("Sorted is ", a, b, c)
