import xml.etree.ElementTree as ET
data = '''
<games>
    <game>
        <name value ="Warframe">
            <info>
                <genre type="string">Looter Shooter,RPG</genre>
                <hours_played>2.410h</hours_played>
            </info>
        </name>
    </game>
    <game>
        <name value="Counter-Strike">
            <info> 
                <genre type="string">First Person Shooter, Comptitive Shooter </genre>
                <hours_played> 1.363h </hours_played>
            </info>
        </name>
    </game>
    <game>
        <name value ="Dauntless">
            <info>
                <genre type="string">Action RPG, CO-OP</genre>
                <hours_played> 743h </hours_played>
            </info>
        </name>
    </game>
</games>
'''
tree = ET.fromstring(data)
dtree = tree.findall("game/name")
print('Games count', len(dtree))
for item in dtree:
    print("Game name:",item.get("value"))
    print(item.find("info/genre").text, item.find("info/hours_played").text)


