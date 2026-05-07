import player

boarder = "=" * 30

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

shop(player)