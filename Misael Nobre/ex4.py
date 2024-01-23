#gross pay program
nhours = input("number of hours:")
nrate = input("Rate amount:")
try:
#convert to float
    fhours = float(nhours)
    frate = float(nrate)
except: 
    print("error! You provided an invalid value, please enter numeric input")
    exit()

if fhours > 40:
    #define regular pay
    reg = fhours*frate
    otp = (fhours - 40)*(frate*1.5)
    ntotal = reg + otp
    print("you have worked overtime:", nhours,"your pay is", ntotal)
else:
    #follows the regular pay minus 40h
    reg = fhours*frate
print("you have worked regular hours:", nhours,"your pay is", reg)
