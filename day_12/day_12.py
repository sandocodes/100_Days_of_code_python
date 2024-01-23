############# Namespaces: Local vs Global Scope #################

##### Always try to avoid modifying a global scope ###########
enemies = 1

def increase_enecmies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enecmies()
print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)


# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()
# game()
# print(player_health)



# There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombies", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)