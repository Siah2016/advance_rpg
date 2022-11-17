intro = "Welcome to Central World"
print(intro)

sub_intro = "You are stuck in a cave with monsters. Are you able to survive?"
print(sub_intro)
print("Good luck!!")
print()

import random
from characters import *

print("Rimuru has encountered Black Serpent! (Level : 3, Health: 100)")
def run():

    def battle(character_one, character_two):
        
        while character_one["health"] > 0 and character_two["health"] > 0:
        # Character One attack
            random_attack = random.choice(character_one["skills"])
            print()
            print(f'{character_one["name"]} attacks {character_two["name"]} with {random_attack[0]}! ({random_attack[1]} damage)')
            print()
            character_two["health"] -= random_attack[1]
            print()
            print (f'{character_two["name"]} has {character_two["health"]} health left.')
            print()
            if character_two['health'] > 0:
            # Character Two attack
                random_attack = random.choice(character_two['skills'])
                print(f'{character_two["name"]} attacks {character_one["name"]} with {random_attack[0]}! ({random_attack[1]} damage)')
                character_one["health"] -= random_attack[1]
                print()
                print (f'{character_one["name"]} has {character_one["health"]} health left!')
                print()
        pass
    battle(my_hero, enemy_list[0])
    if my_hero['health'] > 0:
        my_hero['equipment'].update(enemy_list[0]['equipment'])
        my_hero['coins'].update(enemy_list[0]['coins'])
        print('+ Snake Fangs added to inventory')
        print('+ Dark Snake Scales added to inventory!')
        print()
        print('+ 35 Copper Coins!')
        print('+ 15 Silver Coins!')
        print('+ 4 Gold Coins!')
        print()
        my_hero['level'] += 1 
        print(f'{my_hero["name"]} has leveled up!!')
        print(f'{my_hero["name"]} has gained a new skill')
        
        n_attack = input("Please enter new skill name:")
        n_skill = ((n_attack, random.randint(1, 100)))
        add_skill = my_hero['skills'] + n_skill
        print(f'Added {n_attack} with {n_skill[1]} power level.')
    elif my_hero["health"] <= 0:
        print("Gameover!!")
    print()
    print("Rimuru has encountered Black Spider! (Level : 5, Health: 100")

    battle(my_hero, enemy_list[1])
    if my_hero['health'] > 0:
        my_hero['equipment'].update(enemy_list[1]['equipment'])
        my_hero['coins'].update(enemy_list[1]['coins'])
        print('+ Poison Cloak added to inventory')
        print()
        print('+ 40 Copper Coins!')
        print('+ 20 Silver Coins!')
        print('+ 8 Gold Coins!')
        print()
        my_hero['level'] += 1
        print(f'{my_hero["name"]} has leveled up!!')
        print(f'{my_hero["name"]} has gained a new skill')
        new_attack = input("Please enter new skill name:")
        new_skill = ((new_attack, random.randint(1, 100)))
        add_skill = my_hero['skills'] + new_skill
        print(f'Added {new_attack} with {new_skill[1]} power level.')

    elif my_hero["health"] <= 0:
        print("Gameover!!")

    print("Rimuru has encountered Giant Bat! (Level : 7, Health: 100")

    battle(my_hero, enemy_list[2])
    if my_hero['health'] > 0:
        my_hero['equipment'].update(enemy_list[2]['equipment'])
        my_hero['coins'].update(enemy_list[0]['coins'])
        print('+ Black Cape added to inventory')
        print('+ Leather Boots added to inventory!')
        print()
        print('+ 50 Copper Coins!')
        print('+ 25 Silver Coins!')
        print('+ 12 Gold Coins!')
        print()
        my_hero['level'] += 1
        print()
        print(f'{my_hero["name"]} has leveled up!!')
        print(f'{my_hero["name"]} has gained a new skill')
        ne_attack = input("Please enter new skill name:")
        ne_skill = ((ne_attack, random.randint(1, 100)))
        add_skill = my_hero['skills'] + ne_skill
        add_skill
        print(f'Added {ne_attack} with {ne_skill[1]} power level.')
        print("You Win!!!")

    elif my_hero["health"] <= 0:
        print("Gameover!!")

run()



