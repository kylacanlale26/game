#   START OF CODE

import random

boarder = "=" * 30

# CREATE PLAYER
def create_player():

    print(f"\n{boarder}") #seperator

    player_name = input("\nPlease enter your player name: ") #input - player's name

    print(f"\n{boarder}") #seperator

    #dictionary - classes (+ stats) that the players can choose from
    class_choices = {
        "Knight": {"hp": 65,
                   "attack": 15,
                   "defense":12,
                   "skill": "Power Slash"},
        "Assassin": {"hp": 60,
                     "attack": 25,
                     "defense": 7,
                     "skill": "Shadow Strike"},
        "Mage": {"hp": 50,
                 "attack": 20,
                 "defense": 5,
                 "skill": "Abyssal Flame"},
        "Healer": {"hp": 80,
                   "attack": 8,
                   "defense": 10,
                   "skill": "Divine Healing"},
        "Tank": {"hp": 75,
                 "attack": 12,
                 "defense": 25,
                 "skill": "Iron Clad"}
    }

    #input - player choose class
    print("\nClasses: ")
    class_list = list(class_choices.keys()) #gets all keys from dictionary then turn them into list

    #displays class options with with numbering
    for i, c in enumerate(class_list, start=1):
        print(f"[{i}] {c:}")

    choice = input("\nSelect your class (number): ") #player input chosen class

    #validate input - checks if input is a digit or not included in the choices
    while not choice.isdigit() or int(choice) not in range(1, len(class_list) + 1): #loop to keep asking if invalid input
        print("\nInvalid class selection. Please enter a valid digit from the available choices.")
        choice = input("\nChoose again: ")

    choice = class_list[int(choice) - 1] #converts input into int and -1 since lists count starts at 0

    #makes a copy of the selected class and its stats
    player = class_choices[choice].copy()

    #additional player data - additonal items to dictionary to display
    player["name"] = player_name
    player["class"] = choice
    player["win"] = 0
    player["defeat"] = 0
    player["gold"] = 150
    player["inventory"] = [] #list - inventory storage

    player["max_hp"] = player["hp"] #sets max hp for the healer class

    return player

def player_info_display(player):
    #list - to reorder dictionary
    order = ["name", "class", "hp", "attack", "defense", "skill", "win", "defeat", "gold", "inventory"]

    print("\n~ Player Profile ~")
    for key in order: #displays player's info vertically
        print(f"{key.capitalize():<10}: {player[key]}")

# ENEMY RANDOMIZER
def enemy_picking():

    #enemies stats - tuple inside a list
    enemies = [
        ("Minion", 50, 4, 5), #name, hp, atk, def
        ("Witch", 60, 10, 10),
        ("Evil Fae", 65, 20, 5),
        ("Dark Husk", 70, 20, 12),
        ("Dragon", 75, 25, 15)
    ]

    enemy = random.choice(enemies) #picks random enemy
    return {"name": enemy[0], "hp": enemy[1], "attack": enemy[2], "defense": enemy[3]} #converts to dictionary to be used in game

