def w(v,t):
    if t <= 10:
        return (33-(10* sqr(v)-v +10.5)*(33-t)/(23.1))
    else:
                print("Invalid Temperature!")
def sqr(x):
    return pow(x,0.5)
v = float(input("Enter Velocity : "))
t = float(input("Enter Temperature : "))
print (w(v,t))
                
    
