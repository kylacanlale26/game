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
 
#===START OF CODE===#

import random

#player data
def player_data():

    #input - player's name
    player_name = input("Enter Name: ")

    #dictionary - classes along with their respective stats that the players can choose from
    class_choices = {
        "Knight": {"hp": 120, "attack": 30, "defense": 25, "skill": "Power Slash"},
        "Assassin": {"hp": 100, "attack": 50, "defense": 15, "skill": "Shadow Strike"},
        "Mage": {"hp": 80, "attack": 40, "defense": 5, "skill": "Wind Punch"},
        "Healer": {"hp": 300, "attack": 10, "defense": 20, "skill": "Divine Healing"},
        "Tank": {"hp": 150, "attack": 25, "defense": 200, "skill": "Iron Clad"}
    }

    #player choice input
    print("\nClasses: ")
    for c in class_choices:
        print("-", c)

    choice = input("\nChoose your Class: ").title()

    #validate choice
    while choice not in class_choices:
        choice = input("\nSelected class invalidKyla. Choose again: ").title()

    #copy selected class stats
    player = class_choices[choice].copy()

    #additional player data
    player["name"] = player_name
    player["class"] = choice
    player["gold"] = 150
    player["inventory"] = []
    player["skills_used"] = set()

    return player

player = player_data()

print(player)