# BATTLE SYSTEM
def battle(player, enemy):

    print(f"\n{enemy['name']} has spawned!") #title

    print(f"\n{boarder}") #seperator

    #battle loop
    while enemy['hp'] > 0 and player['hp'] > 0:
        print(f"\n{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")

        print(f"\n{boarder}") #seperator

        # PLAYER ACTION
        print("\nYOUR TURN TO ATTACK!")

        print("\n[1] Normal Attack | [2] Skill")

        action = input("Choose your action (number): ") 

        print(f"\n{boarder}") #seperator

        if action == "1":

            print("\nYou used normal attack!")

            dmg = max(1, int(player["attack"] - enemy["defense"] * 0.5)) #prevents 0 or negative damage | calculate damage with defense reduction
            enemy["hp"] = max(0, enemy["hp"] - dmg) #prevents negative hp
            print(f"\nYou dealt {dmg} to the enemy!")

        #skills system
        elif action == "2":
            print(f"\n{player['skill']}!")

            skill_dmg = 0 #variable with 0 value
            
            #calculation of skill damage
            if player["skill"] == "Power Slash":
                skill_dmg = player["attack"] * 1.3

            elif player["skill"] == "Shadow Strike":
                skill_dmg = player["attack"] * 1.5

            elif player["skill"] == "Abyssal Flame":
                skill_dmg = player["attack"] * 1.8

            elif player["skill"] == "Divine Healing": #healing mechanism (if chosen class is Healer)

                if player["hp"] >= player["max_hp"]: #cancels skill if full hp
                    print("\nYou are full HP, skill cancelled!")
                
                else:
                    heal = int(player["max_hp"] * 0.2) #heals player based on their max hp
                    player["hp"] = min(player["hp"] + heal, player["max_hp"]) #add heal to hp | prevent overheal above max HP    
                    print(f"\nYou healed {heal} HP!")

                skill_dmg = 0 #variable with 0 value
                    
            elif player["skill"] == "Iron Clad": #defense buff mechanism (if chosen class is Tank)
                buff = int(player["defense"] * 0.2) #defense buff calculation
                player["defense"] += buff
                print(f"\nSkill increased your defense by {buff}!")

                skill_dmg = 0 #variable with 0 value
                
            # damage calculation (only if attack skill)
            if dmg > 0: 
                dmg = max(1, int(skill_dmg - enemy["defense"] * 0.5)) #prevents 0 or negative damage | calculate damage with defense reduction
                enemy["hp"] = max(0, enemy["hp"] - dmg) #apply damage to enemy
                print(f"\nYou dealt {dmg} to the enemy!")

        else: #if player typed something out of the choices
            print("\nAction invalid!")
            continue #loop to keep asking if invalid input

        print(f"\n{boarder}") #seperator

        #enemy action

        if enemy["hp"] <= 0:
            break

        print(f"\n{enemy['name']}'s TURN TO ATTACK".upper()) #.upper() to change case to capitalized

        print(f"\n{boarder}") #seperator

        action = random.choice(["normal_attack", "heavy_attack"]) #randomized action picker for enemy

        if action == "normal_attack":
            print(f"\n{enemy['name']} used normal attack!")
            dmg = enemy["attack"] - (player["defense"] * 0.5) #player's defense reduces damage

        else:
            print(f"\n{enemy['name']} used heavy attack!")
            heavy_dmg = enemy["attack"] * 1.5 #heavy attack's damage calculation
            dmg = heavy_dmg - (player["defense"] * 0.5) #damage calculation with defense reduction
        
        dmg = max(1, int(dmg)) #prevents 0 or negative damage
        player["hp"] = max(0, player["hp"] - dmg) #substract dmg to player's hp | prevents HP going negative
        
        print(f"\nYou are hit {dmg} damage!")
        
        print(f"\n{boarder}") #seperator

    #reward system
    if player["hp"] > 0:
        reward = random.randint(10, 40)
        player["gold"] += reward #gives reward
        player["win"] += 1 #tracks win
        print(f"\nYou defeated the {enemy['name']}!")

        return True #indicates player won
    
    else:
        player["defeat"] += 1 #tracks defeat
        print(f"\nYou are defeated by the {enemy['name']}!")

        return False #indicates player lost

