import xml.etree.ElementTree as ET

xml='''
<ETPR> 
    <TGEI>
        <Disciplina value ="Português">
            <Professor type ="string"> Sergio Rodrigues </Professor>
            <Modulos_feitos type="string"> 4 </Modulos_feitos>
        </Disciplina>
        <Disciplina value="SDAC">
            <Professor type="string"> Pedro Matos </Professor>
            <Modulos_feitos type="string"> 7 </Modulos_feitos>
        </Disciplina>
        <Disciplina value="IMEI">
            <Professor type="string"> Carlos Silva </Professor>
            <Modulos_feitos type="string"> 4 </Modulos_feitos>
        </Disciplina>
    </TGEI>
</ETPR>
'''

biblioteca = ET.fromstring(xml)
XML = biblioteca.findall('TGEI/Disciplina')
print('Disciplina:', len(XML)) 
for item in XML: print('Disciplina:', item.get('value')) ; print('Modulos feitos:', item.find('Modulos_feitos').text) ; print('Professor:', item.find('Professor').text) 