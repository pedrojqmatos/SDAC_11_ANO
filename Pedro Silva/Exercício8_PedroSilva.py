ffile = input("Open desegnated file:")
try:
    fopen = open(ffile)
except:
    print("Invalid file name". ffile, "cannot be opened")
    quit()
#se o nome corresponder abre, se nao nao abre nada e fecha
for line in fopen:
    fup= line.upper()
    #tranforma em maiusculas
    print(fup.rstrip())