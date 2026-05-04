#enemy list and randomized enemy picking
import random

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

picked_enemy = enemy_picking()
print(picked_enemy)