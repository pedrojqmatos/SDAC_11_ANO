import xml.etree.ElementTree as ET

code = '''<stand>
    <models>
        <brand value ="Toyota">
            <id type="int">001</id>
            <model type="string">Corolla</model>
            <fuel type="string">Diesel</fuel>
            <max-speed type="string">178km/h</max-speed>
            <weight type="string">1024kg</weight>
            <doors type="int">5</doors>
        </brand>

        <brand value ="Mercedes">
            <id type="int">002</id>
            <model type="string">Benz</model>
            <fuel type="string">Petrol</fuel>
            <max-speed type="string">190km/h</max-speed>
            <weight type="string">1045kg</weight>
            <doors type="int">4</doors>
        </brand>

        <brand value ="BMW">
            <id type="int">003</id>
            <model type="string">i7</model>
            <fuel type="string">Hybrid</fuel>
            <max-speed type="string">183km/h</max-speed>
            <weight type="string">1032kg</weight>
            <doors type="int">5</doors>
        </brand>

        <brand value ="Audi">
            <id type="int">004</id>
            <model type="string">A4</model>
            <fuel type="string">Diesel</fuel>
            <max-speed type="string">176km/h</max-speed>
            <weight type="string">1012kg</weight>
            <doors type="int">4</doors>
        </brand>

        <brand value ="Ford">
            <id type="int">005</id>
            <model type="string">Smax</model>
            <fuel type="string">Petrol</fuel>
            <max-speed type="string">143km/h</max-speed>
            <weight type="string">1120kg</weight>
            <doors type="int">6</doors>
        </brand>
    </models>
</stand>'''

bibli = ET.fromstring(code) #guarda a biblioteca da "code"
XML = bibli.findall('models/brand') #ira procurar o "brand" que localiza-se no "models"
print('Brand count:', len(XML)) #ira contar quantas vezes aparece "brand"
#pergunta "value(brand)", "model" e "Fuel"
for item in XML: print('Brand', item.get('value')) ; print('Model', item.find('model').text) ; print('Fuel', item.find('fuel').text) 