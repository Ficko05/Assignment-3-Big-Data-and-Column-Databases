import happybase
import xml.etree.ElementTree as ET

URL = "./data/Food_Display_Table.xml"


def get_connected():
    connection = happybase.Connection("localhost", 9090)
    connection.open()

    print(connection.tables())

    return connection
    # connection.close()


def create_tabel(connection):
    tables_in_DB = connection.tables()
    print(tables_in_DB)
    if b'foods' not in tables_in_DB:
        print('in if block')
        connection.create_table('foods',
                                {'foodz': dict(), }
                                )

    return connection

    # batch.put()
    # put'test123', '1', 'cf1:name', 'raju'
    # row = table.row(b'1')
    # print(row)


def read_data():
    tree = ET.parse(URL)
    root = tree.getroot()
    # print(root[2013][25].text)
    # print(root[0][0].text)
    # print(len(list(root)))
    return root


def getFoodDataFromXML(data, connection):
    table = connection.table('foods')
    batch = table.batch()

    # scan 'foods' , {COLUMNS => 'foodz:Soy'}
    # batch.put('0', {"foodz:Food_Code": data[0][0].text})
    # batch.send()

    print(data[394][5].text)
    print("hello")
    # print(len(list(data)))
    y = 0
    for x in range(2014):
        # for y in range(25):

        batch.put(f'{x}', {"foodz:Food_Code": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Display_Name": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Portion_Default": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Portion_Amount": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Portion_Display_Name": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Factor": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Increment": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Multiplier": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Grains": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Whole_Grains": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Vegetables": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Orange_Vegetables": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Drkgreen_Vegetables": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Starchy_vegetables": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Other_Vegetables": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Fruits": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Milk": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Meats": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Soy": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Drybeans_Peas": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Oils": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Solid_Fats": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Added_Sugars": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Alcohol": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Calories": data[x][y].text})
        y += 1

        batch.put(f'{x}', {"foodz:Saturated_Fats": data[x][y].text})
        y = 0
        # print(data[x][0].text)
        print(x)
        batch.send()


if __name__ == '__main__':
    read_data()
    connection = get_connected()
    create_tabel(connection)
    getFoodDataFromXML(read_data(), create_tabel(connection))
    connection.close()

# batch.put(f'{x}', {"foodz:Food_Code": data[x][y].text,
#                            "foodz:Display_Name": data[x][y].text,
#                            "foodz:Portion_Default": data[x][y].text,
#                            "foodz:Portion_Amount": data[x][y].text, "foodz:Portion_Display_Name": data[x][y].text,
#                            "foodz:Factor": data[x][y].text,
#                            "foodz:Increment": data[x][y].text, "foodz:Multiplier": data[x][y].text,
#                            "foodz:Grains": data[x][y].text,
#                            "foodz:Whole_Grains": data[x][y].text, "foodz:Vegetables": data[x][y].text,
#                            "foodz:Orange_Vegetables": data[x][y].text,
#                            "foodz:Drkgreen_Vegetables": data[x][y].text,
#                            "foodz:Starchy_vegetables": data[x][y].text,
#                            "foodz:Other_Vegetables": data[x][y].text,
#                            "foodz:Fruits": data[x][y].text, "foodz:Milk": data[x][y].text,
#                            "foodz:Meats": data[x][y].text,
#                            "foodz:Soy": data[x][y].text, "foodz:Drybeans_Peas": data[x][y].text,
#                            "foodz:Oils": data[x][y].text,
#                            "foodz:Solid_Fats": data[x][y].text, "foodz:Solid_Fats": data[x][y].text,
#                            "foodz:Added_Sugars": data[x][y].text,
#                            "foodz:Alcohol": data[x][y].text, "foodz:Calories": data[x][y].text,
#                            "foodz:Saturated_Fats": data[x][y].text})
