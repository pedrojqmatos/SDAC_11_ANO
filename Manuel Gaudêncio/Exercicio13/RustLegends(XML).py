import xml.etree.ElementTree as ET

xml_string = '''<RustLegends>
    <Rust>
        <Player>
            <Name>Tacularr</Name>
            <Age>24</Age>
            <Hours>22000</Hours>
            <occupation>ContentCreator</occupation>
            <Region>AUS</Region>
        </Player>
        <Player>
            <Name>Posty</Name>
            <Age>27</Age>
            <Hours>17000</Hours>
            <occupation>Streamer</occupation>
            <Region>EU</Region>
        </Player>
        <Player>
            <Name>Trausi</Name>
            <Age>34</Age>
            <Hours>24000</Hours>
            <occupation>Streamer</occupation>
            <Region>EU</Region>
        </Player>
        <Player>
            <Name>AloneinTokyo</Name>
            <Age>Unknown</Age>
            <Hours>19000</Hours>
            <occupation>ContentCreator</occupation>
            <Region>SEA</Region>
        </Player>
        <Player>
            <Name>Qaixx</Name>
            <Age>21</Age>
            <Hours>14000</Hours>
            <occupation>Streamer</occupation>
            <Region>EU</Region>
        </Player>
        <Player>
            <Name>Gorliac</Name>
            <Age>23</Age>
            <Hours>16000</Hours>
            <occupation>ContentCreator</occupation>
            <Region>EU</Region>
        </Player>
        <Player>
            <Name>Mikelele</Name>
            <Age>28</Age>
            <Hours>9000</Hours>
            <occupation>ContentCreator</occupation>
            <Region>EU</Region>
        </Player>
        <Player>
            <Name>Hjune</Name>
            <Age>24</Age>
            <Hours>14000</Hours>
            <occupation>ContentCreator</occupation>
            <Region>USA</Region>
        </Player>
        <Player>
            <Name>Alberto</Name>
            <Age>16</Age>
            <Hours>3200</Hours>
            <occupation>GAMER</occupation>
            <Region>EU</Region>
        </Player>
    </Rust>
</RustLegends>'''

# Parsing do XML
root = ET.fromstring(xml_string)

# Informações do respetivo jogador
for player in root.findall('./Rust/Player'):
    name = player.find('Name').text
    age = player.find('Age').text
    hours = player.find('Hours').text
    occupation = player.find('occupation').text
    region = player.find('Region').text
    print(f"Name: {name},   Age: {age},   Hours: {hours},   Occupation: {occupation},   Region: {region}")
    