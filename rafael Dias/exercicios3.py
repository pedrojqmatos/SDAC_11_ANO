nhours = input("number of hours")
nrate = input("rate amount")
fhours = float(nhours)
frate = float(nrate)
if fhours > 40:
    reg = fhours*frate
    otp = (fhours - 40)*(frate*1.5)
    ntotal = reg + otp
    print("you have worked overtime:", "nhours, your pay is", reg)