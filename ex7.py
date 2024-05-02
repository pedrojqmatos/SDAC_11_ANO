data = "X-DSPAM-Confidence: 0.8475 "

descobre = data.find(":") 

escreve_valor = data[descobre + 1 : ].strip()
valor = float(escreve_valor)
print(valor)

round = str(valor)
num = round[0:5]
num5 = round[0:4]
numposion4 = num[4:]

if numposion4 < "5":
    print(num5)
elif numposion4 >= "5":
    numup5float = float(num5)
    finaly = numup5float + 0.01
    print(finaly)