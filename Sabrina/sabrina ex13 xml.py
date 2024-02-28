import xml.etree.ElementTree as ET

data =''' 
<restaurantes>
    <restaurante>
        <name value ="Burguer King">
            <info>
                <local type="string">Santarem</local>
                <tipo_de_comida>Fast Food</tipo_de_comida>
            </info>
        </name>
    </restaurante>

    <restaurante>
        <name value ="La Bella">
            <info>
                <local type="string">Santarem</local>
                <tipo_de_comida> Comida Italiana </tipo_de_comida>
            </info>
        </name>
    </restaurante>

    <restaurante>
        <name value ="EL Mexicano ">
            <info>
                <local type= "string">Santarem</local>
                <tipo_de_comida>Comida Mexicana </tipo_de_comida>
            </info>
        </name>
    </restaurante>

</restaurantes> '''

inf = ET.fromstring(data)
dtree = inf.findall("restaurante/name")
print('Numero de restaurantes:', len(dtree))
for item in dtree:
    print("nome dos restourantes:", item.get("value"))
    print(item.find("info/local").text, item.find("info/tipo_de_comida").text)