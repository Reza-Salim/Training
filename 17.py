byy = int(input("Enter Birth date ,year : "))
bmm = int(input("Enter Birth date ,month : "))
bdd = int(input("Enter Birth date ,day : "))
cyy = int(input("Enter current date ,year : "))
cmm = int(input("Enter current date ,month : "))
cdd = int(input("Enter current date ,day : "))
if cdd< bdd:
    cmm -= 1
    cdd += 30
day = cdd - bdd
if cmm < bmm:
    cyy -= 1
    cmm += 12
month = cmm - bmm
year = cyy- byy
days = day + month *30 + year *36
hh = days * 24
mm = hh *60
ss = mm * 60
print ("old is : {0}/{1}/{2}", year, month, day)
print ("Hour is(hh:mm:ss): {0}:{1}:{2}" ,hh, mm ,ss)

