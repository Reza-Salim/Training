m = int(input("Enter n: "))
n = int(input("Enter m: "))
su = 0
temp = m
for i in range (1 , n):
    su = 0 
    for j in range (1,m+1):
        su +=temp
    temp = su
print(m,"^",n,"=", su)
