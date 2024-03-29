import xml.etree.ElementTree as ET

code = '''<RocketLeague>
    <teams>
        <team value = "Vitality">
            <Coach type = "string">Fairy Peak!</Coach>
            <Captain type = "string">Alpha54</Captain>
            <PlayerOne type = "string">Radosin</PlayerOne>
            <PlayerTwo type = "string">Zen</PlayerTwo>
            <region type = "string">Europe</region>
            <conquist type = "string">RLCS 2022-23 - World Championship winners</conquist>
        </team>
        
        <team value = "Karmin Corp">
            <Coach type = "string">Ferra</Coach>
            <Captain type = "string">Vatira</Captain>
            <PlayerOne type = "string">Rise.</PlayerOne>
            <PlayerTwo type = "string">Atow.</PlayerTwo>
            <region type = "string">Europe</region>
            <conquist type = "string">RLCS 2022-23 - Winter Split Major winners</conquist>
        </team>
        
        <team value = "Gentle Mates Alpine">
            <Coach type = "string">Eversax</Coach>
            <Captain type = "string">itachi</Captain>
            <PlayerOne type = "string">Seikoo</PlayerOne>
            <PlayerTwo type = "string">Juici</PlayerTwo>
            <region type = "string">Europe</region>
            <conquist type = "string">Nothing</conquist>
        </team>
        
        <team value = "BDS">
            <Coach type = "string">Kassio</Coach>
            <Captain type = "string">M0nkey M00n</Captain>
            <PlayerOne type = "string">dralii</PlayerOne>
            <PlayerTwo type = "string">ExoTiik</PlayerTwo>
            <region type = "string">Europe</region>
            <conquist type = "string">RLCS 2021-22 - World Championship winners</conquist>
        </team>
        
        <team value = "NRG">
            <Coach type = "string">Fireburner</Coach>
            <Captain type = "string">GarrettG</Captain>
            <PlayerOne type = "string">mist</PlayerOne>
            <PlayerTwo type = "string">Toastie</PlayerTwo>
            <region type = "string">North America</region>
            <conquist type = "string">RLCS Season 8 - Finals (2019) winners</conquist>
        </team>
            
        <team value = "G2 stride">
            <Coach type = "string">Satthew</Coach>
            <Captain type = "string">Atomic</Captain>
            <PlayerOne type = "string">Daniel</PlayerOne>
            <PlayerTwo type = "string">BeastMode</PlayerTwo>
            <region type = "string">North America</region>
            <conquist type = "string">RLCS Season 9 - North America (2020) winners</conquist>
        </team>
            
        <team value = "Oxygen">
            <Coach type = "string">Snaski</Coach>
            <Captain type = "string">archie</Captain>
            <PlayerOne type = "string">eekso</PlayerOne>
            <PlayerTwo type = "string">Oski</PlayerTwo>
            <region type = "string">Europe</region>
            <conquist type = "string">RLCS 2022-23 - Fall: EU Regional 1 - Fall Open winners</conquist>
        </team>
        
        <team value = "FaZe Clan">
            <Coach type = "string">Roll Dizz</Coach>
            <Captain type = "string"> - </Captain>
            <PlayerOne type = "string">sypical</PlayerOne>
            <PlayerTwo type = "string"> - </PlayerTwo>
            <region type = "string">North America</region>
            <conquist type = "string">RLCS 2022-23 - Winter: NA Regional 3 - Winter Invitational winners</conquist>
        </team>
            
        <team value = "Gen.G">
            <Coach type = "string">Allushin</Coach>
            <Captain type = "string">ApparentlyJack</Captain>
            <PlayerOne type = "string">Chronic</PlayerOne>
            <PlayerTwo type = "string">Firstkiller</PlayerTwo>
            <region type = "string">North America</region>
            <conquist type = "string">RLCS 2022-23 - Fall Split Major</conquist>
        </team>
            
        <team value = "Falcons">
            <Coach type = "string">d7oom-24</Coach>
            <Captain type = "string">Rw9</Captain>
            <PlayerOne type = "string">trk511</PlayerOne>
            <PlayerTwo type = "string">Kiileerrz</PlayerTwo>
            <region type = "string">Saudi Arabia</region>
            <conquist type = "string">RLCS 2024 - Major 1: MENA Open Qualifier 1 winners</conquist>
        </team>
            
        <team value = "Rule One">
            <Coach type = "string">crespor</Coach>
            <Captain type = "string">oKhaliD</Captain>
            <PlayerOne type = "string">Ahmad</PlayerOne>
            <PlayerTwo type = "string">Nwpo</PlayerTwo>
            <region type = "string">Saudi Arabia</region>
            <conquist type = "string">RLCS 2022-23 - Spring: MENA Regional 3 - Spring Invitational winners</conquist>
        </team>
    </teams>
</RocketLeague>'''

bib = ET.fromstring(code)
dxml = bib.findall('teams/team')
print("Teams count:", len(dxml))
for item in dxml:
    print("Team", item.get('value'))
    print("Coach", item.find('Coach').text)
    print("Captain", item.find('Captain').text)
    print("Player One", item.find('PlayerOne').text)
    print("Player Two", item.find('PlayerTwo').text)
    print("Region", item.find('region').text)
    print("Conquist", item.find('conquist').text)
