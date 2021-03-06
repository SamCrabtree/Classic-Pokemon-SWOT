import os
import json
import requests
import matplotlib.pyplot as plt


# MAIN FUNCTION 

def main():
    myTeam,myElements = build_Team()
    team = myTeam    
    buildup = team_makeup(myElements)
    weaknesses = team_weakness(buildup)
    strengths = team_strength(buildup)
    swot_anaylzer(buildup, weaknesses, strengths)
    print('That looks like a solid team! Let\'s Try again!\n')
    repeat()

#THIS FUNCTION COLLECTS THE NAME AND ELEMENTS OF USER POKEMON CHOICES VIA THE POKE LOOKUP
def build_Team():
        team = []
        type = []
        while len(team) < 6:
            try:
                a, b = pokeLookup()
                team.append(a)
                type.append(b)
            except:
                print("Let's try again...")          
        return team, type


# THIS FUNCTION PULLS THE INFORMATION FROM YOUR POKEMON SELECTION AND PASSES IT BACK THE THE BUILD TEAM FUNCTION
def pokeLookup(): 
    try:
        poke_request = input('\n What pokemon would you like to add to your team? \n' )
        if poke_request.lower() == "list":
            listPokemon()
            pokeLookup()

        else:
            individual_api = "https://pokeapi.co/api/v2/pokemon/" + poke_request.lower() + "/"    
            response = requests.get(individual_api)
            poke_data = json.loads(response.text)
            pokemon_name = poke_data['species']['name']
            pokemon_type = poke_data['types'][0]['type']['name']
            print("\n I see you chose " + pokemon_name.capitalize() + " a " + pokemon_type.capitalize() + " pokemon. Great choice! \n")
        return pokemon_name, pokemon_type

    except:
        print("I couldn't find a match for that entry. If you are having trouble, type LIST to print a list of the Original 151 Pokemon and their correct spelling. \n")

# THIS PULLS ALL OF THE NAMES OF THE OG POKEMON IF NEEDED
def listPokemon():
    all_api = "https://pokeapi.co/api/v2/pokemon?limit=151" 
    r = requests.get(all_api) 
    api_response = json.loads(r.text)
    pokemon_list = api_response['results']
    for pokemon in pokemon_list:
        print(pokemon['name'].capitalize())

# THIS FUNCTION WILL GENERATE A PIE CHART ABOUT YOUR TEAMS ELEMENTAL MAKEUP.             
def team_makeup(type_list):
  normal_ct = type_list.count('normal')
  fire_ct  = type_list.count('fire')
  water_ct = type_list.count('water')
  grass_ct = type_list.count('grass')
  electric_ct = type_list.count('electric')
  ice_ct = type_list.count('ice')
  fighting_ct = type_list.count('fighting')
  poison_ct = type_list.count('poison')
  ground_ct = type_list.count('ground')
  flying_ct = type_list.count('flying')
  psychic_ct = type_list.count('psychic')
  bug_ct  = type_list.count('bug')
  rock_ct = type_list.count('rock')
  ghost_ct = type_list.count('ghost')
  dragon_ct = type_list.count('dragon')
  poke_ct = [ normal_ct, fire_ct, water_ct, grass_ct, electric_ct, ice_ct, fighting_ct, poison_ct, 
  ground_ct, flying_ct, psychic_ct, bug_ct, rock_ct, ghost_ct, dragon_ct ]
  return poke_ct

# THIS FUNCTION GENERATES A PIE CHART ON WHAT ELEMENT POKEMON YOUR TEAM WILL HAVE AN ADVANTAGE AGAINST
def team_strength(build):
  normal_str = 0
  fire_str = build[3] + build[5] + build[11]
  water_str = build[1] + build[8] + build[14]
  grass_str = build[2] + build[8] + build[12]
  electric_str = build[2] + build[9]
  ice_str = build[3] + build[9] + build[14]
  fighting_str = build[0] + build[4] + build[12]
  poison_str = build[3] + build[11]
  ground_str = build[1] + build[12] + (build[4] * 2)
  flying_str = build[3] + build[6] + build[11] + (build[8] * 2)
  psychic_str = build[6] + build[7]
  bug_str = build[3] + build[7] + build[10]
  rock_str = build[1] + build[5] + build[9] + build[11]
  ghost_str = build[13] + (build[0] * 2) + (build[6] * 2)
  dragon_str = build[14]
  poke_str = [ normal_str, fire_str, water_str, grass_str, electric_str, ice_str, fighting_str, poison_str, 
  ground_str, flying_str, psychic_str, bug_str, rock_str, ghost_str, dragon_str ]
  return poke_str

