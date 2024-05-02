#leonardo chausse
bigest_number = -1 #difine o "-1" como uma comparação inicial

print("before",bigest_number)

#inicia um loop
for number in [9,41,12,3,74,15]: #seleciona quais numeros serõo utilizados 

    if number > bigest_number:   #compara o numero com o seu anterior e ve qual e o maior
        bigest_number = number   #seleciona o maior numero 

    print (bigest_number,number) #define oque sera escrito durante o correr do programa
   
print("after: ", bigest_number)

#professor
largest_so_far = -1
print("before :", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("after: ", largest_so_far)