import xml.etree.ElementTree as ET

code = """<main>
    <animes>
        <anime name="Demon Slayer">
            <original-name type="string">Kimetsu no Yaiba (鬼滅きめつの刃)</original-name>
            <creation>
                <year type="int">2019</year>
                <creator type="string">Koyoharu Gotouge</creator>
            </creation>
            <main-character type="string">Tanjiro Kamado</main-character>
            <volumes type="int">23</volumes>
            <episodes type="int">26</episodes>
            <state type="string">finished</state>
        </anime>

        <anime name="Sorcerer Battle">
            <original-name type="string">Jujutsu Kaisen (呪術廻戦)</original-name>
            <creation>
                <year type="int">2017</year>
                <creator type="string">Gege Akutami</creator>
            </creation>
            <main-character type="string">Yuji Itadori</main-character>
            <volumes type="int">25</volumes>
            <episodes type="int">47</episodes>
            <state type="string">in progress</state>
        </anime>

        <anime name="Attack on Titan">
            <original-name type="string">Shingeki no Kyojin (進撃の巨人)</original-name>
            <creation>
                <year type="int">2009</year>
                <creator type="string">Hajime Isayama</creator>
            </creation>
            <main-character type="string">Eren Yeager</main-character>
            <volumes type="int">34</volumes>
            <episodes type="int">88</episodes>
            <state type="string">finished</state>
        </anime>

        <anime name="Berserk">
            <original-name type="string">Berserk (ベルセルク)</original-name>
            <creation>
                <year type="int">1989</year>
                <creator type="string">Kentaro Miura</creator>
            </creation>
            <main-character type="string">Guts</main-character>
            <volumes type="int">42</volumes>
            <episodes type="int">25</episodes>
            <state type="string">in progress</state>
        </anime>
    </animes>
</main>"""

#guarda a biblioteca da "code"
lib = ET.fromstring(code)
animes = lib.find("animes")
anime_list = animes.findall("anime")

print('Animes count:', len(anime_list)) #irá contar quantos animes existem

#pergunta o nome do anime, o ano de criação e o criador
for anime in anime_list:
    print('Anime name:', anime.get('name'))
    original_name = anime.find('original-name').text
    print('Original name:', original_name)
    creation_year = anime.find('creation/year').text
    print('Creation year:', creation_year)
    creator = anime.find('creation/creator').text
    print('Creator:', creator)
    print()
