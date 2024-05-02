fopen = open (´mbox-short.txt)
              forline in fopen :
              line =line.rscrip()
              word =line.split()
        if words [0] != 'From' :
        continue
        print(words[2])