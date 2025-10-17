
import time

print("Binary Converter")
time.sleep(0.05)
print("\n1. Convert Decimal to Binary")
time.sleep(0.05)
print("2. Convert Binary to Decimal")

running = True

while running:
    time.sleep(0.05)
    choice = input("\nEnter 1 or 2:")
    while choice not in ["1", "2"]:
        time.sleep(0.05)
        choice = input("Enter 1 or 2:")

    if choice == "1":

        while True:
            number = input("\nEnter a number: ")
            try:
                value = int(number)
                break  #Check if input is an integer
            except ValueError:
                time.sleep(0.05)
                number = input("Enter a number: ")
                    
