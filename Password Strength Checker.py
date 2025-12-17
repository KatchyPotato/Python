import time

#-------------------------------------------------------------------------
#ChatGPT generated the lists, rewrote much of the code, and fixed my logic
#-------------------------------------------------------------------------

# Colors

colors = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[0m"    # reset
]

# Character lists

numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

special_chars = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+",
    "[", "]", "{", "}",
    "\\", "|",
    ";", ":", "'", "\"",
    ",", "<", ".", ">",
    "/", "?",
    "`", "~"
]

uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                    "n","o","p","q","r","s","t","u","v","w","x","y","z"]

time.sleep(0.05)
print("\nPASSWORD STRENGTH CHECKER")

running = True

while running:
    time.sleep(0.05)
    password = input("\nEnter your password [Or type 'exit' to quit]: ")

    if password.lower() == "exit":
        running = False
        break

    strength_level = 0
    feedback = []

    # Check for characters, numbers, uppercase, and lowercase
    if any(char in special_chars for char in password):
        strength_level += 1
    else:
        feedback.append("Add a special character (!,@,#,$, etc.)")

    if any(char in numbers for char in password):
        strength_level += 1
    else:
        feedback.append("Add a number (0-9)")

    if any(char in uppercase_letters for char in password):
        strength_level += 1
    else:
        feedback.append("Add an uppercase letter (A-Z)")

    if any(char in lowercase_letters for char in password):
        strength_level += 1
    else:
        feedback.append("Add a lowercase letter (a-z)")

    # Check length
    if len(password) >= 12:
        strength_level += 2
    elif len(password) >= 8:
        strength_level += 1
    else:
        feedback.append("Make your password at least 8 characters long")

    # Output strength
    if strength_level <= 2:
        time.sleep(0.05)
        print("\n\033[31mPassword Strength: Weak\033[0m")
    elif strength_level <= 4:
        time.sleep(0.05)
        print("\n\033[32mPassword Strength: Moderate\033[0m")
    else:
        time.sleep(0.05)
        print("\n\033[32mPassword Strength: Strong\033[0m")

    # Detailed feedback
    if feedback:
        time.sleep(0.05)
        print("\nSuggestions to improve your password:\n")
        for f in feedback:
            time.sleep(0.05)
            print("- " + f)

    

        
        
    
