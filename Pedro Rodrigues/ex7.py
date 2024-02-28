#Utilize find e string slicing para extrair a parte da string após o 
#carácter dois pontos e, em seguida, utilize a função float para converter
#a string extraída num número flutuante.

str = 'X-DSPAM-Confidence: 0.8475'
cpos = str.find(':')
print ('Colon position is : ', cpos)
npos = str [cpos + 1 : ].strip()
fvalue = float (npos)
print ('Floating value is :', fvalue)
sum = fvalue * 12
print ('The sum result is', sum , 'The round value is', round(sum))