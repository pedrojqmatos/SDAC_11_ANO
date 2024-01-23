#variável para o input
fname = input("Open the designated file: ")
#utilizamos o "Try, Except" vai testar o fhand and open
try:
    fhand = open(fname)
    #ficheiro valido faz isto
except : 
    #se nao der bem vai dar este print, nao da para abrir e vai fechar
    print("Invalid file name", fname, "cannot be opened")
    quit()
    #é a variável para cada linha do input
for line in fhand :
    #tira os espaços a direita
    rline = line.rstrip()
    #meter a variável toda em maiusculas
    up_line = rline.upper()
    #imprime a variável em maiusculas e sem espaços
    print(up_line)
