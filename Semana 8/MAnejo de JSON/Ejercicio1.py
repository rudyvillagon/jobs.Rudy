import json


def pokemon_json():

    with open("Semana8.3\Pokemons.json" , 'r', encoding="cp1252") as f:
        poke_list = json.load(f)
    return poke_list    
    

def  add_pokemon():

    name = input("Name of the Pokemon:  ")
    type = input("what type of Pokemon is:  ") 

    stats = {}

    stats["HP"] = int(input("Add his HP:  "))
    stats["Attack"] = int(input("Add his Attack power: "))
    stats["Defense"] = int(input("Add his Defense power:  "))
    stats["Speed Attack"]= int(input("Add his Speed Attack:  "))
    stats["Speed Defense"] = int(input("Add his Defense Speed:  "))
    stats["Speed"] = int(input("Add his Speed:  "))

    new_pokemon = {
            "Name" :{
            "english" : name,
            } ,
            "Type" : [type],
            "base" : stats
        }

    return new_pokemon



def new_poke_list(poke_list,new_pokemon):

    poke_data = poke_list + [new_pokemon]

    json_string = json.dumps(poke_data,indent=4)
    print(json_string)    

    with open("data.json","w") as pokedex:
        json.dump(poke_data,pokedex,indent=4)


list1 = pokemon_json()
list2 = add_pokemon()

new_poke_list( list1, list2)
