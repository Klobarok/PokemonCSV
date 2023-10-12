import requests
import csv


pokemon_data = []
base_url = "https://pokeapi.co/api/v2/pokemon/"
filename = "pokemon151.csv"
fieldNames = ['ID','Name', 'Type', 'hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']


for i in range(1, 152):
    response = requests.get(base_url + str(i))

    if response.status_code != 200:
        print(f"Failed to retrieve data for Pokemon with ID {i}.")
        continue

    data = response.json()

    name = data['name'].capitalize()
    types = "/".join(t['type']['name'].capitalize() for t in data['types'])  # Get all types
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}  # Get all stats

    pokemon_data.append({
        'ID':i,
        'Name': name,
        'Type': types,
        **stats
    })

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

    writer.writeheader()

    for pokemon in pokemon_data:
        writer.writerow(pokemon)