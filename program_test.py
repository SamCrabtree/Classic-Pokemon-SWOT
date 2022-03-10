import json
import requests
import pandas


# GLOBAL VARIABLES
name = []
pokemon_team = []
pokemon_elements = []


# MAIN FUNCTION 
def main():

    print("Welcome to the Classic Pokemon SWOT Program! \n")
    build_Team()



#THIS FUNCTION ALLOWS YOU TO PICK YOUR TEAM OF 6 POKEMON

def build_Team():
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

# THIS PULLS ALL OF THE NAMES OF THE OG POKEMON

def listPokemon():
    all_api = "https://pokeapi.co/api/v2/pokemon?limit=151" 
    r = requests.get(all_api) 
    api_response = json.loads(r.text)
    pokemon_list = api_response['results']
    for pokemon in pokemon_list:
        print(pokemon['name'].capitalize())


# THIS FUNCTION PULLS THE INFORMATION FROM YOUR POKEMON SELECTION 

def pokeLookup():
    try:
        poke_request = input('What pokemon would you like to add to your team? OR  \n' )
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
        print("I couldn't find a match for that entry. If you are having trouble, type LIST to print a list of the Original 151 Pokemon and their spelling.")
        

    


# THIS FUNCTION GENERATES THE 
def swot_anaylzer():
  return






# THIS FUNCTION WILL GENERATE A PIE CHART ABOUT YOUR TEAMS ELEMENTAL MAKEUP.             
def team_makeup():
  return

# THIS FUNCTION GENERATES A PIE CHART ON WHAT ELEMENT POKEMON YOUR TEAM WILL HAVE AN ADVANTAGE AGAINST
def team_strength():
  return

# THIS FUNCTION GENERATES A PIE CHART ON WHAT ELEMENT POKEMON YOUR TEAM WILL STRUGGLE AGAINST
def team_weakness():
  return



# THIS ENSURES THE PROGRAM RUNS UPON LAUNCH 
main()


