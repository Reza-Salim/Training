def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def pow (x,n):
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)
def main():
    sign =1
    su =0
    x = float(input("Enter x:"))
    y = int(input("Enter n:"))
    for i in range (1, y+1,2):
        su += sign * pow(x,i)/ fact(i)
        sign = - sign
    print("Sin(", x, ") = ", su)

main()
        
