
import time

print("Binary Converter")

running = True

while running:

    time.sleep(0.05)
    print("\n1. Convert Decimal to Binary")
    time.sleep(0.05)
    print("2. Convert Binary to Decimal")
    time.sleep(0.05)
    choice = input("\nEnter 1 or 2: ")
    while choice not in ["1", "2"]:
        time.sleep(0.05)
        choice = input("Enter 1 or 2: ")

    if choice == "1":

        while True:
            time.sleep(0.05)
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

    elif choice == "2":

        valid = False

        while not valid:
            time.sleep(0.05)
            binary = input("\nEnter a Binary number: ")
            valid = True 

            for char in binary:
                if char not in ["1", "0"]:
                    time.sleep(0.05)
                    print("\nPlease enter a valid Binary number")
                    valid = False
                    break

        binary_for_string = binary
        raw_powers = []
        power_of_two = 1

        for bit in binary:
            raw_powers.append(power_of_two)
            power_of_two *= 2

        powers = raw_powers[::-1]
        binary_list = list(binary)

        decimal = 0

        for bit in binary:
            if bit == "0":
                del powers[0]
                del binary_list[0]
            elif bit == "1":
                decimal += powers[0]
                del powers[0]
                del binary_list[0]

        time.sleep(0.05)
        print(f"\n{binary_for_string} in Decimal: {decimal}")
        
        


            
            
            
                    
