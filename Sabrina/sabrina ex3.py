hour=input("Enter hour's: ")
rate=input("Enter rate: ")

if float(hour)>40: #caso o numero de hrs for maior q 40

    fhour=float(hour)
    frate=float(rate)

    hourt=fhour*frate+(fhour-40)*1.5*frate # hora a dividir por rate mais hrs - 40 a multiplicar por 1.5 a multiplicar por rate

    print(("you have worked "),fhour,("Hrs, your payment is: "),hourt)

else:        # caso o nº de hrs for menor q 40

     nhour=float(hour)*float(rate)

     print("pay:",nhour) 