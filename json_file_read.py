import json
f = open("quakeFile2.txt", "a")


with open('query.json') as json_file:
    data = json.load(json_file)
    a = data['features']
    index = 0
    for quake in a:
        place = a[index]['properties']['place']
        place += "\n"
        f.write(place)
        print(place)
        index += 1


f.close()
