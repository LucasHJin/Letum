"""
Final Project
ICS3U
Lucas Jin
This is a DnD based text-adventure role playing game. Based on the timeless genre, it is made with OOP and uses a variety of concepts such as functions, lists, dictionaries, variables, etc.
History:
April 13, 2023: Program Creation
"""
from characters import Character
from weapons import Sword
import os
import time

#FUNCTIONS
def look_around(enemyNumber, enemyType, itemNumber, itemType):
    if enemyNumber>0:
        print("STuff", enemyType)
    if itemNumber>0:
        print("As you look around, examining every nook and cranny, you see a", itemType, "hidden in the corner.")
    if itemNumber<=0 and enemyNumber<=0:
        print("It appears as if there is nothing in this room.")

def open_chest(rand, items):
    rand = 1

def check_profile(person, weapon):
    print(person.name)
    print("Level:", person.level)
    print("Experience:", person.exp+"/"+person.level*50)
    print("{---------------------------------------------------------------}")
    print("  >>  Health:", person.health)
    print("  >>  Weapon:", weapon.name)
    print("{---------------------------------------------------------------}")
    print("  >>  Strength:", person.stats['str'])
    print("  >>  Dexterity", person.stats['dex'])
    print("  >>  Constitution", person.stats['con'])
    print("{---------------------------------------------------------------}")

def print_options(statements):
    for k, v in statements.items():
        print("  ["+k+"] "+v)

def not_option(statements):
    print("That is not an option. The option(s) are: ")
    print_options(statements)
    temp = input("  >>  ")
    return temp


#CHARACTER CREATION
os.system('cls')

print("Welcome to the mystical realm of Letum, where Gods are born and killed. What is your name, oh fine warrior?")
name = input("  >>  ")
print("And of what origin are you "+name+"? [Enter your stats below (str, dex, con). Enter [help] for an explanation.]")
stats_input = input("  >>  ").split(", ")

if stats_input[0].lower()=="help":
    print("\nWithin the realm of Letum, your abilites are governed by 3 stats:")
    print("  >>  Strength: The stat of the strong and bold, strength grants you the ability to wield your weapon with more efficiency, granting extra damage.")
    print("  >>  Dexterity: The stat of the swift and unseen, dexterity grants you the ability to dodge damage and critically strike.")
    print("  >>  Constitution: The stat of the reliable and resilient, constitution grants you a health equalling your indominatable will.\n")
    print("With that knowledge, I ask you once again, of what origin are you? [Enter your stats below (str, dex, con).]")
    stats_input = input("  >>  ")
    stats_input.split(", ")

check = True

while check:
    #change str to int in list
    for i in range(len(stats_input)):
        stats_input[i] = stats_input[i].lstrip("-")
        if stats_input[i].isdigit():
            stats_input[i] = int(stats_input[i])

    if (len(stats_input)!=3):
        print("You must have 3 stats and they must all be integers. [Enter your stats below (str, dex, con).]")
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    elif (stats_input[0]+stats_input[1]+stats_input[2])!=30 or stats_input[0]==0 or stats_input[1]==0 or stats_input[2]==0 or len(stats_input)!=3:
        print("Your stats must sum up to 30 and each one must have at least 1 stat point assigned to it. [Enter your stats below (str, dex, con).]")
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    else:
        check = False

print("\nThank you for revealing our stats.")
print("Good luck, and may you leave behind a legacy worthy of your name.")

time.sleep(2)

#START OF THE GAME

os.system('cls')

possible = {"L": "Look Around"}

print("You awake groggily, your eyes slowly adapting to the darkness that envelops you. As you lie there, wondering if it is simply a bad dream, you hear a noise skitter by you.")
print_options(possible)
choice = input("  >>  ")
while choice.lower() != "l":
    choice = not_option(possible)

look_around(0, 0, 1, "rotting wooden chest")

possible = {"O": "Open The Chest"}
print("What will you do?")
print_options(possible)
while choice.lower() != "o":
    choice = not_option(possible)



weapon_input = input("  >>  ")

player = Character(name=name, str=int(stats_input[0]), dex=int(stats_input[1]), con=int(stats_input[2]), level=1, exp=0)

if weapon_input.lower()=="sword":
    weapon = Sword(name="Old Iron Sword", rarity="Common", character=player)

player.refresh_stats()

print(player.health)
print(player.attack_damage)
print(weapon.damage_multiplier)
print(weapon.damage)
print(weapon.slash())