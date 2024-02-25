import xml.etree.ElementTree as ET
input = '''<stand>
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


stand = ET.fromstring(input)
lst = list()
lst = stand.findall('models/brand')
llst =len(lst)
print('Brand count:', llst) # obter o numero de marcar existentes 


for brand in lst:  
    # Obter informacoes como marca modelo e combustivel
    print('Brand', brand.get('value'))
    print('Model', brand.find('model').text)
    print('Fuel', brand.find('fuel').text)