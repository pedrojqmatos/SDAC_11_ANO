import xml.etree.ElementTree as ET
data = '''<jogos> 
    <jogo> 
        <titulo>The Legend of Zelda: Breath of the Wild</titulo>
        <genero>Ação/Aventura</genero> 
        <plataforma>Nintendo Switch</plataforma> 
        <preco>$59.99</preco> 
    </jogo> 
    <jogo> 
        <titulo>Red Dead Redemption 2</titulo> 
        <genero>Ação/Aventura</genero> 
        <plataforma>PlayStation 4</plataforma> 
        <preco>$39.99</preco> 
    </jogo> 
    <jogo> 
        <titulo>Fortnite</titulo> 
        <genero>Battle Royale</genero> 
        <plataforma>Multiplataforma</plataforma> 
        <preco>Grátis</preco> 
    </jogo> 
    <jogo> 
        <titulo>FIFA 20</titulo> 
        <genero>Esportes</genero> 
        <plataforma>Xbox One</plataforma> 
        <preco>$29.99</preco> 
    </jogo> 
    <jogo> 
        <titulo>Minecraft</titulo> 
        <genero>Sandbox</genero> 
        <plataforma>PC</plataforma> 
        <preco>$26.95</preco> 
    </jogo>
    <jogo> 
        <titulo>Call of Duty: Warzone</titulo> 
        <genero>Battle Royale</genero> 
        <plataforma>Multiplataforma</plataforma> 
        <preco>Grátis</preco> 
    </jogo> 
</jogos>
'''
jogos = ET.fromstring(data)
st = list()
lst = jogos.findall('jogo')
llst =len(lst)
print('jogos presentes na lista:', llst)

for jogos in lst:  
    # Obter informacoes como seu titulo, genero, plataforma e preco
    print('titulo:', jogos.find('titulo').text)
    print('genero:', jogos.find('genero').text)
    print('plataforma:', jogos.find('plataforma').text)
    print('preco:', jogos.find('preco').text, '$\n')