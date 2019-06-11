p=int(input("Enter p:"))
n= int(input("Enter n:"))
inc = int(input("Enter inc:"))
print("Year   Price")
for i in range(1, n+1):
    p= p + (p*inc/100)
    print(i, "     ",p)
    
