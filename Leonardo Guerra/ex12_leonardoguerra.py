import urllib.request, urllib.parse, urllib.error

url = input('Enter link - ')
urlopen = urllib.request.urlopen(url)
words_count = dict()
for line in urlopen: 
    words = line.decode().split()
    for word in words: words_count[word] = words_count.get(word, 0) + 1
    
add = []   
for key, value in words_count.items(): new_tuple = (value, key) ; add.append(new_tuple)
add = sorted(add, reverse=True)
for value, key in add[:10]: print(key, value)
