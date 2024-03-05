import xml.etree.ElementTree as ET

xml_data = '''
<f1>
    <pilots>
        <name value="Max Vestappen">
            <number value="int">1</number>
            <team value="Red Bull">
                <world_champion value="int">3</world_champion>
            </team>
        </name>

        <name value="Checo Perez">
            <number value="int">11</number>
            <team value="Red Bull">
                <world_champion value="int">0</world_champion>
            </team>
        </name>

        <name value="Lewis Hamilton">
            <number value="int">44</number>
            <team value="Mercedes">
                <world_champion value="int">7</world_champion>
            </team>
        </name>

        <name value="George Russel">
            <number value="int">63</number>
            <team value="Mercedes">
                <world_champion value="int">0</world_champion>
            </team>
        </name>

        <name value="Charles Leclerc">
            <number value="int">16</number>
            <team value="Ferrari">
                <world_champion value="int">0</world_champion>
            </team>
        </name>

        <name value="Carlos Sainz">
            <number value="int">55</number>
            <team value="Ferrari">
                <world_champion value="int">0</world_champion>
            </team>
        </name>
    </pilots>
</f1>
'''

root = ET.fromstring(xml_data)

for name_element in root.findall('.//name'):
    pilot_name = name_element.get('value')
    pilot_number = name_element.find('./number').text
    team_name = name_element.find('./team').get('value')
    world_champion_count = name_element.find('./team/world_champion').text

    print(f"Name: {pilot_name}, Number: {pilot_number}, Team: {team_name}, World Champion: {world_champion_count}")
