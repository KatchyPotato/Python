
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

time.sleep(0.05)

pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()
if pokemon not in basic_pokedex:

    while pokemon not in basic_pokedex:
        time.sleep(0.05)
        see_pokedex = input("\n\033[31mInvalid Pokemon! Would you like to see the basic Pokedex?\033[37m Yes/No").capitalize()

        if see_pokedex == "No":
            time.sleep(0.05)
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

        elif see_pokedex == "Yes":
            time.sleep(0.05)
            print("\n\033[37m" + str(basic_pokedex))
            time.sleep(0.05)
            pokemon = input("\n\033[33mEnter Basic Gen 1 Pokemon:\033[37m").capitalize()

wins = 0
losses = 0
pokemon_level = 1
defense_level = 0
offence_level = 0
pokemon_status = "Basic"
health = 50
xp = 0

while running:

    time.sleep(0.05)
    print("\n\033[31m(\033[37m-O-\033[31m)\033[94m Actions \033[31m(\033[37m-O-\033[31m)\n\n\033[37m~\033[33mTrain\n\033[37m~\033[33mBattle\n\033[37m~\033[33mStats\033[37m")
    time.sleep(0.05)
    action = input("\n\033[94mEnter Action:\033[37m").capitalize()

    #First action, stats

    if action == "Stats":
        time.sleep(0.05)
        print(f"\n\033[95mTrainer Name:\033[37m {trainer_name}")
        time.sleep(0.05)
        print(f"\033[94mPokemon:\033[37m {pokemon}")
        time.sleep(0.05)
        print(f"\033[33mStatus:\033[37m {pokemon_status}")
        if pokemon_status == "Basic":
            time.sleep(0.05)
            print(f"\033[92mPokemon Level:\033[37m {pokemon_level}/5")
        elif pokemon_status == "Evolved":
            time.sleep(0.05)
            print(f"\033[92mPokemon Level:\033[37m {pokemon_level}/10")
            
        time.sleep(0.05)
        print(f"\033[95mXP:\033[37m {xp}/100")
        if pokemon_status == "Basic":
            time.sleep(0.05)
            print(f"\033[31mOffence:\033[37m {offence_level}/20")
        elif pokemon_status == "Evolved":
            time.sleep(0.05)
            print(f"\033[31mOffence:\033[37m {offence_level}/50")
        if pokemon_status == "Basic":
            time.sleep(0.05)
            print(f"\033[32mDefence:\033[37m {defense_level}/20")
        elif pokemon_status == "Evolved":
            time.sleep(0.05)
            print(f"\033[32mDefence:\033[37m {defense_level}/50")
        time.sleep(0.05)
        print(f"\033[91mHealth:\033[37m {health} HP")
        time.sleep(0.05)
        print(f"\033[92mWins:\033[37m {wins}")
        time.sleep(0.05)
        print(f"\033[31mLosses:\033[37m {losses}")
        if losses > 0:
            ratio = round(wins / losses, 1)
        else:
            ratio = "N.A."
        time.sleep(0.05)
        print(f"\033[93mWin/Loss Ratio:\033[37m {ratio}")
            

        back = ""
        while back != "Back":
            time.sleep(0.05)
            back = input("\n\033[37mType \"Back\" to return to actions").capitalize()

    elif action == "Train":

    #Second action, train

        train_type = ""
        while train_type != "Offence" and train_type != "Defense":
            time.sleep(0.05)
            train_type = input("\n\033[37mTrain\033[31m Offence\033[37m or\033[32m Defense\033[37m:").capitalize()

        if train_type == "Offence":
            word_bank = ["attack", "aggression", "assault", "barrage", "bombardment", "charge", "incursion",
                         "invasion", "onslaught", "raid", "strike", "violation", "agro", "aoe", "blitz", "waylay",
                         "melee", "foray", "siege", "enroachment", "strike", "coup", "flank", "volley", "agro"]

        elif train_type == "Defense":
            word_bank = ["defend", "protect", "heal", "sheild", "dodge", "counter", "cover", "resistance", "withstand", "duck", "jump", "dash",
                          "tank", "retrograde", "resist", "repel", "hold", "screen", "health", "armor", "escape", "mobility", "movement", "assist", "position"]


        train_help = ""
        while train_help != "Yes" and train_help != "No":
            time.sleep(0.05)
            train_help = input("\n\033[37mWould you like to see Traning Instructions? Yes/No:").capitalize()

        if train_help == "Yes":
            time.sleep(0.05)
            print("\n\033[37mType the words as they appear on the screen within the time boundaries\n\n\033[32mVALID:\033[37m Words typed correctly within time boundaries\n\033[31mINVALID:\033[37m Words typed incorectly, or outside of time boundaries") 

        elif train_help == "No":
            pass

        start = ""
        while start != "Go":
            time.sleep(0.05)
            start = input("\n\033[37mType \"Go\" to start Training:").capitalize()

        if start == "Go":

            valid = 0
            invalid = 0

            for x in range(10):
                word = random.choice(word_bank)
                time.sleep(0.05)
                print("\n\033[95m" + word)
                start_time = time.time()
                time.sleep(0.05)
                typed = input("\n\033[37mType Here:").lower()
                end_time = time.time()

                elapsed_time = round(end_time - start_time)

                if elapsed_time <= 3 and typed == word:
                    valid += 1

                else:
                    invalid += 1
        time.sleep(0.05)
        print(f"\n\n\033[37mRESULTS:\n\n\033[32mVALID: {valid}\n\033[31mINVALID: {invalid}")

        if train_type == "Offence":
            time.sleep(0.05)
            print(f"\n\033[31mOffence\033[37m Levels Gained: {round(valid / 3)}")
            offence_level += round(valid / 3)

        elif train_type == "Defense":
            time.sleep(0.05)
            print(f"\n\033[32mDefense\033[37m Levels Gained: {round(valid / 3)}")
            defense_level += round(valid / 3)
        time.sleep(0.05)
        print(f"\033[95mXP\033[37m Levels Gained: {valid}")
        xp += valid
        

        
        back = ""
        while back != "Back":
            time.sleep(0.05)
            back = input("\n\033[37mType \"Back\" to return to actions").capitalize()
        

    elif action == "Battle":

        #Third action, battle

        time.sleep(0.05)

        difficulty = ""
        while difficulty != "Normal" and difficulty != "Hard":
            difficulty = input("\n\033[92mNormal\033[37m or\033[31m Hard\033[37m?").capitalize()

        if difficulty == "Normal":
            opponent = random.choice(basic_pokedex)
            opponent_health = 50
            opponent_attack = 10

        elif difficulty == "Hard":
            opponent = random.choice(evolved_pokedex)
            opponent_health = 150
            opponent_attack = 15

        battle_health = health
        battle_attack = offence_level
        heal_strength = defense_level
        heals_left = 3
        min_damage = battle_attack
        max_damage = battle_attack + 5
        opponent_min_damage = opponent_attack
        opponent_max_damage = opponent_attack + 5

        while battle_health > 0 and opponent_health > 0:
            time.sleep(0.05)
            print(f"\n\033[95mOpponent:\033[37m {opponent}")
            time.sleep(0.05)
            print(f"\033[92mHealth:\033[37m {opponent_health} HP")
            time.sleep(0.05)
            print(f"\033[31mAttack:\033[37m {opponent_attack}")
            time.sleep(0.05)
            print("\n\033[31m(\033[37m-O-\033[31m)\033[94m Battle Actions \033[31m(\033[37m-O-\033[31m)\n\n\033[37m~\033[33mAttack\n\033[37m~\033[33mHeal\n\033[37m~\033[33mStats\033[37m")

            battle_action = ""
            while battle_action != "Attack" and battle_action != "Heal" and battle_action != "Stats":
                time.sleep(0.05)
                battle_action = input("\n\033[94mEnter Battle Action:\033[37m").capitalize()

            #First battle action, stats

            if battle_action == "Stats":
                time.sleep(0.05)
                print(f"\n\033[94mPokemon:\033[37m {pokemon}")
                time.sleep(0.05)
                print(f"\033[91mHealth:\033[37m {battle_health} HP")
                time.sleep(0.05)
                print(f"\033[31mAttack:\033[37m {battle_attack}")
                time.sleep(0.05)
                print(f"\033[92mHeals Left:\033[37m {heals_left}")
                time.sleep(0.05)
                print(f"\033[32mHeal Strength:\033[37m {heal_strength} HP")

                end_turn = ""
                while end_turn != "Done":
                    time.sleep(0.05)
                    end_turn = input("\n\033[37mType \"Done\" to end turn").capitalize()

            #Second battle action, heal

            elif battle_action == "Heal":
                if heals_left > 0:
                    if battle_health == health:
                        time.sleep(0.05)
                        print("\n\033[37mYou are already at max health!")

                    elif battle_health < health:
                        battle_health += heal_strength
                        time.sleep(0.05)
                        print("\n\033[37mPokemon Healed")

                        if battle_health > health:
                            battle_health = health
                            
                        else:
                            pass
                        heals_left -= 1
                        
                else:
                    time.sleep(0.05)
                    print("\n\033[37mYou have used up all your heals!")

                end_turn = ""
                while end_turn != "Done":
                    time.sleep(0.05)
                    end_turn = input("\n\033[37mType \"Done\" to end turn").capitalize()

            #Third battle action, attack

            elif battle_action == "Attack":
                damage_dealt = random.randint(min_damage, max_damage)
                opponent_health -= damage_dealt
                time.sleep(0.05)
                print(f"\n\033[37m{pokemon} dealt {damage_dealt} damage to {opponent}")

                end_turn = ""
                while end_turn != "Done":
                    time.sleep(0.05)
                    end_turn = input("\n\033[37mType \"Done\" to end turn").capitalize()

            #Opponent Turn

            opponent_damage_dealt = random.randint(opponent_min_damage, opponent_max_damage)
            battle_health -= opponent_damage_dealt
            time.sleep(0.05)
            print(f"\n\033[37m{opponent} dealt {opponent_damage_dealt} damage to {pokemon}")
            time.sleep(0.05)
            print(f"\033[91mYour Health:\033[37m {battle_health} HP")

        #Results
                
        see_results = ""
        while see_results != "Done":
            time.sleep(0.05)
            see_results = input("\n\033[37mBattle over. Type \"Done\" to see results").capitalize()

        if opponent_health < battle_health:
            time.sleep(0.05)
            print("\n\033[33mResults:")
            time.sleep(0.05)
            print("\033[32mWin!")
            time.sleep(0.05)
            if opponent in evolved_pokedex:
                print(f"\033[95mXP\033[37m Levels Gained: 15")
            elif opponent in basic_pokedex:
                print(f"\033[95mXP\033[37m Levels Gained: 10")
            xp += 10
            wins += 1

        elif battle_health < opponent_health:
            time.sleep(0.05)
            print("\n\033[33mResults:")
            time.sleep(0.05)
            print("\033[31mLoss!")
            time.sleep(0.05)
            print(f"\033[95mXP\033[37m Levels Gained: 0")
            losses += 1

        elif battle_health == opponent_health:
            time.sleep(0.05)
            print("\n\033[33mResults:")
            time.sleep(0.05)
            print("\033[95mDraw!")
            time.sleep(0.05)
            print(f"\033[95mXP\033[37m Levels Gained: 5")

        
        back = ""
        while back != "Back":
            time.sleep(0.05)
            back = input("\n\033[37mType \"Back\" to return to actions").capitalize()

    #Final stats check

    if xp >= 100:
        pokemon_level += 1
        time.sleep(0.05)
        print(f"\n\033[95mYou gained 100 XP!\033[37m Your pokemon is now level {pokemon_level}")
        time.sleep(0.05)
        print("\033[37mXP reset")
        xp = 0

    if pokemon_status == "Basic" and pokemon_level == 5:
        print(f"\n\033[93mYou gained 5 levels!\033[37m Your pokemon evolved from {pokemon} to {evolved_pokedex[basic_pokedex.index(pokemon)]}")
        time.sleep(0.05)
        print("\033[37mStats upgraded. You can now gain more offence and defense levels")
        pokemon_status = "Evolved"
        pokemon = evolved_pokedex[basic_pokedex.index(pokemon)]
        health = 100 

    if pokemon_status == "Basic":
        if offence_level > 20:
            offence_level = 20
        if defense_level > 20:
            defense_level = 20
        if pokemon_level > 5:
            pokemon_level = 5


    elif pokemon_status == "Evolved":
        if offence_level > 50:
            offence_level = 50
        if defense_level > 50:
            defense_level = 50
        if pokemon_level > 10:
            pokemon_level = 10       
