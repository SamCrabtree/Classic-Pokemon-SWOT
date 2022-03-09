import json
import requests
import pandas
import sys

name = []
pokemon_team = []
pokemon_elements = []


def main():

    print("Welcome to the Classic Pokemon SWOT Program! \n")
    print(listPokemon())
    team()


# THIS PULLS ALL OF THE NAMES OF THE OG POKEMON

def listPokemon():
    all_api = "https://pokeapi.co/api/v2/pokemon?limit=151" 
    r = requests.get(all_api) 
    api_response = json.loads(r.text)
    pokemon_list = api_response['results']
    for pokemon in pokemon_list:
        print(pokemon['name'].capitalize())


#

def pokeLookup():
    try:
        poke_request = input('What pokemon would you like to add to your team? OR type "List" to display a list of all names. \n' )
        if poke_request.lower == "list":
            listPokemon()
        else:
            individual_api = "https://pokeapi.co/api/v2/pokemon/" + poke_request.lower() + "/"    
            response = requests.get(individual_api)
            poke_data = json.loads(response.text)
            pokemon_name = poke_data['species']['name']
            pokemon_type = poke_data['types'][0]['type']['name']
            print("\n I see you chose " + pokemon_name.capitalize() + ". Great choice! \n")
        return pokemon_name, pokemon_type
    
    except:
        print("I couldn't find a match for that entry.")
        

    
   

def team():
        poke_team = []
        types = []
        while len(poke_team) < 6:
            try:
                a, b = pokeLookup()
                poke_team.append(a)
                types.append(b)
            except:
                print("Let's try again...")
                
            
        for pokemon in poke_team:
            print(pokemon.capitalize())

        print(types)

        return poke_team, types
            


main()

