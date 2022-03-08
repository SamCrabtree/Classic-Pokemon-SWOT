import requests
import pandas

def main():
    team()
    
def list():
    all_api = "https://pokeapi.co/api/v2/pokemon?limit=151" 
    all_pokemon = requests.get(all_api) 
    all_results = all_pokemon.json() as f 

def pokeLookup():
    poke_request = input("What pokemon would you like to add to your team? ")
    pokemon = poke_request
    api_url = "https://pokeapi.co/api/v2/pokemon/" + poke_request.lower() + "/"
    
    response = requests.get(api_url)

    results = str(response.json())
    print(all_results + "I see you chose " + pokemon.capitalize() + ". Great choice!")
    return pokemon, results 

def team():
        count = 0
        while count < 6:
            pokeLookup()
            count = count +1
        else:
            print('Your team ')
            
      
            




main()

