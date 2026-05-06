import enemy
import player

import random

boarder = "=" * 30

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
        print("\nBattle Actions (Number): [1] Normal Attack | [2] Skill")
        action = input("Choose: ").lower() 
            #.lower() to change case to lower case

        print(f"\n{boarder}") #seperator

        if action == "1":
            print("\nYou used normal attack!")
            dmg = player["attack"] - (enemy["defense"] * 0.5) #enemy's defense reduces damage
            dmg = max(1, int(dmg)) #prevents 0 or negative damage
            enemy["hp"] -= dmg #substract dmg to enemy's hp
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
                    print(f"\nYou healed {heal} HP!")
                    

            elif player["skill"] == "Iron Clad": #defense buff mechanism (if chosen class is Tank)
                defense = int(player["defense"] * 0.2) #defense buff calculation
                player["defense"] += defense
                print(f"\nSkill increased your defense by {defense}!")
                
            
            dmg = skill_dmg - (enemy["defense"] * 0.5) #enemy's defense reduces damage
            dmg = max(1, int(dmg)) #prevents 0 or negative damage
            enemy["hp"] -= dmg
            print(f"\nYou dealt {dmg} to the enemy!")

        else: #if player typed something out of the choices
            print("\nAction invalid!")
            continue

        print(f"\n{boarder}") #seperator

        #check if enemy is defeated
        if enemy["hp"] <= 0:
            print(f"\nYou defeated the {enemy['name']}!")
            print(f"\n{boarder}") #seperator
            break

        #enemy action
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
        print(f"\nYou are hit {dmg} damage!")
        
        print(f"\n{boarder}") #seperator

        #check if player is defeated
        if player["hp"] <= 0:
            print(f"\nYou are defeated by the {enemy['name']}!")
            print(f"\n{boarder}") #seperator
            break

# RESULT

# def results()

battle(player, enemy)