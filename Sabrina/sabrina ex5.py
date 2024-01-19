hour=input ("Enter hours: ")
rate=input ("Enter rate: ")

fhour=float(hour)
frate=float(rate)

def computepay (hour,rate): # defenir uma função 

    if fhour > 40:       # caso o nº de hrs for maior q 40, horas x rate + hrs extra com taxa extra

        payx=frate*fhour+(fhour-40)*1.5*frate
        return payx

    else:               # caso o user n tenha trabalhado hrs extra (mais de 40) fica sem taxa extra

        pay = frate*fhour   
        return pay

final = computepay(hour,rate)
print ("pay: ",final) 