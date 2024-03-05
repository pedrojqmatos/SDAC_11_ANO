def imprimir_em_maiusculas(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'b') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.upper(), end='')
    except FileNotFoundError:
        print(f"O arquivo '{nome_do_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    nome_do_arquivo = input("Escreva o nome do arquivo: ")
    imprimir_em_maiusculas(nome_do_arquivo)

