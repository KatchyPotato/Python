
import time
import random

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
    "Rattata", "Spearow", "Ekans", "Pikachu", "Sandshrew", "Nidoran",
    "Clefairy", "Vulpix", "Jigglypuff", "Zubat", "Oddish", "Paras", "Venonat",
    "Diglett", "Meowth", "Psyduck", "Mankey", "Growlithe", "Poliwag", "Abra",
    "Machop", "Bellsprout", "Tentacool", "Geodude", "Ponyta", "Slowpoke",
    "Magnemite", "Doduo", "Seel", "Grimer", "Shellder", "Gastly",
    "Drowzee", "Krabby", "Exeggcute", "Cubone", "Koffing", "Rhyhorn",
    "Eevee", "Omanyte", "Kabuto", "Dratini"]

evolved_pokedex = ["Venusaur", "Charizard", "Blastoise", "Butterfree", "Beedrill", "Pidgeot",
    "Raticate", "Fearow", "Arbok", "Raichu", "Sandslash", "Nidoking",
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
        see_pokedex = input("\n\033[31mInvalid Pokemon! Would you like to see the basic Pokedex?\033[37m Yes/No").capitalize()

        if see_pokedex == "No":
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

        elif see_pokedex == "Yes":
            print("\n\033[37m" + str(basic_pokedex))
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

wins = 0
losses = 0
pokemon_level = 1
defence_level = 0
offence_level = 0
pokemon_status = "Basic"
health = 50
xp = 0

while running:
    print("\n\033[31m(\033[37m-O-\033[31m)\033[94m Actions \033[31m(\033[37m-O-\033[31m)\n\n\033[37m~\033[33mTrain\n\033[37m~\033[33mBattle\n\033[37m~\033[33mStats\033[37m")
    action = input("\n\033[94mEnter Action:\033[37m").capitalize()

    #First action, stats

    if action == "Stats":
        print(f"\n\033[95mTrainer Name:\033[37m {trainer_name}")
        print(f"\033[94mPokemon:\033[37m {pokemon}")
        print(f"\033[33mStatus:\033[37m {pokemon_status}")
        print(f"\033[92mPokemon Level:\033[37m {pokemon_level}/5")
        print(f"\033[95mXP:\033[37m {xp}/100")
        print(f"\033[31mOffence:\033[37m {offence_level}/50")
        print(f"\033[32mDefence:\033[37m {defence_level}/50")
        print(f"\033[91mHealth:\033[37m {health} HP")
        print(f"\033[92mWins:\033[37m {wins}")
        print(f"\033[31mLosses:\033[37m {losses}")
        if losses > 0:
            ratio = wins / losses
        else:
            ratio = "N.A."

        print(f"\033[93mWin/Loss Ratio:\033[37m {ratio}")
            

        back = ""
        while back != "Back":
            back = input("\n\033[37mType \"Back\" to Return to Actions").capitalize()

    elif action == "Train":

    #Second action, train

        train_type = ""
        while train_type != "Offence" and train_type != "Defence":
            train_type = input("\n\033[37mTrain\033[31m Offence\033[37m or\033[32m Defence\033[37m:").capitalize()

        if train_type == "Offence":
            word_bank = ["attack", "aggression", "assault", "barrage", "bombardment", "charge", "incursion",
                         "invasion", "onslaught", "raid", "strike", "violation", "agro", "AoE", "blitz", "waylay",
                         "melee", "foray", "siege", "enroachment", "strike", "coup", "flank", "volley", "agro"]

        elif train_type == "Defence":
            word_bank = ["defend", "protect", "heal", "sheild", "dodge", "counter", "cover", "resistance", "withstand", "duck", "jump", "dash",
                          "tank", "retrograde", "resist", "repel", "hold", "screen", "health", "armor", "escape", "mobility", "movement", "assist", "position"]


        train_help = ""
        while train_help != "Yes" and train_help != "No":
            train_help = input("\n\033[37mWould you like to see Traning Instructions? Yes/No:").capitalize()

        if train_help == "Yes":
            print("\n\033[37mType the words as they appear on the screen within the time boundaries\n\n\033[32mVALID:\033[37m Words typed correctly within time boundaries\n\033[31mINVALID:\033[37m Words typed incorectly, or outside of time boundaries") 

        elif train_help == "No":
            pass

        start = ""
        while start != "Go":
            start = input("\n\033[37mType \"Go\" to start Training:").capitalize()

        if start == "Go":

            valid = 0
            invalid = 0

            for x in range(10):
                word = random.choice(word_bank)
                print("\n\033[95m" + word)
                start_time = time.time()
                typed = input("\n\033[37mType Here:").lower()
                end_time = time.time()

                elapsed_time = round(end_time - start_time)

                if elapsed_time <= 3 and typed == word:
                    valid += 1

                else:
                    invalid += 1

        print(f"\n\n\033[37mRESULTS:\n\n\033[32mVALID: {valid}\n\033[31mINVALID: {invalid}")

        if train_type == "Offence":
            print(f"\n\033[31mOffence\033[37m Levels Gained: {valid}")
            offence_level += valid

        elif train_type == "Defence":
            print(f"\n\033[32mDefence\033[37m Levels Gained: {valid}")
            defence_level += valid

        print(f"\033[95mXP\033[37m Levels Gained: {valid}")
        xp += valid
        

        back = ""
        while back != "Back":
            back = input("\n\033[37mType \"Back\" to Return to Actions").capitalize()

        
        

        
