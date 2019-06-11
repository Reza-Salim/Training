

f = int(input("Foot?"))
i = int(input("Inch?"))
def calc():
    ftm = 0.3048 * f
    ftc = 100* ftm
    itm = (1/12)*0.3048*i
    itc = 100*itm
    print ("The  ",f ,"foot is ",ftm ,"meter")
    print ("The  ",f , "foot is ", ftc," centimeter")
    print("The ",i ," inch is ", itm , "meter")
    print ("The ", i ,"inch is ",itc ,"centimeter")
calc()


    
