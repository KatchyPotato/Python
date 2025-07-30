number1 = int(input("Input first number:"))
arithmetic = input("What arithmatic would you like to use?")
number2 = int(input("Input second number:"))

if arithmetic == "+":
    calculation = (number1 + number2)
    print(calculation)

elif arithmetic == "-":
    calculation = (number1 - number2)
    print(number1 - number2)

elif arithmetic == "*":
    calculation = (number1 * number2)
    print(number1 * number2)

elif arithmetic == "/":
    calculation = (number1 /number2)
    print(number1 / number2)

end_message = "Calculation complete. Your calculation: {0} {1} {2} = {3}"
print(end_message.format(number1, arithmetic, number2, calculation))

try_again = input("Would you like to try again? (Yes or No)")

