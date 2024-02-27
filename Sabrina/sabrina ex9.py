fix = input("open the designated file: ")

try:
    ffix = open(fix)
except:

    print("invalid file name",fix,"cannot be opened")
    quit()

for line in ffix:

    llrs = line.rstrip()
    print(line.upper())
    