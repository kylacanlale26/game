#player data - name, class and stats, and additional data
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

    choice = input("\nChoose your Class (Number): ")

    #validate choice - checks if input is a digit or not included in the choices
    while not choice.isdigit() or int(choice) not in range(1, len(class_list) + 1):
        choice = input("\nSelected class invalid. Choose again: ")

    choice = class_list[int(choice) - 1]

    #copy selected class' stats
    player = class_choices[choice].copy()

    #additional player data - add items to dictionary class_choice
    player["name"] = player_name
    player["class"] = choice
    player["win"] = [] #list - win storage
    player["gold"] = 150
    player["inventory"] = [] #list - inventory storage

    player["max_hp"] = player["hp"] #sets max hp for the healer

    return player

player = create_player()
 
line = "=" * 5

#list - to reorder dictionary
order = ["name", "class", "hp", "defense", "skill", "gold", "inventory"]

#displays player's info vertically
print(f"\n{line}Player Info{line}")
for key in order:
    print(f"{key.capitalize()}: {player[key]}")