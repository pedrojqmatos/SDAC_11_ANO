fput = input('Select the file>>>')
fopen = open(fput)

for line in fopen:
    if line.startswith('From:'):
        continue 

    print(line)