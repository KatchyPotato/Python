
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

aesthetic = ["~", "*", "^", ":", ";", ".", "+", "•"]

cards = ["♠", "♥", "♦", "♣"]

ocean = ["~", "=", "-", "_", "≈", "≋", "≂", "≃", "≄", "≅"]

galaxy = ["*", "•", "✦", "✧"]

cherry = ["*", "+", "•", "~"]

greek = [
    "Α","Β","Γ","Δ","Ε","Ζ","Η","Θ",
    "Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π",
    "Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω",
    "α","β","γ","δ","ε","ζ","η","θ",
    "ι","κ","λ","μ","ν","ξ","ο","π",
    "ρ","σ","τ","υ","φ","χ","ψ","ω",
    "Ω","Δ","Φ","Σ","Ψ","Θ"
]

cherry_colors = [
    "\033[38;5;219m",  # soft pink
    "\033[38;5;212m",  # medium pink
    "\033[38;5;225m"   # pale pink
]

galaxy_colors = [
    "\033[38;5;93m",   # purple
    "\033[38;5;201m",  # pink
    "\033[38;5;57m",   # dark blue
    "\033[38;5;27m"    # deep blue

]
greek_colors = [
    "\033[38;5;223m",  # light tan
    "\033[38;5;180m",  # medium tan
    "\033[38;5;230m",  # parchment white
    "\033[38;5;250m",  # marble white
    "\033[38;5;34m",   # olive green
    "\033[38;5;71m"    # light green
]

ocean_colors = [
    "\033[38;5;27m",   # deep ocean blue
    "\033[38;5;33m",   # blue
    "\033[38;5;39m",   # light blue
    "\033[38;5;44m",   # aqua
    "\033[38;5;51m"    # seafoam cyan
]

card_colors = [
    "\033[31m",  # red
    "\033[90m"   # gray
]

aesthetic_colors = [
    "\033[38;5;200m",  # pink
    "\033[38;5;201m",  # hot pink
    "\033[38;5;198m",  # magenta
    "\033[38;5;165m",  # purple
    "\033[38;5;93m",   # violet
    "\033[38;5;129m"   # deep purple
]

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
print("~\033[90mM\033[37me\033[97mc\033[90mh\033[37ma\033[97mn\033[90mi\033[37mc\033[97ma\033[90ml\033[0m")
time.sleep(0.05)
print("~\033[38;5;200mA\033[38;5;201me\033[38;5;198ms\033[38;5;165mt\033[38;5;93mh\033[38;5;129me\033[38;5;200mt\033[38;5;201mi\033[38;5;198mc\033[0m")
time.sleep(0.05)
print("~\033[31mC\033[90ma\033[31mr\033[90md\033[31ms\033[0m")
time.sleep(0.05)
print("~\033[38;5;27mO\033[38;5;33mc\033[38;5;39me\033[38;5;44ma\033[38;5;51mn\033[0m")
time.sleep(0.05)
print("~\033[38;5;223mG\033[38;5;230mr\033[38;5;34me\033[38;5;180me\033[38;5;71mk\033[0m")
time.sleep(0.05)
print("~\033[38;5;93mG\033[38;5;201ma\033[38;5;57ml\033[38;5;27ma\033[38;5;93mx\033[38;5;201my\033[0m")
time.sleep(0.05)
print("~\033[38;5;219mC\033[38;5;212mh\033[38;5;225me\033[38;5;219mr\033[38;5;212mr\033[38;5;225my\033[0m")






choice = ""
while choice not in ["Rainbow", "Binary", "Fire", "Neon", "Mechanical", "Aesthetic", "Cards", "Ocean", "Greek", "Galaxy", "Cherry"]:
    time.sleep(0.05)
    choice = input("\nEnter Wave Option: ").capitalize()

#Rainbow wave option

if choice == "Rainbow":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        color = 0
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += rainbow_colors[color]
                line += random.choice(letters)
                if color == 6:
                    color = 0
                else:
                    color += 1
            time.sleep(0.05)
            print(line)
            char_count += 5
            
        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += rainbow_colors[color]
                line += random.choice(letters)
                if color == 6:
                    color = 0
                else:
                    color += 1
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

#Aesthetic wave option

elif choice == "Aesthetic":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(aesthetic_colors)
                line += random.choice(aesthetic)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(aesthetic_colors)
                line += random.choice(aesthetic)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Cards wave option

elif choice == "Cards":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(card_colors)
                line += random.choice(cards)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(card_colors)
                line += random.choice(cards)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Ocean wave option

elif choice == "Ocean":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(ocean_colors)
                line += random.choice(ocean)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(ocean_colors)
                line += random.choice(ocean)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Greek wave option

elif choice == "Greek":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(greek_colors)
                line += random.choice(greek)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(greek_colors)
                line += random.choice(greek)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Galaxy wave option

elif choice == "Galaxy":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(galaxy_colors)
                line += random.choice(galaxy)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(galaxy_colors)
                line += random.choice(galaxy)
            time.sleep(0.05)
            print(line)
            char_count -= 5

#Cherry wave option

elif choice == "Cherry":

    running = True

    while running:
        wave_length = random.randint(15, 200)
        wave_length -= wave_length % 5

        char_count = 5
        while char_count <= wave_length:
            line = ""
            for char in range(char_count):
                line += random.choice(cherry_colors)
                line += random.choice(cherry)
            time.sleep(0.05)
            print(line)
            char_count += 5

        char_count = wave_length

        while char_count > 0:
            line = ""
            for char in range(char_count):
                line += random.choice(cherry_colors)
                line += random.choice(cherry)
            time.sleep(0.05)
            print(line)
            char_count -= 5





    
    
        
