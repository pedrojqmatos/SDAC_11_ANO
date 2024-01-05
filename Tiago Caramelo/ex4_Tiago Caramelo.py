#gross pay program
nhours = input("Number of hours:")
nrate = input("Rate amount:")

try:
    fhours = float(nhours)
    frate = float(nrate)
except:
    print("Error! You provided an invalid value, please input a valid numeric input")
    exit()

if fhours > 40:
    #definir o pagamento regular
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 1.5)
    #a variável "nhours" vai converter o "inp" em int; #a variável "nrate" vai converter o "ntotal" em float
    ntotal = reg + otp
    #valor total que iremos receber
    print("you have worked overtime:", nhours , "Your pay is:", ntotal, "€")
else: 
    #o pagamento recular será igual a variável "fhours" * a variável "frate"
    reg = fhours * frate 
    print("You have worked regular hours:", nhours, "Your pay is:", reg, "€")