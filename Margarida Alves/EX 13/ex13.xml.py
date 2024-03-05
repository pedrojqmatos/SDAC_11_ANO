import xml.etree.ElementTree as ET
data='''
<roupas>

    <roupa>
        <vestuario value = "camisas">
            <nome type="string">camisa azul</nome>
            <categoria type="string">camisa</categoria>
            <tamanho type="string">M</tamanho>
            <cor type="string">Azul</cor>
            <preco type="string">20.00€</preco>
        </vestuario>
    </roupa>

    <roupa>
        <vestuario value = "calças">
            <nome type="string">Calcas Jeans</nome>
            <categoria type="string">Calcas</categoria>
            <tamanho type="string">32</tamanho>
            <cor type="string">Preto</cor>
            <preco type="string">35.00€</preco>
        </vestuario>
    </roupa>

    <roupa>
        <vestuario value = "casacos">
            <nome type="string">casaco preto</nome>
            <categoria type="string">casaco</categoria>
            <tamanho type="string">xl</tamanho>
            <cor type="string">Vermelho</cor>
            <preco type="string">45.00€</preco>
        </vestuario>
    </roupa>

</roupas>
'''

tree = ET.fromstring(data)
ltree = tree.findall('roupa/vestuario')
print('Número de roupas', len(ltree))
for item in tree:
    print("nome", item.find ('vestuario/nome').text)
    print("tamanho", item.find ('vestuario/tamanho').text)
    print("preço", item.find ('vestuario/preco').text)
