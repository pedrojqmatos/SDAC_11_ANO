#Utilize find e string slicing para extrair a parte da string após o 
#carácter dois pontos e, em seguida, utilize a função float para converter
#a string extraída num número flutuante.

data = "X-DSPAM-Confidence: 0.8475 "

atpos = data.find(":")
print(atpos)

matpos=atpos + 1

nmbr = data.find(" ", matpos)
print(nmbr)

data1 = nmbr.strip()
print(data1)

final = data[nmbr,data1]


