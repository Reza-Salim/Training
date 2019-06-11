id1 = -1
max1 = -1
max2 = -1
id2 = -1
n = 0
while n < 2:   
    print ("Please enter a number greater than 1")
    n = int(input("Enter n : "))
    
else:
    for i in range (1, n+1):
        id0 = int(input("Enter id: "))
        aver = float(input("Enter average: "))
        if aver > max1:
            id2 = id1
            max2 = max1
            max1 = aver
            id1 = id0
        else:
            if aver>max2:
                max2=aver
                id2=id0
    print ("Max2 = ", max2,"\t\tId2 =", id2)
            
