#Task 1 set up Virtual environment and install requests
#Task 2 Fetching Data from Pokemon API

import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

pikachu_data = json.loads(json_data)
#This code retrieves data from the Pokemon API and then converts it from JSON into a Python object

print(f"Name: {pikachu_data['name'].title()}")
for index, ability in enumerate(pikachu_data['abilities'], 1):
    print(f"Ability {str(index)}: {ability.get('ability').get('name').title()}")
print("\n")
#This f-string navigates through the Python object we retrieved accessing the appropriate dictionary key value pair and list indices

# Task 3 Analyzing and Displaying Data

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        pokemon = response.json()

        if isinstance(pokemon, dict):
            name = pokemon['name'].title()
            list_of_abilities = pokemon['abilities']
            weight = pokemon['weight']
            print(f"Name: {name}")
            for index, ability in enumerate(list_of_abilities, 1):
                print(f"Ability {str(index)}: {ability.get('ability').get('name').title()}")
            print(f"Weight: {str(weight)}\n")
        else:
            issue = pokemon.get('status')
            reason_why = pokemon.get('reason', 'unknown error')
            print(f"Error {issue}: {reason_why}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}") 

'''
fetch_pokemon_data inserts the name of the pokemon into its appropriate place in the pokeapi url.
Then in a try, except block it uses the requests pip to retrieve the api's invofmration and using the .json method converts the json encoded content into
a python object. I then ensure that there is no errors by checking in isinstance that the information returns as a dictionary.
I then navigate through the dictionary to retrieve values for name, list of abilities, and weight. I print each in an f-string, and specifically
I use the enumerate function to loop through the list of abilities while using two .get() methods to access ability names in our f-string as ability name is a dictionary nested inside another dictionary inside a list inside the outer dictionary.
In the else and except blocks I catch any unexpected errors.
'''

def calculate_average_weight(list_of_pokemon):
    pokemon_weight_list = []
    for pokemon_name in list_of_pokemon:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        try:
            response = requests.get(url)
            pokemon_json = response.json()
            if isinstance(pokemon_json, dict):
                pokemon_weight_list.append(int(pokemon_json['weight']))
            else:
                issue = pokemon.get('status')
                reason_why = pokemon.get('reason', 'unknown error')
                print(f"Error {issue}: {reason_why}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    average_weight = sum(pokemon_weight_list)/len(pokemon_weight_list)
    return average_weight
'''
calculate_average_weight uses the same syntax as fetch_pokemon_data to retrieve the json object and convert it into a python object but deviates slightly as instantiate a list of weights before I navigate the API,
and once I access the API instead of printing it's info I simply append the weight to our newly instantiated list. I also ensure that the value I am retrieving from the API dictionary is in integer type.
In the else and except blocks I catch any unexpected errors. Lastly I calculate average weight by using the sum function on our list and then dividing the sum by the list's length. I then return that output.
'''

pokemon_list = ['charizard', 'squirtle', 'mew']
for pokemon in pokemon_list:
    fetch_pokemon_data(pokemon)

#I loop through my list of pokemon calling fetch_pokemon_data on each item

print(f"Average Weight: {calculate_average_weight(pokemon_list)}")

# Here I call calculate_aerage_weight on the entire list but as it has a return instead of a print output I wrap the function call in its own print statement