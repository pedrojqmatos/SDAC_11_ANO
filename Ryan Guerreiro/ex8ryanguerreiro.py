input=input("Open the designated file: ") #input do nome do ficheiro

try:
    iopen=open(input) #o python irá abrir o ficheiro que foi designado
except:
    print("Invalid file name",input,"cannot be oppened") #parar o codigo quando o ficheiro não conseguiu abrir
    quit()

for line in iopen:  #transformação de retirar os espaços e deixar em maiúsculas
    linestr = line.rstrip()
    print(linestr.upper())