# THIS FUNCTION GENERATES A PIE CHART ON WHAT ELEMENT POKEMON YOUR TEAM WILL STRUGGLE AGAINST
def team_weakness(build):
  normal_wk = (build[13] * 2) + build[12]
  fire_wk = build[1] + build[2] + build[12] + build[14] 
  water_wk = build[2] + build[3] + build[14]
  grass_wk = build[1] + build[3] + build[7] + build[9] + build[11] + build[14]
  electric_wk = build[4] + build[3] + build[14] + (build[12] * 2)
  ice_wk = build[1] + build[5]
  fighting_wk = build[7] + build[9] + build[10] + build[11] + (build[13] * 2)
  poison_wk = build[7] + build[8] + build[12] + build[13]
  ground_wk = build[3] + build[11] + (build[9] * 2)
  flying_wk = build[4] + build[12]
  psychic_wk = build[10]
  bug_wk = build[1] + build[6] + build[9] + build[13]
  rock_wk = build[6] + build[8]
  ghost_wk = 0
  dragon_wk = 0
  poke_wk = [ normal_wk, fire_wk, water_wk, grass_wk, electric_wk, ice_wk, fighting_wk, poison_wk, 
  ground_wk, flying_wk, psychic_wk, bug_wk, rock_wk, ghost_wk, dragon_wk ]
  return poke_wk

# THIS FUNCTION GENERATES THE STRENGTH AND WEAKNESS COUNTS AND THEN PLOTS THE RESULTS TO THREE SEPERATE PIE CHARTS
def swot_anaylzer(count, strength, weakness):
  list_elements = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon']
  colors = ['lavenderblush', 'firebrick', 'royalblue', 'forestgreen', 'yellow', 'mediumblue', 'saddlebrown', 'black', 'peru', 'cornflowerblue', 'darkviolet', 'darkgreen', 'slategray', 'ghostwhite', 'silver']
  team_make_up = count
  explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
  team_strengths = strength
  team_weaknesses = weakness
  

  Team_Make_Up, ax1 = plt.subplots()
  ax1.pie(team_make_up, labels=list_elements, colors=colors, explode=explode, autopct='%1.1f%%', shadow=False, startangle=90)
  ax1.axis('equal')
  plt.title("Check Out Your Pokemon Build!", bbox={'facecolor':'0.8', 'pad':5})
  plt.legend()
  

  Team_Strengths, ax1 = plt.subplots()
  ax1.pie(team_strengths, labels=list_elements, colors=colors, explode=explode, autopct='%1.1f%%', shadow=False, startangle=90)
  ax1.axis('equal')
  plt.title("Your Pokemon Team Is Most Effective Against...\n" + "(Deal heavy damage for elements with higher percentages!)", bbox={'facecolor':'0.8', 'pad':5})
  plt.legend()
  plt.figure(1)
  
  Team_Weaknesses, ax1 = plt.subplots()
  ax1.pie(team_weaknesses, labels=list_elements, colors=colors, explode=explode, autopct='%1.1f%%', shadow=False, startangle=90)
  ax1.axis('equal')
  plt.title("Your Pokemon Team Is Most Vunerable To...\n" + "(Look out for elements with higher percentages!)", bbox={'facecolor':'0.8', 'pad':5})
  plt.legend()
  plt.figure(2)
  plt.show()
  return

# THIS FUNCTION ASKS THE USER IF THEY WANT TO RUN THE LOOP AGAIN. IF NOT THE PROGRAM WILL CLOSE. 
def repeat():
    answer = input('Would you like to create another team? If yes, type "Y"')
    if answer == 'Y':
        main()
    else:
        print('Thanks for playing! Smell ya later!\n')
        os._exit(0)

# THIS ENSURES THE PROGRAM RUNS UPON LAUNCH 
print("Welcome to the Classic Pokemon SWOT Program! \n")
main()