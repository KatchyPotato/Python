
import time

print("Binary Converter")
time.sleep(0.05)
print("\n1. Convert Decimal to Binary")
time.sleep(0.05)
print("2. Convert Binary to Decimal")

running = True

while running:
    time.sleep(0.05)
    choice = input("\nEnter 1 or 2: ")
    while choice not in ["1", "2"]:
        time.sleep(0.05)
        choice = input("Enter 1 or 2: ")

    if choice == "1":

        while True:
            raw_input = input("\nEnter a number: ")
            try:
                number = int(raw_input)
                if number < 0:
                    time.sleep(0.05)
                    print("\nPlease enter a positive number")
                    continue
                break
            except ValueError:
                time.sleep(0.05)
                print("\nPlease enter a whole number")

        if number == 0:
            time.sleep(0.05)
            print("\n0 in Binary: 0")

        else:
            number_for_string = number
            raw_binary = ""

            while number > 0:
                bit = number % 2
                raw_binary += str(bit)
                number //= 2

            binary = raw_binary[::-1]
            time.sleep(0.05)
            print(f"\n{number_for_string} in Binary: {binary}")


            
            
            
                    
