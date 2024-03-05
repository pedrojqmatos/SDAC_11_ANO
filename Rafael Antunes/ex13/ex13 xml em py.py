import xml.etree.ElementTree as ET

data = '''
<alimentos>
  <alimento>
    <nome>Maçã</nome>
    <tipo>Fruta</tipo>
    <cor>Vermelho</cor>
    <calorias>52</calorias>
    <proteínas>0.3</proteínas>
    <gorduras>0.2</gorduras>
    <carboidratos>14</carboidratos>
    <fibra>2.4</fibra>
  </alimento>
  <alimento>
    <nome>Arroz</nome>
    <tipo>Grão</tipo>
    <cor>Branco</cor>
    <calorias>130</calorias>
    <proteínas>2.7</proteínas>
    <gorduras>0.3</gorduras>
    <carboidratos>28</carboidratos>
    <fibra>0.6</fibra>
  </alimento>
  <alimento>
    <nome>Peito de Frango</nome>
    <tipo>Carne</tipo>
    <cor>Branco</cor>
    <calorias>165</calorias>
    <proteínas>31</proteínas>
    <gorduras>3.6</gorduras>
    <carboidratos>0</carboidratos>
    <fibra>0</fibra>
  </alimento>
  <alimento>
    <nome>Picanha de Vaca</nome>
    <tipo>Carne</tipo>
    <cor>Branco</cor>
    <calorias>450</calorias>
    <proteínas>20</proteínas>
    <gorduras>35</gorduras>
    <carboidratos>0</carboidratos>
    <fibra>0</fibra>
  </alimento>
  <alimento>
    <nome>Lombo de Carneiro</nome>
    <tipo>Carne</tipo>
    <cor>Branco</cor>
    <calorias>300</calorias>
    <proteínas>20</proteínas>
    <gorduras>25</gorduras>
    <carboidratos>0</carboidratos>
    <fibra>0</fibra>
  </alimento>
</alimentos>
'''

dados = ET.fromstring(data)

for alimento in dados.findall('alimento'):
    print("Nome:", alimento.find('nome').text)
    print("Tipo:", alimento.find('tipo').text)
    print("Cor:", alimento.find('cor').text)
    print("Calorias:", alimento.find('calorias').text)
    print("Proteínas:", alimento.find('proteínas').text)
    print("Gorduras:", alimento.find('gorduras').text)
    print("Carboidratos:", alimento.find('carboidratos').text)
    print("Fibra:", alimento.find('fibra').text)
    print()
