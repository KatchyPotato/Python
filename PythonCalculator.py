number1 = int(input("Input first number:"))
arithmetic = input("Input arithmetic:")
number2 = int(input("Input second number:"))

#Calculator recives input for two numbers and an operation

if arithmetic == "+":
    calculation = (number1 + number2)
    print(number1 + number2)

elif arithmetic == "-":
    calculation = (number1 - number2)
    print(number1 - number2)

elif arithmetic == "*":
    calculation = (number1 * number2)
    print(number1 * number2)

elif arithmetic == "/":
    calculation = (number1 /number2)
    print(number1 / number2)

#Different funtions for different opperations

end_message = "Calculation complete. Your calculation: {0} {1} {2} = {3}"
print(end_message.format(number1, arithmetic, number2, calculation))

#End message prints out your calculation. Uses formatting to combine integers and strings

try_again = input("Would you like to try again? (Yes or No)")

if try_again == "No":
    print("CALCULATOR TERMINATED")
elif try_again == "Yes":

#Code for seccond calculation

    number1 = int(input("Input first number:"))
    arithmetic = input("Input arithmetic:")
    number2 = int(input("Input second number:"))

    if arithmetic == "+":
        calculation = (number1 + number2)
        print(number1 + number2)

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
    
#Calculator code runs exacly the same as the first time

    try_again = input("Would you like to try again? (Yes or No)")

    if try_again == "No":
                print("CALCULATOR TERMINATED")
    elif try_again == "Yes":

#Code for third calculation

        number1 = int(input("Input first number:"))
        arithmetic = input("Input arithmetic:")
        number2 = int(input("Input second number:"))

        if arithmetic == "+":
            calculation = (number1 + number2)
            print(number1 + number2)

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

        print("MAX CALCULATIONS USED. CALCULATOR TERMINATED")

#Calculator terminates once all of the attempts are used



