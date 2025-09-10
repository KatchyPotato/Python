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

pokemon = input("\n\033[33mIEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

if pokemon not in basic_pokedex:

    while pokemon not in basic_pokedex:
        see_pokedex = input("\n\033[31mInvalid Pokemon! Would you like to see the basic Pokedex? Yes / No\033[37m")

        if see_pokedex == "No":
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m")

        elif see_pokedex == "Yes":
            print("\n\033[37m" + str(basic_pokedex))
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m")

pokemon_level = 1
defence_level = 1
offence_level = 1

while running:
    print("\n\033[31mC\033[37m-O-\033[31mD\033[94m Actions \033[31mC\033[37m-O-\033[31mD\n\033[37m~\033[33mTrain\n\033[37m~\033[33mFight\n\033[37m~\033[33mStats\033[37m")
    action = input("\n\033[94mEnter Action:\033[37m")

    #if action = "Stats":
        #print(f"\n\033[33mPokemon:\033[37m 
            
        
