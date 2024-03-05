import xml.etree.ElementTree as ET  
input = '''<filmes>
    <filme>
        <titulo value = "Spider Man">
            <categoria type = "string">Super-Heróis</categoria>
        </titulo>
    </filme>
    <filme>
        <titulo value = "Interestelar">
            <categoria type = "string">Ficção Científica</categoria>
        </titulo>    
    </filme>
    <filme>
        <titulo value ="Forrest Gump">
            <categoria type = "string">Drama</categoria>
        </titulo>                
    </filme>
    <filme>
        <titulo value = "Matrix">
            <categoria type = "string">Ação</categoria>
        </titulo>    
    </filme>
    <filme>
        <titulo value = "O Senhor dos Anéis">
            <categoria type = "string">Aventura</categoria>
        </titulo>    
    </filme>
</filmes>'''
stuff = ET.fromstring (input)
lst = stuff.findall('filme/titulo')
print('Número de filmes', len(lst))
for item in lst:
  print ('titulo', item.get('value'))
  print ('Categoria', item.find('categoria').text)
    