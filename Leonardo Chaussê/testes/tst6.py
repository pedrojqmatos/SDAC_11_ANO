#word = "www.leonardochausse.com"
#search_word = word.find ("com")
#print(search_word)

#------------------------------------------

#word = "www.leonardochausse.com"
#replace_word = word.replace ("com", "http")
#print(replace_word)

#------------------------------------------

data = "X-DSPAM-Confidence: 0.8475 "

dots = data.find(":")
print("colon position:",dots)

sppos = data.find ("5",dots)
print(sppos)

final = data[dots + 1 : sppos + 1]
print(final)

f= round(float(final))
print("final result",f,"!")



