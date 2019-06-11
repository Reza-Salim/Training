def cal(m1,m2,d):
    g = 6.673e-8
    return (g*m1*m2/po(d))
def po(d):
    return(d*d)
def main():
    m1= float(input("Enter m1: "))
    m2 = float(input("Enter m2: "))
    d= float(input("Enter d: "))
    print ("F is ", cal(m1,m2,d))
main()
