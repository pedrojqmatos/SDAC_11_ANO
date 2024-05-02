frase = input("escreva uma frase?--> ")

selectword = input("selecione a letra que queres contar--> ")

count = 0

for letter in frase :
    if letter == selectword:
        count = count + 1
print(count)
