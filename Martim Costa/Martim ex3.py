hour=input("Enter hour's: ")
rate=input("Enter rate: ")
if float(hour)>40:
    fhour=float(hour)
    frate=float(rate)
    hourt=fhour*frate+(fhour-40)*1.5*frate
    print(("you have worked a total of"),fhour,("Hrs and your payment is: "),hourt)
else:
     nhour=float(hour)*float(rate)
     print("payment is:",nhour)