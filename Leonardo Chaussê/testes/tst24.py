import requests

def obter_informacoes_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados_pokemon = resposta.json()

        print(f"Informações sobre o Pokémon {nome_pokemon}:")
        print(f"Nome: {dados_pokemon['name'].capitalize()}")
        print(f"ID: {dados_pokemon['id']}")
        print("Tipos:", ", ".join(tipo['type']['name'] for tipo in dados_pokemon['types']))
        print(f"Peso: {dados_pokemon['weight']} hectogramas")
        print(f"Altura: {dados_pokemon['height']} centimetros")
    else:
        print(f"Erro ao obter informações para o Pokémon {nome_pokemon}. Código de status: {resposta.status_code}")

if __name__ == "__main__":
    nome_pokemon = input("Digite o nome do Pokémon: ")
    obter_informacoes_pokemon(nome_pokemon)
