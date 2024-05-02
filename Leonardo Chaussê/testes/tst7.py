fname = input("Open the designated file: ")

try :
    fhand = open(fname)
except :
    print("invalid file name",fname,"canot be open")
    quit()

for line in fhand :
    #retira todos os espaços a direita
    rline = line.rstrip()
    #coloca todos os caracteres em upercase
    print (rline.upper())