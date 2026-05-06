#   START OF CODE

import random

boarder = "=" * 30

# CREATE PLAYER
def create_player():

    print(f"\n{boarder}") #seperator

    #input - player's name
    player_name = input("\nEnter Name: ")

    print(f"\n{boarder}") #seperator

    #dictionary - classes + stats that the players can choose from
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
        "Healer": {"hp": 100,
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
    class_list = list(class_choices.keys())

    for i, c in enumerate(class_list, start=1):
        print(f"[{i}] {c:}")

    choice = input("\nSelect your class (number): ")

    #validate choice - checks if input is a digit or not included in the choices
    while not choice.isdigit() or int(choice) not in range(1, len(class_list) + 1):
        choice = input("\nSelected class invalid. Choose again: ")

    choice = class_list[int(choice) - 1]

    #copy selected class' stats
    player = class_choices[choice].copy()

    #additional player data - add items to dictionary class_choice
    player["name"] = player_name
    player["class"] = choice
    player["win"] = 0
    player["defeat"] = 0
    player["gold"] = 150
    player["inventory"] = [] #list - inventory storage

    player["max_hp"] = player["hp"] #sets max hp for the healer

    return player

def player_info_display(player):
    #list - to reorder dictionary
    order = ["name", "class", "hp", "attack", "defense", "skill", "win", "defeat", "gold", "inventory"]

    #displays player's info vertically
    print("\n~ Player Profile ~")
    for key in order:
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

    enemy = random.choice(enemies)
    return {"name": enemy[0], "hp": enemy[1], "attack": enemy[2], "defense": enemy[3]}

# BATTLE SYSTEM
def battle(player, enemy):

    print(f"\n{boarder}") #seperator

    print(f"\n{enemy['name']} has spawned!")

    print(f"\n{boarder}") #seperator

    #battle loop
    while enemy['hp'] > 0 and player['hp'] > 0:
        print(f"\n{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        print(f"\n{boarder}") #seperator

        # PLAYER ACTION
        print("\nYOUR TURN TO ATTACK!")
        print("\n[1] Normal Attack | [2] Skill")
        action = input("Choose action: ") 

        print(f"\n{boarder}") #seperator

        if action == "1":
            print("\nYou used normal attack!")
            dmg = player["attack"] - (enemy["defense"] * 0.5) #enemy's defense reduces damage
            dmg = max(1, int(dmg)) #prevents 0 or negative damage
            enemy["hp"] -= dmg #substract dmg to enemy's hp
            enemy["hp"] = max(0, enemy["hp"])  #prevent negative enemy HP
            print(f"\nYou dealt {dmg} to the enemy!")

        #skills system
        elif action == "2":
            print(f"\n{player['skill']}!")

            skill_dmg = 0
            
            #each class have different skills and deals different amount of damage
            if player["skill"] == "Power Slash":
                skill_dmg = player["attack"] * 1.3 #skill's adjusted damage

            elif player["skill"] == "Shadow Strike":
                skill_dmg = player["attack"] * 1.5 #skill's adjusted damage

            elif player["skill"] == "Abyssal Flame":
                skill_dmg = player["attack"] * 1.8 #skill's adjusted damage

            elif player["skill"] == "Divine Healing": #healing mechanism (if chosen class is Healer)

                if player["hp"] >= player["max_hp"]:
                    print("\nYou are full HP, skill cancelled!")
                
                else:
                    heal = int(player["max_hp"] * 0.2) #heals player based on their max hp
                    player["hp"] += heal
                    player["hp"] = min(player["hp"], player["max_hp"])  #prevent overheal above max HP    
                    print(f"\nYou healed {heal} HP!")
                    
            elif player["skill"] == "Iron Clad": #defense buff mechanism (if chosen class is Tank)
                defense = int(player["defense"] * 0.2) #defense buff calculation
                player["defense"] += defense
                print(f"\nSkill increased your defense by {defense}!")
                

            dmg = skill_dmg - (enemy["defense"] * 0.5) #enemy's defense reduces damage
            dmg = max(1, int(dmg)) #prevents 0 or negative damage
            enemy["hp"] -= dmg
            enemy["hp"] = max(0, enemy["hp"])  #prevent negative enemy HP
            print(f"\nYou dealt {dmg} to the enemy!")
            dmg = 0

        else: #if player typed something out of the choices
            print("\nAction invalid!")
            continue

        print(f"\n{boarder}") #seperator

        #enemy action

        if enemy["hp"] <= 0:
            break

        print(f"\n{enemy['name']}'s TURN TO ATTACK".upper()) #.upper() to change case to capitalized

        print(f"\n{boarder}") #seperator

        action = random.choice(["normal_attack", "heavy_atk"]) #randomized action picker for enemy's action

        if action == "normal_attack":
            print(f"\n{enemy['name']} used normal attack!")
            dmg = enemy["attack"] - (player["defense"] * 0.5) #player's defense reduces damage

        else:
            print(f"\n{enemy['name']} used heavy attack!")
            heavy_dmg = enemy["attack"] * 1.5 #heavy attack's damage calculation
            dmg = heavy_dmg - (player["defense"] * 0.5) #player's defense reduces damage
        
        dmg = max(1, int(dmg)) #prevents 0 or negative damage
        player["hp"] -= dmg #substract dmg to player's hp
        player["hp"] = max(0, player["hp"])  #prevent HP going negative
        print(f"\nYou are hit {dmg} damage!")
        
        print(f"\n{boarder}") #seperator

    #reward system
    if player["hp"] > 0:
        reward = random.randint(10, 40)
        player["gold"] += reward #gives reward
        player["win"] += 1 #tracks win
        print(f"\nYou defeated the {enemy['name']}!")
        return True
    
    else:
        player["defeat"] += 1 #tracks defeat
        print(f"\nYou are defeated by the {enemy['name']}!")
        return False

# SHOP SYSTEM
def shop(player):
        
    while True:

        print("\n~ WELCOME TO THE POTION SHOP ~")
        print(f"\nGold: {player['gold']}")

        print("\n[1] BUY POTIONS | [2] EXIT")

        choice = input("\nEnter choice: ")

        while not choice.isdigit() or int(choice) not in [1, 2]:
            choice = input("\nSelected option invalid. Choose again: ")

        if choice == "1":

            shop_items = {
                "Heal Potion": {"price": 20, "heal": 30},
                "Attack Potion": {"price": 50, "attack": 10},
                "Defense Potion": {"price": 50, "defense": 5}
            }

            while True:

                print(f"\n{boarder}")
                print("\n~ AVAILABLE ITEMS ~")

                item_list = list(shop_items.items())

                for i, (item_name, stats) in enumerate(item_list, start=1):

                    if "heal" in stats:
                        desc = f"Heals {stats['heal']} HP"
                    elif "attack" in stats:
                        desc = f"Boosts Attack by {stats['attack']}"
                    elif "defense" in stats:
                        desc = f"Boosts Defense by {stats['defense']}"
                    else:
                        desc = "No effect"

                    print(f"[{i}] {item_name} - {stats['price']} Gold | {desc}")
                

                choice = input("\nSelect potion to buy: ")

                while not choice.isdigit() or int(choice) not in range(1, len(item_list) + 1):
                    choice = input("\nSelected option invalid. Choose again: ")

                selected_name, selected_stats = item_list[int(choice) - 1]
                price = selected_stats["price"]

                if "heal" in selected_stats and player["hp"] >= player["max_hp"]:
                    print(f"\n{boarder}")
                    print("\nYour HP is already full! You cannot buy a Heal Potion.")
                    continue

                if player["gold"] < price:
                    print("\nYou don't have enough gold!")
                    return

                player["gold"] -= price

                if "heal" in selected_stats:
                    player["hp"] += selected_stats["heal"]
                    player["hp"] = min(player["hp"], player["max_hp"])
                elif "attack" in selected_stats:
                    player["attack"] += selected_stats["attack"]
                elif "defense" in selected_stats:
                    player["defense"] += selected_stats["defense"]

                player["inventory"].append(selected_name)

                print(f"\n{boarder}")
                print(f"\nYou bought {selected_name}!")
                print(f"\nRemaining Gold: {player['gold']}")

                again = input("\nBuy another potion? [yes/no]: ").lower()

                if again == "no":
                    print(f"\n{boarder}")
                    print("\nLeaving shop...")
                    return

        elif choice == "2":
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
                shop(player)

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