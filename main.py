from Character import *
from Scene import *
import random
import os

def display_menu():
    print("Menu")
    print('Please choose one of the following actions: ')
    print("Actions: Attack, Move, Heal")

def print_map(rooms):
    for y in range(rooms.height-1, -1, -1):
        top_wall = ""
        top_middle = ""
        middle = ""
        bottom_middle = ""
        for x in range(0, rooms.width):
            top_wall += "+---"
            top_middle += "|   "
            middle += "| "
            bottom_middle += "|   "
            if (x, y) == rooms.player:
                if (x, y) in rooms.enemies.values():
                    middle += 'O'
                else:
                    middle += 'X'
            elif (x, y) in rooms.enemies.values():
                middle += 'E'
            else:
                middle += " "
            middle += " "
        print(top_wall + "+")
        print(top_middle + "|")
        print(middle + "|")
        print(bottom_middle + "|")
    bottom_wall = ""
    for x in range(0, rooms.width):
        bottom_wall += "+---"
    print(bottom_wall + '+')

def main():
    username = input("What would you like your username to be?: ")
    player = Character(username)
    character_type = input("What character type would you like to play? (Tank, Healer, Damage): ")
    if character_type == 'Tank':
        player = Tank(username)
    elif character_type == 'Healer':
        player = Healer(username)
    enemy_count = random.randint(2, 4)
    enemies = {}
    for enemy in range(enemy_count):
        enemies[enemy] = Enemy(f"Enemy {enemy}", random.randint(5, 100), random.uniform(2, 3))
    rooms = Scene(random.randint(1, enemy_count), random.randint(1, enemy_count), enemy_count)
    win = False
    player.get_shield_and_sword()
    while (player.health > 0) and not win:
        print_map(rooms)
        display_menu()
        action_choice = input("Which action would you like to do: ")
        if action_choice.lower() == "attack" or action_choice.lower() == 'a':
            if enemy_count > 0:
                if rooms.enemy_exists():
                    print(f"Your health: {player.health}")
                    print(f"Enemy health: {enemies[rooms.get_enemy_index()].health}")
                    player.attack(enemies[rooms.get_enemy_index()])
                    if enemies[rooms.get_enemy_index()].health > 0:
                        print(f"Enemy's new health: {enemies[rooms.get_enemy_index()].health}")
                        enemies[rooms.get_enemy_index()].attack(player)
                        if player.health <= 0:
                            print("The enemy killed you. You lose!")
                            win = True
                        else:
                            print(f"Your new health: {player.health}")
                    elif enemies[rooms.get_enemy_index()].health <= 0:
                        print('Enemy died')
                    if enemies[rooms.get_enemy_index()].health <= 0:
                        enemies.pop(rooms.get_enemy_index())
                        rooms.remove_enemy()
                        if len(enemies) == 0:
                            print("You won!")
                            win = True
                else:
                    print("There are no enemies in this room, so you cannot attack. ")
            else:
                print("All of the enemies have been defeated. ")
                win = True

        elif action_choice.lower() == "move" or action_choice.lower() == 'm':
            print("Menu")
            print("Here are the directions you can move in: ")
            movement = input("Forward(w), Backward(s), Left(a), Right(d): ")
            if movement.lower() == 'w' or movement.lower() == 'forward':
                rooms.update_player_loc(player.move('forward'))
            elif movement.lower() == 's' or movement.lower() == 'backward':
                rooms.update_player_loc(player.move('backward'))
            elif movement.lower() == 'a' or movement.lower() == 'left':
                rooms.update_player_loc(player.move('left'))
            elif movement.lower() == 'd' or movement.lower() == 'right':
                rooms.update_player_loc(player.move('right'))
            else:
                print("You typed in an invalid direction. ")

        elif action_choice.lower() == "heal" or action_choice.lower() == 'h':
            print(f'Current health: {player.health}')
            player.heal(10)
            print(f'New health: {player.health}')

        else:
            print("You typed in an invalid action. ")
        os.system('cls' if os.name == 'nt' else 'clear')
main()