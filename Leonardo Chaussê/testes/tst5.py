word = input("fruta 1")
count = input("fruta 2")


if len(word) == len(count) :
    print("A palavra" ,word, "é banana")
if len(word) < len(count) :
    print("A palavra", word, "é menor que", count )
elif len(word) > len(count) :
    print ("A palavra", word, "e maior que", count)
else :
    print("Terminado")