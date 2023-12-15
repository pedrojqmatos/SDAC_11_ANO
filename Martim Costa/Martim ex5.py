hour=input ("Enter hours: ")
rate=input ("Enter rate: ")
fhour=float(hour)
frate=float(rate)
def computepay (hour,rate):
    if fhour> 40:
        payx=frate*fhour+(fhour-40)*1.5*frate
        return payx
    else:
        payy=frate*fhour   
        return payy
final=computepay(hour,rate)
print("your payment is",final)
