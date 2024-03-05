import xml.etree.ElementTree as ET

xml_data = '''
<items>
    <item>
        <roupa>sweat</roupa>
        <nome>Camisola Nike Club</nome>
        <tamanho>
            <type>int</type>
            <value>xl</value>
        </tamanho>
        <cor>
            <type>string</type>
            <value>grey</value>
        </cor>
        <preco>
            <type>float</type>
            <value>44.00</value>
        </preco>
    </item>
    <item>
        <roupa>meias nike</roupa>
        <nome>meias nike</nome>
        <tamanho>
            <type>int</type>
            <value>37-40</value>
        </tamanho>
        <cor>
            <type>string</type>
            <value>green</value>
        </cor>
        <preco>
            <type>float</type>
            <value>15.00</value>
        </preco>
    </item>
    <item>
        <roupa>calças</roupa>
        <nome>The North Face Exploration Tapered</nome>
        <tamanho>
            <type>int</type>
            <value>xl</value>
        </tamanho>
        <cor>
            <type>string</type>
            <value>preto</value>
        </cor>
        <preco>
            <type>float</type>
            <value>85.00</value>
        </preco>
    </item>
</items>
'''


root = ET.fromstring(xml_data)


for item in root.findall('item'):
    print("Roupa:", item.find('roupa').text)
    print("Nome:", item.find('nome').text)
    print("Tamanho:", item.find('tamanho/value').text)
    print("Cor:", item.find('cor/value').text)
    print("Preço:", item.find('preco/value').text)
    print("\n")
