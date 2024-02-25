import xml.etree.ElementTree as ET

data = '''<jogadores>
    <jogador>
        <nome>MrSavage</nome>
        <pais>Noruega</pais>
        <servidor>EU</servidor>
        <earnings>360.579</earnings>
    </jogador>
    <jogador>
        <nome>Endretta</nome>
        <pais>Estados Unidos</pais>
        <servidor>Noruega</servidor>
        <earnings>257.920</earnings>
    </jogador>
    <jogador>
        <nome>Mongraal</nome>
        <pais>Reino Unido</pais>
        <servidor>EU</servidor>
        <earnings>334.050</earnings>
    </jogador>
    <jogador>
        <nome>Vadeal</nome>
        <pais>Alemanha</pais>
        <servidor>EU</servidor>
        <earnings>500.115</earnings>
    </jogador>
    <jogador>
        <nome>Malibuca</nome>
        <pais>Russia</pais>
        <servidor>EU</servidor>
        <earnings>408.340</earnings>
    </jogador>
    <jogador>
        <nome>4zr</nome>
        <pais>Suiça</pais>
        <servidor>EU</servidor>
        <earnings>223.491</earnings>
    </jogador>
    <jogador>
        <nome>TaySon</nome>
        <pais>Eslovénia</pais>
        <servidor>EU</servidor>
        <earnings>1.115.994</earnings>
    </jogador>
    <jogador>
        <nome>Merstach</nome>
        <pais>Letónia</pais>
        <servidor>EU</servidor>
        <earnings>428.380</earnings>
    </jogador>
    <jogador>
        <nome>Seeyun</nome>
        <pais>Brasil</pais>
        <servidor>BR</servidor>
        <earnings>81.267</earnings>
    </jogador>
    <jogador>
        <nome>916Gon</nome>
        <pais>Brasil</pais>
        <servidor>BR</servidor>
        <earnings>19.600</earnings>
    </jogador>
    <jogador>
        <nome>Vic0</nome>
        <pais>Áustria</pais>
        <servidor>EU</servidor>
        <earnings>85.675</earnings>
    </jogador>
    <jogador>
        <nome>Pinq</nome>
        <pais>Reino Unido</pais>
        <servidor>EU</servidor>
        <earnings>224.782</earnings>
    </jogador>
    <jogador>
        <nome>K1nG</nome>
        <pais>Brasil</pais>
        <servidor>EU/BR</servidor>
        <earnings>238.990</earnings>
    </jogador>
</jogadores>
'''

jogadores = ET.fromstring(data)
lst = list()
lst = jogadores.findall('jogador')
llst =len(lst)
print('Jogadores presentes na lista:', llst) # obter o numero de mjogadores existentes 


for jogador in lst:  
    # Obter informacoes como seu nome, pais, servidor e earnings
    print('Nome:', jogador.find('nome').text)
    print('Pais:', jogador.find('pais').text)
    print('Servidor:', jogador.find('servidor').text)
    print('Earnings:', jogador.find('earnings').text, '$\n')