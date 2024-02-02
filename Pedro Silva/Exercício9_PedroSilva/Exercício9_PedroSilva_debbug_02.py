fopen = open("mbox-short.txt")

for line in fopen:
    line = line.rstrip()
    print("Estas são as linhas>>>", line)
    words = line.split()
    print("Estas são as palavras>>>", words)
    if words[0] != "From":
        continue
    print(words[2])