#Task 1 set up Virtual environment and install requests
#Task 2 Fetch data from a space API

import requests
import json

def fetch_planet_data():
    list_of_planets = []
    url = 'https://api.le-systeme-solaire.net/rest/bodies'
    try:
        response = requests.get(url)
        json_object = response.json()
        if isinstance(json_object, dict):
            for body in json_object['bodies']:
                if body['isPlanet'] == True:
                    # name = body.get('englishName')
                    # mass = body.get('mass').get('massValue')
                    # mass_exponent = body.get('mass').get('massExponent')
                    # orbit_period = body.get('sideralOrbit')
                    #print(f"Name: {name},\tMass: {str(mass)} * 10 to the {str(mass_exponent)} power,\tOrbit Period: {str(orbit_period)} days")
                    list_of_planets.append(body)
            return list_of_planets
        else:
            issue = json_object.get('status')
            reason_why = json_object.get('reason', 'unknown error')
            print(f"Error {issue}: {reason_why}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}") 
print("\n")
# fetch_planet_data()
'''
fetch_planet_data works by taking the space API url and using the requests pip to retrieve the information before the json module converts it into a python object. The structure of the Space API
is a list of bodies inside a larger dictionary structure and each body in the list has its own nested dictionary. Once we confirm our converted json object is the outer dictionary we loop through the 'bodies' list inside of it and if the 'isPlanet' key in the nested dictionary has a true value
We will retrieve data from it. I then use the .get() method to return the nested values for name, mass value, mass exponent, and orbital period and print them in an f-string. I have error handling if the API returns as not a list or if there is an issue with our requests pip.
'''

#Task 3 Data Presentation and Analysis

def find_heaviest_planet(list_of_planets):
    planet_mass_dict = {}
    for planet in list_of_planets:
        mass_value = planet.get('mass').get('massValue')
        mass_exponent = planet.get('mass').get('massExponent')
        mass = float(mass_value)* (10 ** float(mass_exponent))
        name = planet.get('englishName')
        planet_mass_dict[name] = mass
    heaviest_planet_mass = max(planet_mass_dict.values())
    for key, value in planet_mass_dict.items():
        if value == heaviest_planet_mass:
            heaviest_planet_name = key    
    return heaviest_planet_name, heaviest_planet_mass

'''
This function works by instantiating a temporary dictionary where name will be the key and mass will be the value.
I then loop through every planet in the list that we are inputing and use the .get method to retrieve mass value and mass exponent which are used to then calculate the mass (mass_value * 10**mass_exponent)
I then use a getter for name and assign the name and the mass we calculated as a key value pair in our temporary dictionary.
I assign heaviest_planet_mass using the built in max function on the temporary dictionary.values() method.
I then retrieve that planets name by looping through the key, value pair in the .items method assigning the key to heaviest_name when value is equal to the heaviest_mass variable we just assigned. I then return both heaviest_name and heaviest_variable values. 
'''

for planet in fetch_planet_data():
    print(f"Name: {planet.get('englishName')},\tMass: {str(planet.get('mass').get('massValue'))} * 10 to the {str(planet.get('mass').get('massExponent'))} power,\tOrbit Period: {str(planet.get('sideralOrbit'))} days")

name, mass = find_heaviest_planet(fetch_planet_data())

print(f"\nThe heaviest planet is {name} at a mass of {str(mass)}")


def longest_orbit_period(list_of_planets):
    orbit_dict = {}
    for planet in list_of_planets:
        planet_name = planet.get('englishName')
        planet_orbit = planet.get('sideralOrbit')
        orbit_dict[planet_name] = planet_orbit
    longest_orbit = max(orbit_dict.values())
    for key, value in orbit_dict.items():
        if value == longest_orbit:
            longest_orbit_name = key
    return longest_orbit_name, longest_orbit

'''
longest_orbit_period works very similarly to th heaviest_planet function. We instantiate a temporary dictionary and then loop through the input, a list of dictionaries.
We use the .get() method on the nested dictionaries to retrieve name and orbit information and ake that the key, value pair inside our dictionary.
I then assign longest_orbit by using the built in max function on the orbit_dict.values() list. I lastly then use the .items() method and a conditional matching the values we are looping through with the max we just assigned,
to then assign that value's key to the longest_orbit_name variable. I then return both longest_orbit_name and longest_orbit 
'''

orbit_name, long_orbit = longest_orbit_period(fetch_planet_data())
print(f"\n{orbit_name} has the longest orbit period at {str(long_orbit)} days")