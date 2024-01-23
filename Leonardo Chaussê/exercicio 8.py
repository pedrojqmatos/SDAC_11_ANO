fname = input("Open the designated file: ")

try :
    fhand = open (fname)

except :
    if fname == ("mbox-short.txt") :
        print("ok valid file name")

    else:

        print("Invalid file name '",fname,"' canot be opened")
    
    quit()

for line in fhand :
    #retira todos os espaços a direita
    rline = line.rstrip()
    #coloca todos os caracteres em upercase
    print (rline.upper())