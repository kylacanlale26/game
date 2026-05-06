#enemy list and randomized enemy picking
import random

#enemies stats - tuple inside a list
enemies = [
    ("Minion", 50, 4, 5), #name, hp, atk, def
    ("Witch", 60, 10, 10),
    ("Evil Fae", 75, 20, 5),
    ("Dark Husk", 80, 20, 15),
    ("Dragon", 100, 25, 20)
]

#randomized enemy picking
def enemy_picking():
    enemy = random.choice(enemies)
    return {"name": enemy[0], "hp": enemy[1], "attack": enemy[2], "defense": enemy[3]}

enemy = enemy_picking()