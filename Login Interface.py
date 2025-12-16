
import time

#ChatGPT for color code list and debugging

colors = {
    "black": "\033[30m",      # Black
    "red": "\033[31m",        # Red
    "green": "\033[32m",      # Green
    "yellow": "\033[33m",     # Yellow
    "blue": "\033[34m",       # Blue
    "magenta": "\033[35m",    # Magenta
    "cyan": "\033[36m",       # Cyan
    "white": "\033[37m",      # White

    "bright_black": "\033[90m",   # Gray
    "bright_red": "\033[91m",     # Bright Red
    "bright_green": "\033[92m",   # Bright Green
    "bright_yellow": "\033[93m",  # Bright Yellow
    "bright_blue": "\033[94m",    # Bright Blue
    "bright_magenta": "\033[95m", # Bright Magenta
    "bright_cyan": "\033[96m",    # Bright Cyan
    "bright_white": "\033[97m",   # Bright White

    "reset": "\033[0m"        # Reset
}

user1 = ["Empty", "Empty"]
user2 = ["Empty", "Empty"]
user3 = ["Empty", "Empty"]
user4 = ["Empty", "Empty"]
user5 = ["Empty", "Empty"]


accounts_created = 0

users = {
    "user1" : user1,
    "user2" : user2,
    "user3" : user3,
    "user4" : user4,
    "user5" : user5,
}

text = {
    "user1" : "",
    "user2" : "",
    "user3" : "",
    "user4" : "",
    "user5" : "",

}



running = True

