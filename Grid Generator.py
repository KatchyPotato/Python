import time
time.sleep(0.05)
print("\n# Grid Generator #")

running = True

# get number of rows and row length

while running:
    while True:
        try:
            time.sleep(0.05)
            rows = int(input("\nEnter number of rows: "))
            if rows <= 0:
                raise ValueError
            break
        except ValueError:
            time.sleep(0.05)
            print("\n\033[31mPlease enter a positive integer\033[0m")

    while True:
        try:
            time.sleep(0.05)
            length = int(input("\nEnter row length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            time.sleep(0.05)
            print("\n\033[31mPlease enter a positive integer\033[0m")

    # generate grid
    print("\n")
    for row in range(rows):
        time.sleep(0.05)
        print(("*" * length))

    time.sleep(0.05)
    generate_new = ""
    while generate_new not in ["yes", "no"]:
        generate_new = input("\nWould you like to generate a new grid? (yes/no) ").lower()

    if generate_new == "yes":
        running = True
    elif generate_new == "no":
        running = False



    
    
