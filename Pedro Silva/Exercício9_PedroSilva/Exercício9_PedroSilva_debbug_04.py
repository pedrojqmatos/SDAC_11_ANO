fopen = open("mbox-short.txt")

for line in fopen:
    line = line.rstrip()
    print("Estas são as linhas>>>", line)
    words = line.split()
    print("Estas são as palavras>>>", words)
    if len(words) < 1:
        continue
    if words[0] != "From":
        print("Ignora")
        continue
    print(words[2])