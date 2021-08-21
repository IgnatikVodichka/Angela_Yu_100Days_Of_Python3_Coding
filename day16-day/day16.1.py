from prettytable import PrettyTable  # special package from pypi.org installed for tables.


pokemon_table = PrettyTable()
pokemon_table.add_column("Pokemon name", ["Pikatchu", "Squirtle", "Charmander"])
pokemon_table.add_column("Pokemon type", ["Electric", "Water", "Fire"])

pokemon_table.align = "l"  # aligning the data in table 'l' - left and 'r' for right

print(pokemon_table)
