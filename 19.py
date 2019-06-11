n = int(input("Enter n:"))
i=1
while i<=n:
    id = int(input("Enter id:"))
    h = int(input("Enter h:"))
    hp = int(input("Enter hp:"))
    ov = 0
    if h>40:
        ov = 0.5*(h-40)*hp
    p = ov +hp*h
    print("id = ",id ,"  ov= ", ov , "p=" ,p)
    i +=1
