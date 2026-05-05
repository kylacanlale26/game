# Simple dungeon text based game
# where the player can input their name
# have their own stats
# you provide the player classes to choose from your own declared classes
# attack system
# defense and skill mechanism or additional mechanisim
# complete
# gold and shop system
# end game
# use list, tuple, dictionary, set
 
#   START OF CODE

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
    ("Minion", 100, 8, 5),
    ("Witch", 120, 15, 10),
    ("Evil Fae", 200, 25, 5),
    ("Dark Husk", 200, 30, 15),
    ("Dragon", 500, 50, 20)
]

#randomized enemy picking
def enemy_picking():
    enemy = random.choice(enemies)
    return {"name": enemy[0], "hp": enemy[1], "attack": enemy[2], "defense": enemy[3]}

# ATTACK SYSTEM

#   skill system

# SHOP SYSTEM

# GAME LOOP