data = "X-DSPAM-Confidence: 0.8475 "

descobre = data.find(":") 
#irá procurar os ":" e indica a sua possição

escreve_valor = data[descobre + 1 : ].strip()
#escreve o lavor aseguir ao ":"+1 ou seja depois do espaço até o fim e retira o espaço de ambos os lados
valor = float(escreve_valor)
print(valor)

round = str(valor)
num = round[0:5]
#escreve o numero ate a posição 3 
num5 = round[0:4]
#escreve o numero ate a posição 2
numposion3 = num[4:]
#escreve o valor so da posição 3
numposion2 = num[3:4]
#escreve o valor so da posição 2

if numposion3 < "5":
    print(num5)
    #se o valor na 3 posição for menor que 5 returna o valor ate a 3 casa sem alteração
elif numposion3 >= "5":
    numup5float = float(num5)
    finaly = numup5float + 0.01
    print(finaly)
    #se o valor na 3 posição for maior ou igual a 5 retorna o valor com alterações