#Escrever Ficheiros em letra Maiuscula

file= input("Open the designated file: ")    # Pede ao utilizador o nome de um ficheiro           

try:                     # Verifica se existe esse ficheiro
    ofile= open(file)
except:
    print("Invalid file", file, "name cannot be opened ")      # Caso nao existir esse ficherio, envia alerta
    quit()

for line in ofile :           # Para cada linha
    rline = line     # Retira o espaco entre linhas
    up_line = rline.upper()   # Coloca as palavras todas em maiusculas
    print(up_line)            # Escreve as linhas sem espacos e em letras maiusculas
