# Pokémon Data Scraper

## Description

This Python script fetches data for the original 151 Pokémon from the [PokéAPI](https://pokeapi.co/) and writes it to a CSV file. The data includes the Pokémon's ID, name, type(s), and base stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed).

## How to Use

### Prerequisites

- Python 3.x
- `requests` library

### Steps

1. **Clone the Repository:**
    ```shell
    git clone https://github.com/Klobarok/PokemonCSV
    ```

2. **Install Dependencies:**
    ```shell
    pip install requests
    ```
3. **Run the Script:**
    ```shell
    python script_name.py
    ```
    Replace `script_name.py` with the name of your Python file.

### Output

- A CSV file named `pokemon151.csv` containing data for the first 151 Pokémon.

## Data Format

- **ID:** The Pokémon's ID from 1 to 151.
- **Name:** The Pokémon's name.
- **Type:** The Pokémon's type(s). If a Pokémon has two types, they are separated by a slash.
- **hp, attack, defense, special-attack, special-defense, speed:** The Pokémon's base stats.

## Error Handling

- If the script fails to retrieve data for a particular Pokémon, it will print an error message and continue to the next one.

## Disclaimer

This script uses [PokéAPI](https://pokeapi.co/). Ensure to comply with their usage guidelines and use the data responsibly and ethically.
