
import random
import time
import random

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

print("\033[90mDungeons & Dice")
time.sleep(0.05)
print("\nInstructions:")
time.sleep(0.05)
print("\n\033[32m~Even Roll:\033[90m Attack Opponent")
time.sleep(0.05)
print("\033[31m~Odd Roll:\033[90m Opponent Attacks")
time.sleep(0.05)
print("\033[92m~Heal:\033[90m Restore Health")
time.sleep(0.05)

name = input("\n\033[90mEnter Name:")
time.sleep(0.05)
opponent_name = input("Enter Opponent Name:")

player_health = 50
opponent_health = 50
heals_left = 3

while player_health and opponent_health > 0:
    time.sleep(0.05)
    print("\n\033[90m~Actions~")
    time.sleep(0.05)
    print("Roll Dice")
    time.sleep(0.05)
    print(f"Heal [{heals_left} left]")
    time.sleep(0.05)
    print(f"Your HP:\033[92m {player_health}")
    time.sleep(0.05)
    print(f"\033[90mOpponent HP:\033[91m {opponent_health}")

    action = input("\n\033[90mEnter Action:").title()
    while action not in ["Heal", "Roll Dice"]:
        time.sleep(0.05)
        action = input("Enter Action:").title()
        
    if action == "Heal":
        if heals_left > 0:
            if player_health == 50:
                time.sleep(0.05)
                print("\nYou are already at max health!")

            elif player_health < 50:
                restored = random.randint(1, 5)
                player_health += restored
                time.sleep(0.05)
                print(f"\033[92mRestored {restored} HP")

                heals_left -= 1

                if player_health > 50:
                    player_health = 50

        else:
            print("\n\n\033[90mYou are out of heals!")

    elif action == "Roll Dice":
        dice = [1, 2, 3, 4, 5, 6]
        roll = random.choice(dice)
        if roll % 2 == 0:
            time.sleep(0.05)
            print(f"\n\033[90mRoll:\033[32m {roll}")
            damage = random.randint(3, 10)
            time.sleep(0.05)
            print(f"\n\033[90mYou dealt {damage} damage to {opponent_name}")
            opponent_health -= damage
            

        elif roll % 2 != 0:
            time.sleep(0.05)
            print(f"\n\033[90mRoll:\033[31m {roll}")
            damage = random.randint(3, 10)
            time.sleep(0.05)
            print(f"\n\033[90mYou recived {damage} damage from {opponent_name}")
            player_health -= damage

time.sleep(0.05)
results = input("\n\033[90mBattle over. Type \"Done\" to see results").capitalize()
while results != "Done":
    time.sleep(0.05)
    results = input("\n\033[90mBattle over. Type \"Done\" to see results").capitalize()

if player_health > opponent_health:
    print("\n\033[90mResults:")
    time.sleep(0.05)
    print("\n\033[32mWin")
    time.sleep(0.05)
    print(f"\033[90mYour HP: \033[92m {player_health}")
    time.sleep(0.05)
    print(f"\033[90mOpponent HP:\033[91m {opponent_health}")

if player_health < opponent_health:
    print("\n\033[90mResults:")
    time.sleep(0.05)
    print("\n33[31mLoss")
    time.sleep(0.05)
    print(f"\n\033[90mYour HP: \033[92m {player_health}")
    time.sleep(0.05)
    print(f"\033[90mOpponent HP:\033[91m {opponent_health}")

exit = input("\n\033[90mType any key to exit:")
    
