import xml.etree.ElementTree as ET
code = '''
<stand>
    <shoes>
        <name value ="nikeSB">
            <style type ="string">Skate shoes</style>
            <sizenumber type="string">43</sizenumber>
            <color type="string">yelow/gren</color>
            <orders type="string">41</orders>
            <price type="string">450€</price>
            <material type="string">canvas</material>
        </name>
    
        <name value ="nike air max 97">
            <style type ="string">training shoes</style>
            <sizenumber type="string">34</sizenumber>
            <color type="string">black/wite</color>
            <orders type="string">13</orders>
            <price type="string">250€</price>
            <material type="string">mesh</material>
        </name>
    
        <name value ="new balance">
            <style type ="string">all in 1</style>
            <sizenumber type="string">46</sizenumber>
            <color type="string">black/blue</color>
            <orders type="string">23</orders>
            <price type="string">120€</price>
            <material type="string">canvas</material>
        </name>

        <name value="nike">
            <style type="string">air max</style>
            <sizenumber type="string">42</sizenumber>
            <color type="string">black/red</color>
            <material type="string">leather</material>
            <orders type="string">45</orders>
            <price type="string">150€</price>
            <material type="string">leather</material>
        </name>

        <name value="adidas superstar">
            <style type="string">classic</style>
            <sizenumber type="string">38</sizenumber>
            <color type="string">white/black</color>
            <orders type="string">55</orders>
            <price type="string">120€</price>
            <material type="string">leather</material>
        </name>

        <name value="converse chuck taylor">
            <style type="string">high top</style>
            <sizenumber type="string">40</sizenumber>
            <color type="string">red</color>
            <orders type="string">28</orders>
            <price type="string">80€</price>
            <material type="string">canvas</material>
        </name>

        <name value="nike react element">
            <style type="string">running shoes</style>
            <sizenumber type="string">41</sizenumber>
            <color type="string">blue/green</color>
            <orders type="string">37</orders>
            <price type="string">160€</price>
            <material type="string">mesh</material>
        </name>

        <name value="reebok classic">
            <style type="string">retro</style>
            <sizenumber type="string">43</sizenumber>
            <color type="string">white/navy</color>
            <orders type="string">20</orders>
            <price type="string">100€</price>
            <material type="string">suede</material>
        </name>

    </shoes>
</stand>
'''

search = ET.fromstring(code) 

dxml = search.findall('shoes/name') #ira procurar o "nome" que localiza-se no "shoes"

print('Shoes count:', len(dxml)) #ira contar quantas vezes aparece "name"


for item in dxml:
     print('Nome:', item.get("value")) 
     print('Estilo:', item.find('style').text) 
     print('Numero:', item.find('sizenumber').text) 
     print('Pedidos:', item.find('orders').text)
     print('Cor:', item.find('color').text )
     print('Preço:', item.find('price').text) 
     print('Material:', item.find('material').text) 