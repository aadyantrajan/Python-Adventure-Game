from Character import *
from Scene import *

def main():
    username = input("What would you like your username to be?: ")
    character_type = input("What character type would you like to play? (Tank, Healer, Damage): ")
    player_character = Character(username)
    print(player_character.health)
    player_character.attack(player_character)
    print(player_character.health)
main()