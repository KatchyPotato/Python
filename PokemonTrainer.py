print("\n\033[31m(\033[37m-O-\033[31m)\033[94m Pokemon Trainer \033[31m(\033[37m-O-\033[31m)")

running = True

#ChatGPT generated ANSI color code list

colors = {
    "reset": "\033[0m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

#ChatGPT generated pokemon lists

basic_pokedex =["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey",
    "Rattata", "Spearow", "Ekans", "Pikachu", "Sandshrew", "Nidoran♀", "Nidoran♂",
    "Clefairy", "Vulpix", "Jigglypuff", "Zubat", "Oddish", "Paras", "Venonat",
    "Diglett", "Meowth", "Psyduck", "Mankey", "Growlithe", "Poliwag", "Abra",
    "Machop", "Bellsprout", "Tentacool", "Geodude", "Ponyta", "Slowpoke",
    "Magnemite", "Doduo", "Seel", "Grimer", "Shellder", "Gastly",
    "Drowzee", "Krabby", "Exeggcute", "Cubone", "Koffing", "Rhyhorn",
    "Eevee", "Omanyte", "Kabuto", "Dratini"]

evolved_pokedex = ["Venusaur", "Charizard", "Blastoise", "Butterfree", "Beedrill", "Pidgeot",
    "Raticate", "Fearow", "Arbok", "Raichu", "Sandslash", "Nidoqueen", "Nidoking",
    "Clefable", "Ninetales", "Wigglytuff", "Golbat", "Vileplume", "Parasect", "Venomoth",
    "Dugtrio", "Persian", "Golduck", "Primeape", "Arcanine", "Poliwrath", "Alakazam",
    "Machamp", "Victreebel", "Tentacruel", "Golem", "Rapidash", "Slowbro",
    "Magneton", "Dodrio", "Dewgong", "Muk", "Cloyster", "Gengar",
    "Hypno", "Kingler", "Exeggutor", "Marowak", "Weezing", "Rhydon",
    "Vaporeon", "Omastar", "Kabutops", "Dragonite"]



trainer_name = input("\n\033[33mEnter Trainer Name:\033[37m")

pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()
if pokemon not in basic_pokedex:

    while pokemon not in basic_pokedex:
        see_pokedex = input("\n\033[31mInvalid Pokemon! Would you like to see the basic Pokedex? Yes / No\033[37m").capitalize()

        if see_pokedex == "No":
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

        elif see_pokedex == "Yes":
            print("\n\033[37m" + str(basic_pokedex))
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

pokemon_level = 1
defence_level = 1
offence_level = 1
pokemon_status = "Basic"
health = 50

while running:
    print("\n\033[31m(\033[37m-O-\033[31m)\033[94m Actions \033[31m(\033[37m-O-\033[31m)\n\n\033[37m~\033[33mTrain\n\033[37m~\033[33mFight\n\033[37m~\033[33mStats\033[37m")
    action = input("\n\033[94mEnter Action:\033[37m").capitalize()

    if action == "Stats":
        print(f"\n\033[95mTrainer Name:\033[37m {trainer_name}")
        print(f"\033[94mPokemon:\033[37m {pokemon}")
        print(f"\033[33mStatus:\033[37m {pokemon_status}")
        print(f"\033[92mPokemon Level:\033[37m {pokemon_level}/10")
        print(f"\033[31mOffence:\033[37m {offence_level}/5")
        print(f"\033[32mDefence:\033[37m {defence_level}/5")
        print(f"\033[91mHealth:\033[37m {health} HP")

        back = ""
        while back != "Back":
            back = input("\n\033[37mType \"Back\" to Return to Actions").capitalize()

        
