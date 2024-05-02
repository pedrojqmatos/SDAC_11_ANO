import urllib.request
import re

# Abrir o link
url = "https://corta-fitas.blogs.sapo.pt/alergia-a-realidade-8170294"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

# Encontrar todas as palavras
words = re.findall(r'\b\w+\b', html.lower())

# Contar as palavras e armazenar em um dicionário
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Criar uma lista e um tuple com as palavras e suas contagens
word_list = [(key, value) for key, value in word_count.items()]
word_tuple = tuple(word_list)

# Ordenar os itens pelos termos mais encontrados
sorted_word_list = sorted(word_list, key=lambda x: x[1], reverse=True)
top_10_words = sorted_word_list[:10]

print("Os 10 termos mais encontrados:")
for word, count in top_10_words:
    print(f"{word}: {count}")