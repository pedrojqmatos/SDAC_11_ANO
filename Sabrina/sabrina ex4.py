hour=input("Enter hour: ")

try:      

    fhour=float(hour)
    rate=input("Enter rate: ")

    frate=float(rate)
    print("nice")

except:     # caso o user n tenha colocado um valor numerico

        print("Error, please enter numeric input")
        exit()