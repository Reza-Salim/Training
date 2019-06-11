while True:
    m = int(input("Enter m:"))
    tedad = int(input("Enter tedad :"))
    s = int(input("Enter s:"))
    k = (12*m)/(12-tedad*s/100)
    p = k / tedad
    print("k = ", k, '\t', p)
    ansi = input("Do you want to continue(y/n):")
    if ansi[0] == 'n' or ansi[0] == 'N':
        break
    
