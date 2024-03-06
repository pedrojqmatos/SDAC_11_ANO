import xml.etree.ElementTree as ET

data = '''
<ClothesBrands>
    <Brands>
        <Brand value="Polo Ralph Lauren">
            <id type="int">001</id>
            <size type="string">XS</size>
            <country type="string">United States</country>
            <colour type="string">purple</colour>
            <category>
                <product type="string">Polo Shirts</product>
                <product type="string">Sportshirts</product>
                <product type="string">Trainers</product>
            </category>
        </Brand>

        <Brand name="Nike">
            <id type="int">002</id>
            <size type="string">S</size>
            <country type="string">United States</country>
            <colour type="string">green</colour>
            <category>
                <product type="string">Air Max</product>
                <product type="string">Tech Fleece</product>
                <product type="string">Hoodies</product>
            </category>
        </Brand>

        <Brand name="Lacoste">
            <id type="int">003</id>
            <size type="string">M</size>
            <country type="string">France</country>
            <colour type="string">pink</colour>
            <category>
                <product type="string">Polo Shirts</product>
                <product type="string">Sweatshirt</product>
                <product type="string">Sneakers</product>
            </category>
        </Brand>

        <Brand name="Gant">
            <id type="int">004</id>
            <size type="string">L</size>
            <country type="string">United States</country>
            <colour type="string">white</colour>
            <category>
                <product type="string">Coat</product>
                <product type="string">Hoodies</product>
                <product type="string">Shirts</product>
            </category>
        </Brand>

        <Brand name="Pepe Jeans">
            <id type="int">005</id>
            <size type="string">XL</size>
            <country type="string">United States</country>
            <colour type="string">red</colour>
            <category>
                <product type="string">T-Shirt</product>
                <product type="string">Jeans</product>
                <product type="string">Knitwear</product>
            </category>
        </Brand>

        <Brand name="Tommy Hilfiger">
            <id type="int">006</id>
            <size type="string">XXL</size>
            <country type="string">United States</country>
            <colour type="string">blue</colour>
            <category>
                <product type="string">Polo Shirts</product>
                <product type="string">Shirts</product>
                <product type="string">Knitwear</product>
            </category>
        </Brand>

        <Brand name="Calvin Klein">
            <id type="int">007</id>
            <size type="string">XXXL</size>
            <country type="string">United States</country>
            <colour type="string">black</colour>
            <category>
                <product type="string">Jeans</product>
                <product type="string">Shoes</product>
                <product type="string">Underwear</product>
            </category>
        </Brand>
    </Brands>
</ClothesBrands>
'''

sdata = ET.fromstring(data)
brands_list = sdata.findall('Brands/Brand')

print('Brand count:', len(brands_list))

for brand in brands_list:
    print('Brand:', brand.get("value") if brand.get("value") else brand.get("name"))
    print('ID:', brand.find('id').text)
    print('Size:', brand.find('size').text)
    print('Country:', brand.find('country').text)
    print('Colour:', brand.find('colour').text)
    print('Categories:')
    categories = brand.find('category')
    for product in categories.findall('product'):
        print('- ', product.text)
    print('\n')
