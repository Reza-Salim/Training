
po = 10
su = 0
num = int(input("Enter a number: "))
temp = num
while temp > 0:
    su = (po * su) + temp % 10
    temp = temp // 10
if (su == num):
    print("Yes")
else:
    print("No")
    
