first_number = int(input("Pick a number"))
second_number = int(input("Pick a second number"))
arithmatic = input("What arithmatic would you like to use?")

if arithmatic == "+":
    print(first_number + second_number)

elif arithmatic == "-":
    print(first_number - second_number)

elif arithmatic == "*":
    print(first_number * second_number)

elif arithmatic == "/":
    print(first_number / second_number)
else: print("INVALID ARITHMATIC")


