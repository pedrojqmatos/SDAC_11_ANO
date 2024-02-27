import xml.etree.ElementTree as ET

code = '''<F1>
    <Teams>
        <Team value="Read Bull">
            <Manager type="string">Christian Horner</Manager>
            <FirtPilot type="string">Max Verstappen</FirtPilot>
            <SecondPilot type="string">Sergio Perez</SecondPilot>
        </Team>

        <Team value="Mercedes">
            <Manager type="string">Toto Wolff</Manager>
            <FirtPilot type="string">Lewis Hamilton</FirtPilot>
            <SecondPilot type="string">George Russell</SecondPilot>
        </Team>

        <Team value="Ferrari">
            <Manager type="string">Frédéric Vasseur</Manager>
            <FirtPilot type="string">Charles Leclerc</FirtPilot>
            <SecondPilot type="string">Carlos Sainz</SecondPilot>
        </Team>

        <Team value="McLaren">
            <Manager type="string">Andrea Stella</Manager>
            <FirtPilot type="string">Lando Norris</FirtPilot>
            <SecondPilot type="string">Oscar Piastri</SecondPilot>
        </Team>

        <Team value="RB">
            <Manager type="string">Laurent Mekies</Manager>
            <FirtPilot type="string">Yuki Tsunoda</FirtPilot>
            <SecondPilot type="string">Daniel Ricciardo</SecondPilot>
        </Team>

        <Team value="Kick Sauber">
            <Manager type="string">Alessandro Alunni Bravi</Manager>
            <FirtPilot type="string">Valtteri Bottas</FirtPilot>
            <SecondPilot type="string">Zhou Guanyu</SecondPilot>
        </Team>

        <Team value="Haas">
            <Manager type="string">Ayao Komatsu</Manager>
            <FirtPilot type="string">Kavin Magnussen</FirtPilot>
            <SecondPilot type="string">Nico Hulkenberg</SecondPilot>
        </Team>

        <Team value="Aston Martin">
            <Manager type="string">Mike Krack</Manager>
            <FirtPilot type="string">Fernando Alonso</FirtPilot>
            <SecondPilot type="string">Lance Stroll</SecondPilot>
        </Team>

        <Team value="Alpine">
            <Manager type="string">Bruno Famin</Manager>
            <FirtPilot type="string">Piere Gasly</FirtPilot>
            <SecondPilot type="string">Esteban Ocon</SecondPilot>
        </Team>

        <Team value="Willians Racing">
            <Manager type="string">James Vowles</Manager>
            <FirtPilot type="string">Alexander Albon</FirtPilot>
            <SecondPilot type="string">Logan Sargeant</SecondPilot>
        </Team>
    </Teams>
</F1>'''

bibli = ET.fromstring(code) #guarda a biblioteca da "code"
XML = bibli.findall('Teams/Team') #ira procurar o "Team" que localiza-se no "Teams"
print('Teams count:', len(XML)) #ira contar quantas vezes as parece "Team"
#pergunta "value(Team)", "Manager" e "First Pilot"
for F1 in XML: print('Team:', F1.get('value')) ; print('Manager:', F1.find('Manager').text) ; print('First Pilot:', F1.find('FirtPilot').text) 