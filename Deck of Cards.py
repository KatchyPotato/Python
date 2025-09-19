
import random
import time

#ChatGPT generated deck list

deck = [
    "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
    "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
    "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
    "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]

#ChatGPT generated ANSI color code list

colors = {
    "red": "\033[31m",
    "white": "\033[37m",
    "bright_black": "\033[90m"}

running = True

print("\n\033[90m ♣ \033[31mDeck\033[37m of\033[90m Cards\033[31m ♥")

while running:
    time.sleep(0.05)
    print("\n\033[37mActions")
    time.sleep(0.05)
    print("\n\033[90m~Shuffle Deck")
    time.sleep(0.05)
    print("\033[31m~Draw Cards")
    time.sleep(0.05)
    print("\033[90m~Deal Cards")
    time.sleep(0.05)
    print("\033[31m~Show Deck")
    time.sleep(0.05)
    print("\033[90m~Reset Deck")

    action = ""
    while action not in ["Shuffle Deck", "Draw Cards", "Deal Cards", "Show Deck", "Reset Deck"]:
        time.sleep(0.05)
        action = input("\n\033[37mEnter Action:").title()

    #First action, show deck

    if action == "Show Deck":

        colored_deck = ""
        for card in deck:
            if "♥" in card or "♦" in card:
                card = ("\033[31m" + card)
                colored_deck += (card + " ")

            elif "♠" in card or "♣" in card:
                card = ("\033[90m" + card)
                colored_deck += (card + " ")

        time.sleep(0.05)
        print("\n" + colored_deck)

    #Second action, shuffle deck

    elif action == "Shuffle Deck":
        random.shuffle(deck)
        time.sleep(0.05)
        print("\n\033[37mDeck Shuffled")

    #Third action, reset deck

    elif action == "Reset Deck":
        deck = [
            "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
            "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
            "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
            "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]
        time.sleep(0.05)
        print("\n\033[37mDeck Reset")

    #Fourth action, draw cards

    elif action == "Draw Cards":
        time.sleep(0.05)
        card_number = int(input("\n\033[37mHow Many Cards?"))

        cards = deck[:card_number]

        colored_hand = ""
        for card in cards:
            if "♥" in card or "♦" in card:
                card = ("\033[31m" + card)
                colored_hand += (card + " ")

            elif "♠" in card or "♣" in card:
                card = ("\033[90m" + card)
                colored_hand += (card + " ")

        deck = deck[card_number:]

        time.sleep(0.05)
        print("\nDrawn: " + colored_hand)

    #Fifth action, deal cards

    elif action == "Deal Cards":
        time.sleep(0.05)
        people = int(input("\n\033[37mHow Many People? "))
        while len(deck) % people != 0:
            print("\n\033[31mDeck must be divisible by people")
            print("Current deck length: " + str(len(deck)))
            time.sleep(0.05)
            people = int(input("\n\033[37mHow Many People? "))

        cards_per_player = len(deck) // people
        player_num = 1

        while player_num <= people:
            player_hand = deck[:cards_per_player]
            colored_hand = ""
            for card in player_hand:
                if "♥" in card or "♦" in card:
                    card = ("\033[31m" + card)
                    colored_hand += (card + " ")

                elif "♠" in card or "♣" in card:
                    card = ("\033[90m" + card)
                    colored_hand += (card + " ")

            time.sleep(0.05)
            print(f"\n\033[37mPlayer {player_num}: {colored_hand}")
            deck = deck[cards_per_player:]
            player_num += 1

        

        

    

            

           

    
