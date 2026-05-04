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

import random

#user input details
def player_details():
    player_name = input("Enter Name: ")

    #dictionary - classes along with their respective stats that the players can choose from
    player_class = {
        "Knight": {"HP": 150, "Attack": 30, "Defense": 25, "Skill": "Power Slash"},
        "Assasin": {"HP": 100, "Attack": 50, "Defense": 15, "Skill": "Shadow Strike"},
        "Mage": {"HP": 80, "Attack": 40, "Defense": 5, "Skill": "Wind Punch"},
        "Healer": {"HP": 300, "Attack": 10, "Defense": 20, "Skill": "Divine Healing"},
        "Tank": {"HP": 200, "Attack": 25, "Defense": 200, "Skill": "Iron Skin"}
    }