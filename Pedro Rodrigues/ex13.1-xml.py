#ex13.1-xml

import xml.etree.ElementTree as ET
code = '''
<store>
    <series>
            <category value ="Action">
                <series_name type = "string" >Breaking Bad</series_name>
                <series_time type = "string" >54 horas</series_time>
            </category>
            <category value ="Comedy">
                <series_name type = "string">The Office</series_name>
                <series_time type = "string" >12 horas</series_time>
            </category>
            <category value ="Drama">
                <series_name type = "string">Stranger Things</series_name>
                <series_time type = "string" >45 horas</series_time>
            </category>
    </series>
</store>'''


stuff = ET.fromstring(code)
lst = stuff.findall('series/category')

print('series count:', len(lst))

for item in lst:
    print("Categorias: ", item.get('value'))
    print("Nome da série: ", item.find('series_name').text)
    print("Tempo de série: ", item.find('series_time').text)


    