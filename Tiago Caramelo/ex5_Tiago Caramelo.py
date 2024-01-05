def computepay(nhours, nrate): 
    #input onde iremos escolher o número de horas, de seguida o "inp" e o "ntotl" são as 2 variáveis
    if nhours > 40:
        #definir o pagamento regular
        reg = nhours * nrate
        otp = (nhours - 40) * (nrate * 1.5)
        #a variável "nhours" vai converter o "inp" em int; #a variável "nrate" vai converter o "ntotal" em float
        ntotal = reg + otp
        #valor total que iremos receber
        print("you have worked overtime:", nhours , "Your pay is:", ntotal, "€")
    else: 
     #o pagamento recular será igual a variável "fhours" * a variável "frate"
        ntotal = nhours * nrate 
    print("You have worked regular hours:", nhours, "Your pay is:", ntotal, "€")
    return ntotal
    

nhours = input("Enter Hours:")
nrate = input("Enter Rate:")
#corverter em float
fhours = float(nhours)
frate = float(nrate)   


xp = computepay(fhours, frate)
print("Pay: ", xp, "€")
