
#ChatGPT for generating symbol and color lists, and for help with debugging the code

import random
import time

letters = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

neon = ["@", "#", "&", "%", "$", "!", "*", "+", "=", "?"]

binary = ["0", "1"]

fire = ["*", "~", "^",]

mechanical = ["{", "}", "(", ")", "|", "\\", "/"]

rainbow_colors = [
    "\033[38;5;196m",  # red
    "\033[38;5;208m",  # orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;46m",   # green
    "\033[38;5;21m",   # blue
    "\033[38;5;93m",   # indigo
    "\033[38;5;201m"   # violet
]

neon_colors = [
    "\033[38;5;201m",  # hot pink
    "\033[38;5;93m",   # bright purple
    "\033[38;5;51m",   # bright cyan
    "\033[38;5;45m",   # teal
    "\033[38;5;226m",  # bright yellow
    "\033[38;5;208m",  # bright orange
    "\033[38;5;46m"    # bright green
]

fire_colors = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # dark orange
    "\033[38;5;208m",  # orange
    "\033[38;5;214m",  # light orange
    "\033[38;5;226m",  # yellow
    "\033[38;5;220m"   # pale yellow
]

mechanical_colors = [
    "\033[90m",  # bright black / gray
    "\033[37m",  # white
    "\033[97m"   # bright white
]

reset = "\033[0m"



print("\nWave Options:")
time.sleep(0.05)
print("\n~\033[38;5;196mR\033[38;5;208ma\033[38;5;226mi\033[38;5;46mn\033[38;5;21mb\033[38;5;93mo\033[38;5;201mw\033[0m")
time.sleep(0.05)
print("~\033[38;5;46mBinary\033[0m")
time.sleep(0.05)
print("~\033[38;5;196mF\033[38;5;202mi\033[38;5;208mr\033[38;5;214me\033[0m")
time.sleep(0.05)
print("~\033[38;5;201mN\033[38;5;93me\033[38;5;51mo\033[38;5;45mn\033[0m")
time.sleep(0.05)
print("~\033[90mMechanical\033[0m")

choice = ""
while choice not in ["Rainbow", "Binary", "Fire", "Neon", "Mechanical"]:
    time.sleep(0.05)
    choice = input("\nEnter Wave Option: ").capitalize()

#Rainbow wave option

if choice == "Rainbow":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(rainbow_colors)
                line += random.choice(letters)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(rainbow_colors)
                line += random.choice(letters)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Binary wave option

elif choice == "Binary":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += "\033[38;5;46m"
                line += random.choice(binary)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += "\033[38;5;46m"
                line += random.choice(binary)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Fire wave option

elif choice == "Fire":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(fire_colors)
                line += random.choice(fire)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(fire_colors)
                line += random.choice(fire)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Neon wave option

elif choice == "Neon":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(neon_colors)
                line += random.choice(neon)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(neon_colors)
                line += random.choice(neon)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Mechanical wave option

elif choice == "Mechanical":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(mechanical_colors)
                line += random.choice(mechanical)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(mechanical_colors)
                line += random.choice(mechanical)
            time.sleep(0.05)
            print(line)
            char_count -= 5

    
    
        
