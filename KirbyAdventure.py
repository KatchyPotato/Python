print("Kirby: Choose your own adventure")
print("""\nYou are walking home from school, all alone.
You notice a hamburger lying on the ground.""")
          
pick_up = input("\nDo you pick up the hamburger? (Yes or No)")

if pick_up == "Yes":
        print("""\nKirby must have smelled the hamburger... he jumps out at you.
He seems to want the hamburger.""")
        give_or_not = input("\nDo you give it to him? (Yes or No")
        if give_or_not == "Yes":
            print("""\nHe inhales it, and grows a pair of human legs.
He looks ready to fight.""")
            fight = input("\nDo you fight? (Yes or No)")
            if fight == "Yes":
                print("""\nHe kicks you, chattering your femure bone.
you lunge for him, but he scampers away into the woods. You know you will be
haunted by him forever. GAME OVER""")
            elif fight == "No":
                print("""\nYou slowly back away, promising him more hamburgers
you lead him home, feeding him all the hamburgers your mom just made, plus
the entire contents of the fridge. Kirby leaves after he has been satisfied. YOU WIN""")

        elif give_or_not == "No":
            print("""\n Bad idea. You eat it in front of his face.
before you know it, he attacks you, eating you instead. GAME OVER""")

elif pick_up == "No":
        print("""\nYou leave it behind, and continue to walk home.
behind you, you hear the sound of something viciously devouring the hamburger.""")

        print("""\nYou arrive backhome. Your mom cooked hamburgers for dinner.
after eating your meal, you retire to your bedroom. Something rattles the window.""")

        check = input("\nDo you check the window? (Yes or No)")
        if check == "No":
            print("""\nYou decide to just go to sleep, ingnoring whatever is out there.
In the middle of the night, something shatters your window, and crawls through
the space. Climbing on top of you, it appears to be Kirby. He stares at you,
and then eats you in one bite... hungry for more hamburgers. GAME OVER""")

        elif check == "Yes":
            print("""\nYou opened the window, to see Kirby staring back at you.
He looks hungry for hamburgers. You rush to the fridge, and hand Kirby
all the leftovers. Kirby eats them, and is satisfied... but not for long.
You go to sleep, relising that he will always come back for more. YOU WIN""")
        
print("\nYou have reached the end of your adventure")    
    
