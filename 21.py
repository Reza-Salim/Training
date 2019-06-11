x = int(input("Enter the x:"))
sum = 0
for i in range(1,11):
    s = 1/x -(1/(x+2*x))
    x +=1
    print ("\nTerm",s)
    sum +=s
print ("\nSum: ",sum)
