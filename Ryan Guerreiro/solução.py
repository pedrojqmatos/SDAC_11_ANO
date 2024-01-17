word= input("Frase 1: ")
word2= input("Frase 2: ")

if word and word2 == "banana" :
    print("all right, bananas")
if len(word) < len(word2) :
    print("your word," + word + ", comes before",word2)
elif len(word) > len(word2):
    print("your word, " + word + ", comes after",word2)
