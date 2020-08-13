import json

from Character import Character


#
def validateJSON(filePath):
    with open(filePath) as characters:
        try:
            data = json.load(characters)
        except ValueError as error:
            return "error"
        return data


def loadCharacters(filePath):
    try:
        characters = []
        attributes = []
        data = validateJSON(filePath)

        for (k,v) in data.items():
            for character in v:
                properties = []
                for feature in character['features']:
                    for key,value in feature.items():
                        for values,v in value.items():
                            properties += [[key,values,v]]
                        if not (key in attributes):
                            attributes += [key]
                state = True
                person = Character(
                    character['name'],
                    character['imgUrl'],
                    properties,
                    state
                )
                characters += [person]
        print(attributes)
        #return characters,attributes
        filterAttributes(characters,"hair")

    except ValueError as error:
        return "Error, wrong JSON"


def filterAttributes(characters,value):
    results = []

    for character in characters:
        for props in character.features:
            if (value == props[0]):
                if not (props[1] in results):
                    results += [props[1]]
    print(results)
    filterValues(characters,value,results[0])
    #return results

def filterValues(characters,prop,value):
    results = []

    for character in characters:
        for props in character.features:
            if ((props[0] == prop) and (value == props[1])):
                if not (props[2] in results):
                    results += [props[2]]
    print(results)
    return results