# SHOP SYSTEM
def shop(player):

    #shop loop 
    while True:

        print("\n~ WELCOME TO THE POTION SHOP ~") #title

        print(f"\nGold: {player['gold']}") #display gold count

        print("\n[1] BUY POTIONS | [2] EXIT") #options

        choice = input("\nEnter your action: ") #input choice

        #input validation - checks if input is included in the choices
        while choice not in ["1", "2"]:
            choice = input("\nSelected option invalid. Choose again: ")

        if choice == "1":

            #picking potion to buy loop
            while True:

                #dictionary - shop items
                shop_items = {
                    "Heal Potion": {"price": 20, "heal": 30},
                    "Attack Potion": {"price": 50, "attack": 10},
                    "Defense Potion": {"price": 50, "defense": 5}
                }

                print(f"\n{boarder}")

                print("\n~ AVAILABLE ITEMS ~")

                item_list = list(shop_items.items()) #converts dictionary to list of key-value pairs

                for i, (item_name, stats) in enumerate(item_list, start=1): #displays shop items and description options with numbering

                    #description
                    if "heal" in stats:
                        desc = f"Heals {stats['heal']} HP"
                    elif "attack" in stats:
                        desc = f"Boosts Attack by {stats['attack']}"
                    elif "defense" in stats:
                        desc = f"Boosts Defense by {stats['defense']}"

                    print(f"[{i}] {item_name} - {stats['price']} Gold | {desc}")
                

                choice = input("\nSelect potion to buy: ")

                #validate input - checks if its a digit or included in the choices
                while not choice.isdigit() or int(choice) not in range(1, len(item_list) + 1): #loop to keep asking if invalid input
                    choice = input("\nSelected option invalid. Choose again: ")

                selected_name, stats = item_list[int(choice) - 1]
                price = stats["price"]

                #checks if hp is full to stop player from buying
                if "heal" in stats and player["hp"] >= player["max_hp"]:
                    print(f"\n{boarder}")
                    print("\nYour HP is already full! You cannot buy a Heal Potion.")
                    continue

                #checks if there's enough gold
                if player["gold"] < price:
                    print("\nYou don't have enough gold!")
                    return

                #updates player's gold
                player["gold"] -= price

                #adjust stats when player bought potion
                if "heal" in stats:
                    player["hp"] += stats["heal"]
                    player["hp"] = min(player["hp"], player["max_hp"])
                elif "attack" in stats:
                    player["attack"] += stats["attack"]
                elif "defense" in stats:
                    player["defense"] += stats["defense"]

                player["inventory"].append(selected_name) #add bought items in inventory

                print(f"\n{boarder}")

                print(f"\nYou bought {selected_name}!")

                print(f"\nRemaining Gold: {player['gold']}")

                again = input("\nBuy another potion? [yes/no]: ").lower() #to loop buying potion | set input to lower case

                if again == "no": #exit the shop
                    print(f"\n{boarder}")
                    print("\nLeaving shop...")
                    return

        elif choice == "2": #exit the shop
            print(f"\n{boarder}")
            print("\nLeaving shop...")
            return

# GAME OVERALL SYSTEM
def game():

    while True:

        print(f"\n{boarder}") #seperator

        print("\n~ WELCOME TO THE DUNGEONS ~") #welcome title

        player = create_player()

        print(f"\n{boarder}") #seperator

        while True:

            print("\n~ DUNGEON MENU ~") #welcome title

            dungeon_menu = ("Enter Dungeon", "Player Profile", "Shop", "Quit") #tuple
            for i, item in enumerate(dungeon_menu, start=1):
                print(f"[{i}] {item}")

            choice = input("\nSelect an option: ")

            #validate choice - checks if input is a digit or not included in the choices
            while not choice.isdigit() or int(choice) not in range(1, len(dungeon_menu) + 1):
                choice = input("\nSelected option invalid. Choose again: ")

            print(f"\n{boarder}") #seperator

            if choice == "1":
                enemy = enemy_picking()
                battle(player, enemy)

            elif choice == "2":
                player_info_display(player) #displays player profile and updates

            elif choice == "3":
                shop(player) #displays shop

            elif choice == "4":
                print("\nGAME OVER")
                break

            print(f"\n{boarder}") #seperator

            #END GAME
            if player["win"] == 5:
                print("\nCONGRATULATIONS ON CLEARING THE DUNGEONS!")

            elif player["defeat"] == 5 or player["hp"] == 0:
                print("\nGAME OVER")

            
        #restart mechanics
        print(f"\n{boarder}") #seperator

        print("\n[1] PLAY AGAIN | [2] EXIT")

        choice = input("\nChoose: ")

        #validate choice - checks if input is a digit or not included in the choices
        while not choice.isdigit() or int(choice) not in [1, 2]:
            choice = input("\nSelected option invalid. Choose again: ")

        if choice == "1":
            continue

        elif choice == "2":
            print(f"\n{boarder}") #seperator
            print("\nExisting the dungeons... Goodbye!")
            print(f"\n{boarder}") #seperator
            break

game()