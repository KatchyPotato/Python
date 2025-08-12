try_again = "Yes"

while try_again == "Yes":

    shoppinglist = input("Input the items you need:").split()
    what_to_get = {}

    for item in shoppinglist:
        amount_needed = int(input(f"\nHow many {item} do you need?"))
        amount_had = int(input(f"\nHow many {item} do you currently have?"))

        #ChatGPT helped a little at this point

        how_much_to_get = amount_needed - amount_had
        if how_much_to_get < 0:
            how_much_to_get = 0
        what_to_get[item] = how_much_to_get

    print("\nGenerated shoppinglist:")
    print(what_to_get)
    new_list = input("\nWant to generate a new shoppinglist? (Yes or No)")
  
