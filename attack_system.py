import random

print("~ WELCOME TO THE DUNGEONS ~") #welcome title

# CREATE PLAYER
def create_player():

    #input - player's name
    player_name = input("\nEnter Name: ")

    #dictionary - classes along with their respective stats that the players can choose from
    class_choices = {
        "Knight": {"hp": 120, "attack": 30, "defense": 25, "skill": "Power Slash"},
        "Assassin": {"hp": 100, "attack": 50, "defense": 15, "skill": "Shadow Strike"},
        "Mage": {"hp": 80, "attack": 40, "defense": 5, "skill": "Wind Punch"},
        "Healer": {"hp": 300, "attack": 10, "defense": 20, "skill": "Divine Healing"},
        "Tank": {"hp": 150, "attack": 25, "defense": 200, "skill": "Iron Clad"}
    }

    #input - player choose class
    print("\nClasses: ")
    for c in class_choices:
        print("-", c)

    choice = input("\nChoose your Class: ").title()

    #validate choice
    while choice not in class_choices:
        choice = input("\nSelected class invalidKyla. Choose again: ").title()

    #copy selected class' stats
    player = class_choices[choice].copy()

    #additional player data - add items to dictionary class_choice
    player["name"] = player_name
    player["class"] = choice
    player["gold"] = 150
    player["inventory"] = [] #list - inventory storage

    return player

player = create_player()
 
line = "=" * 5

#list - to reorder dictionary
order = ["name", "class", "hp", "defense", "skill", "gold", "inventory"]

#displays player's info vertically
print(f"\n{line}Player Info{line}")
for key in order:
    print(f"{key.capitalize():<10}: {player[key]}")

# ENEMY RANDOMIZER

#enemies stats - tuple inside a list
enemies = [
    ("Minion", 100, 8, 5), #name, hp, atk, def
    ("Witch", 120, 15, 10),
    ("Evil Fae", 200, 25, 5),
    ("Dark Husk", 200, 30, 15),
    ("Dragon", 500, 50, 20)
]

#randomized enemy picking
def enemy_picking():
    enemy = random.choice(enemies)
    return {"name": enemy[0], "hp": enemy[1], "attack": enemy[2], "defense": enemy[3]}

# BATTLE SYSTEM

def battle(player, enemy):

    print(f"\n{enemy['name']} has spawned!")

    while enemy['hp'] > 0 and player['hp'] > 0: #attack loop
        print(f"\n{player['name']} HP: {player['hp']}")
        print(f"\n{enemy['name']} HP: {enemy['hp']}")

        # PLAYER ACTION
        print("\nYOUR TURN!")
        print("\nBattle Actions: Normal Attack | Skill")
        action = input("Choose: ").lower() 
            #.lower() to change case to lower case

        if action == "normal attack":
            print("\nYou used normal attack!")
            dmg = player["attack"] - random.randint(0, enemy["defense"]) #defense mechonism - calculate player damage by subtracting random defense value based on enemy's defense
            dmg = max(1, int(dmg)) #prevent negative damage
            enemy["hp"] -= dmg #substract dmg to enemy's hp
            print(f"\nYou dealt {dmg} to the enemy!")

        #skills system
        elif action == "skill":
            print(f"{player['skill']}!")
            skill_dmg = player["attack"] * 2 #skill's damage is double the player's atk
            dmg = skill_dmg - random.randint(0, enemy["defense"]) #defense mechonism - calculate player damage by subtracting random defense value based on enemy's defense
            dmg = max(1, int(dmg)) #prevent negative damage
            enemy["hp"] -= dmg
            print(f"\nYou dealt {dmg} to the enemy!")

        else: #if player typed something out of the choices
            print("\nAction invalid!")

        #check if enemy is defeated
        if enemy["hp"] <= 0:
            print(f"\n You defeated {enemy['name']}")
            break

        #enemy action
        print(f"\n{enemy['name']}'s TURN".upper()) #.upper() to change case to capitalized

        action = random.choice(["normal_attack", "heavier_atk"]) #randomized action picker for enemy's action

        if action == "normal_attack":
            print(f"\n{enemy['name']} used normal attack!")
            dmg = enemy["attack"] - random.randint(0, player["defense"]) #defense mechonism - calculate enemy damage by subtracting random defense value based on player's defense
            dmg = max(1, int(dmg)) #prevent negative damage
            player["hp"] -= dmg #substract dmg to player's hp
            print(f"\nYou are hit {dmg} damage!")

        elif action == "heavier_atk":
            print(f"\n{enemy['name']} used heavy attack!")
            heavy_dmg = enemy["attack"] * 1.5 #heavy attack's damage calculation
            dmg = heavy_dmg - random.randint(0, player["defense"]) #defense mechonism - calculate enemy damage by subtracting random defense value based on player's defense
            dmg = max(1, int(dmg)) #prevent negative damage
            player["hp"] -= dmg #substract dmg to player's hp
            print(f"\nYou are hit {dmg} heavy damage!")
        
        #check if player is defeated
        if player["hp"] <= 0:
            print(f"\nYou are defeated by {enemy['name']}!")
            break

enemy = enemy_picking()
battle(player, enemy)