while running:

    print("\nWelcome to Log-in")
    time.sleep(0.05)
    print("\nUser 1: " + user1[0])
    time.sleep(0.05)
    print("User 2: " + user2[0])
    time.sleep(0.05)
    print("User 3: " + user3[0])
    time.sleep(0.05)
    print("User 4: " + user4[0])
    time.sleep(0.05)
    print("User 5: " + user5[0])
    time.sleep(0.05)

    print("\nActions:")
    time.sleep(0.05)
    print("\n1. Log into an account")
    time.sleep(0.05)
    print("2. Create an account")
    time.sleep(0.05)
    print("3. Delete an account")
    time.sleep(0.05)

    user_action = ""
    while user_action not in ["1", "2", "3"]:
        time.sleep(0.05)
        user_action = input("\nEnter Action [1, 2, 3]: ")

    # ----------------------------------
    # LOG INTO ACCOUNT
    # ----------------------------------
    if user_action == "1":

        if accounts_created == 0:
            time.sleep(0.05)
            print("\n\033[31mPlease create an account before logging in!\033[0m")

        else:
            account_choice = ""
            while account_choice not in users:
                time.sleep(0.05)
                account_choice = input("\nWhat user would you like to log into? [user1, user2, user3...] ").lower()
                if account_choice not in users:
                    continue
                elif "Empty" in users[account_choice]:
                    print("\n\033[31mThat account slot has not been created!\033[0m")
                    continue
                else:
                    time.sleep(0.05)
                    print("\nEnter login information:")
                    success = False
                    while not success:
                        time.sleep(0.05)
                        user_name_try = input("\nUsername: ")
                        time.sleep(0.05)
                        password_try = input("\nPassword: ")
                        if user_name_try != users[account_choice][0] or password_try != users[account_choice][1]:
                            time.sleep(0.05)
                            print("\n\033[31mInvalid login credidentials! Please try again\033[0m")
                            continue
                        else:
                            #Log user in
                            success = True
                            time.sleep(0.05)
                            print(f"\n\033[32mWelcome, {users[account_choice][0]}!\033[0m")

                            logged_in = True

                            while logged_in:
                                time.sleep(0.05)
                                print("\nUser Actions:")
                                time.sleep(0.05)
                                print("\n1. Add data")
                                time.sleep(0.05)
                                print("2. Read data")
                                time.sleep(0.05)
                                print("3. Delete all data")
                                time.sleep(0.05)
                                print("4. Log out")
                                user_action = ""
                                while user_action not in ["1", "2", "3", "4"]:
                                    user_action = input("\nEnter user action: [1, 2, 3, 4] ").lower()

                                #Add data
                                if user_action == "1":
                                    time.sleep(0.05)
                                    user_data = input("\nEnter your data: ")
                                    text[account_choice] += user_data
                                    time.sleep(0.05)
                                    print("\n\033[32mData successfully added!\033[0m")
                                    

                                #Read data
                                elif user_action == "2":
                                    #Check if any data exists
                                    if len(text[account_choice]) == 0:
                                        time.sleep(0.05)
                                        print("\n\033[31mYou have no data! Add data before reading\033[0m")
                                    else:
                                        time.sleep(0.05)
                                        print(f"\n{account_choice} data:")
                                        time.sleep(0.05)
                                        print(f"\n{text[account_choice]}")

                                #Delete all data
                                elif user_action == "3":
                                    #Check if any data exists
                                    if len(text[account_choice]) == 0:
                                        time.sleep(0.05)
                                        print("\n\033[31mYour data is already empty! Add data before deleting\033[0m")
                                    else:
                                        text[account_choice] = ""
                                        time.sleep(0.05)
                                        print("\n\033[32mAll data deleted!\033[0m")
                                    

                                #Log out
                                elif user_action == "4":
                                    time.sleep(0.05)
                                    print("\n\033[32mYou have been logged out!\033[0m")
                                    logged_in = False
                                    

                                
                                    
                            
    # ----------------------------------
    # CREATE ACCOUNT
    # ----------------------------------
    elif user_action == "2":

        if accounts_created == 5:
            time.sleep(0.05)
            print("\n\033[31mThere are no account slots left! Deleat an account to create a new one\033[0m")

        else:

            # Choose slot
            account_slot = ""
            success = False
            while account_slot not in users or not success:
                time.sleep(0.05)
                account_slot = input("\nChoose an account slot: [user1, user2, user3...] ").lower()

                if account_slot not in users:
                    continue

                if "Empty" not in users[account_slot]:
                    time.sleep(0.05)
                    print("\n\033[31mThat account slot is already full! Please select an empty slot\033[0m")
                    success = False
                else:
                    success = True

            # Create username
            username_created = False
            while not username_created:
                time.sleep(0.05)
                user_name = input("\nCreate your username: ")

                taken = False
                for key, data in users.items():
                    if user_name == data[0]:
                        taken = True
                        break

                if taken:
                    time.sleep(0.05)
                    print("\n\033[31mThat username has already been taken!\033[0m")
                else:
                    username_created = True

            # Create password
            password_created = False
            while not password_created:
                time.sleep(0.05)
                password = input("\nCreate your password: ")

                taken = False
                for key, data in users.items():
                    if password == data[1]:
                        taken = True
                        break

                if taken:
                    time.sleep(0.05)
                    print("\n\033[31mThat password has already been taken!\033[0m")
                else:
                    password_created = True

            # Save account
            users[account_slot][0] = user_name
            users[account_slot][1] = password
            accounts_created += 1
            time.sleep(0.05)
            print("\n\033[32mAccount created successfully!\033[0m")

    # ----------------------------------
    # DELETE ACCOUNT
    # ----------------------------------
    elif user_action == "3":
        if accounts_created == 0:
            time.sleep(0.05)
            print("\n\033[31mThere are no accounts to delete!\033[0m")

        else:

            # Choose slot
            account_slot = ""
            success = False
            while account_slot not in users or not success:
                time.sleep(0.05)
                account_slot = input("\nChoose an account to delete: [user1, user2, user3...] ").lower()

                if account_slot not in users:
                    continue

                if "Empty" in users[account_slot]:
                    time.sleep(0.05)
                    print("\n\033[31mThat account slot is already empty!\033[0m")
                    success = False
                else:
                    success = True

            # Deleat account
            users[account_slot][0] = "Empty"
            users[account_slot][1] = "Empty"
            text[account_slot] = ""
            accounts_created -= 1
            time.sleep(0.05)
            print("\n\033[32mAccount deleted successfully!\033[0m")

            

        
        


                            
                                
                            
                            

        

            
                
            
            



































    
