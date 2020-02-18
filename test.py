import json

with open('.\\04-scrapy\\06-spider-items\\arania_fibeca\\tmp\\productos-fybeca.json') as json_file:
    data = json.load(json_file)
    ahorro_total = 0
    for p in data:
        ahorro_total = ahorro_total + p['ahorro']
    print(ahorro_total)

