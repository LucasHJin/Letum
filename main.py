"""
Final Project
ICS3U
Lucas Jin
This is a DnD based text-adventure role playing game. Based on the timeless genre, it is made with OOP and uses a variety of concepts such as functions, lists, dictionaries, variables, etc.
History:
April 13, 2023: Program Creation
"""

#DROP ARMOUR AND WEAPONS?!!! AND CHEST
#FIX AFTER FINISHING R1, GOES TO R2 WITH 0 IN EVERYTHING -> NEED TO GO THROUGH TOP PART AGAIN
#OPTIONAL -> ORDER ITEMS IN SHOP
#OPTIONAL -> MAKE NUMBERS INSTEAD OF NAMES FOR ENEMIES
#REPLACE ALL THE ARMOR NAMINGS WITH ONE CONSISTENT NAMING


from characters import Character
from weapons import Sword
from battles import Battle
from armor import Head
from armor import Body
from armor import Ring
import os
import time
from shops import Shop
import random
#https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out MAYBE

#FUNCTIONS
def open_chest(items):
    for i in items.keys():
        if not isinstance(i, Sword) and not isinstance(i, Head) and not isinstance(i, Body) and not isinstance(i, Ring):
            print(i+":", items[i])
        else:
            print(i.name+":", items[i])

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

print(" ~ Hello, I am the Creator. I have brought you to the mystical realm of Letum, where Gods are born and killed. You will recognize my communications with you through '~' symbols. ~ ")
print(" ~ What is your name, oh fine warrior? ~ ")
name = input("  >>  ")
print(" ~ And of what origin are you "+name+"? [Enter your stats below (str, dex, con). Enter [help] for an explanation.] ~ ")
stats_input = input("  >>  ").split(", ")

if stats_input[0].lower()=="help":
    print("\nWithin the realm of Letum, your abilites are governed by 3 stats:")
    print("  >>  Strength: The stat of the strong and bold, strength grants you the ability to wield your weapon with more efficiency, granting extra damage.")
    print("  >>  Dexterity: The stat of the swift and unseen, dexterity grants you the ability to dodge damage and critically strike.")
    print("  >>  Constitution: The stat of the reliable and resilient, constitution grants you a health equalling your indominatable will.\n")
    print(" ~ With that knowledge, I ask you once again, of what origin are you? [Enter your stats below (str, dex, con).] ~ ")
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
        print(" ~ You must have 3 stats and they must all be integers. [Enter your stats below (str, dex, con).] ~ ")
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    elif (stats_input[0]+stats_input[1]+stats_input[2])!=30 or stats_input[0]==0 or stats_input[1]==0 or stats_input[2]==0 or len(stats_input)!=3:
        print(" ~ Your stats must sum up to 30 and each one must have at least 1 stat point assigned to it. [Enter your stats below (str, dex, con).] ~ ")
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    else:
        check = False

print("\n ~ Thank you for revealing our stats. ~ ")
print(" ~ Your goal is simple. It is to survive as long as possible against an endless horde of monsters. ~ ")
print(" ~ Good luck, and may you leave behind a legacy worthy of your name. ~ ")

time.sleep(1.5)

#START OF THE GAME

#clear screen
os.system('cls')

possible = {"L": "Look Around"}

print("You awake groggily, your eyes slowly adapting to the darkness that envelops you. As you lie there, wondering if it is simply a bad dream, you hear a noise skitter by you.")
print_options(possible)
choice = input("  >>  ")
while choice.lower() != "l":
    choice = not_option(possible)

print("As you look around, you see a rotten wooden chest a few metres to your left. You approach it, wondering what it could possibly contain.")

possible = {"O": "Open The Chest"}
print("What will you do?")
print_options(possible)
choice = input("  >>  ")
while choice.lower() != "o":
    choice = not_option(possible)

print("\nAs you open the rotting chest, its hinges slowly creaking like the gutteral roar of a ghastly beast, you notice a reflective piece of metal within it. Looking closer, you make out the shape of a sword. Suddenly, it disappears, followed by vocal notifications, seemingly from the same 'Creator' you spoke to previously.")

#player = Character(name=name, srn=int(stats_input[0]), dex=int(stats_input[1]), con=int(stats_input[2]), level=1, exp=0)
#only do ^^ if there are optional paramaters that could be passed but aren't
player = Character(name, int(stats_input[0]), int(stats_input[1]), int(stats_input[2]), 1, 0)
weapon = Sword("Old Iron Sword", "Common", player, 0, 0, 0, 0, 0)
player.equipment['Weapon'] = weapon
#refresh stats to set proper stats (like initializing) for player
player.refresh_stats()
#add obtained items to inventory

contain = {
    'Gold': 100,
    'Health Potion': 5,
    weapon: 1
}
open_chest(contain)

player.add_inventory(contain)

print(" ~ This is a magical chest. Each time you defeat a wave of monsters, it will be refilled with random items. It may contain gold, health potions, weapons or armor. ~ ")
print(" ~ You might have seen notifications earlier stating that you obtained 100 Gold and 5 Health Potions. All material things will be put in your inventory or equipped onto your body. To check your equipped items, stats, health and more, you will need to access your status. ~ ")
print(" ~ To check what is in your inventory, press [I] when prompted for an input. ~ ")
print(" ~ If you want to check your status and your equipped items, press [S] when prompted for an input. ~ ")
print(" ~ Once finished learning the basics, press [C] to continue. ~ ")

possible = {
    "I": "Open Inventory",
    "S": "Open Status",
    "C": "Continue"
}
print("\nWhat will you do?")
print_options(possible)
choice = input("  >>  ")
while choice.lower() != "c":
    if choice.lower() == "i":
        player.check_inventory()
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")
    elif choice.lower() == "s":
        player.check_profile()
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")
    elif choice.lower() != "c":
        print(" ~ That was not one of the options. The options are: ~ ")
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")

print("As you wonder what to do now, you here once again the voice in your head.")
print(" ~ I'm unable to say much else due to restrictions but I will try to reveal as much as possible. ~ ")
print(" ~ Very soon, you will be thrust into your first battle. You will have to fight all sorts of horrendous monsters but, if you manage to escape unscathed, you will be much stronger. ~ ")
print(" ~ Additionally, there is one more way to get better equipment and weapons. ~")
print(" ~ Look to your right. ~")
print("Looking to your right, you see a stall, populated with a human like figure. Looking closer, you realise it is a dwarf. Wondering how you never noticed it, the voice suddenly exclaims")
print(" ~ Be not scared. I teleported my loyal follower, Kun, to your location to aid you in your survival. He will sell you items and... who knows, maybe he'll be able to help you with your mentality as well. ~")
print("With that statement, you hear a sudden bang.")
print(" ~ Sorry, it appears I am unable to say more. Good luck! ~ ")
input("[Enter any key to continue.]")


eyDict = {
    'Rat': [3, 0, 0],
    'Goblin': [0, 0, 0],
    'Skeleton': [0, 0, 0],
    'Demon': [0, 0, 0]
}
rnd = Battle(eyDict, player, weapon)
result_temp = "TEMP"
round_counter = 0

shop = Shop(player)
shop.create_items([10, 10, 10, 10])

POSSIBLE = {
    "I": "Open Inventory",
    "S": "Open Status",
    "B": "Buy Items from the Shop",
    "E": "Equip Equipment",
    "F": "Fight"
}


os.system('cls')
print("What will you do now?")
print_options(POSSIBLE)
choice = input("  >>  ")

while result_temp != "DEAD":
    while choice.lower() != "f":
        if choice.lower() == "i":
            player.check_inventory()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        elif choice.lower() == "s":
            player.check_profile()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        elif choice.lower() == "b":
            shop.open_shop()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        elif choice.lower() == "e":
            player.equip_equipment()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        elif choice.lower() != "f":
            print(" ~ That was not one of the options. The options are: ~ ")
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")

    print("ROUND", round_counter+1)
    print("{---------------------------------------------------------------}")
    result = rnd.entire_game()
    round_counter += 1
    result_temp = result

    generate_multipliers = {
        'Rat': [5, 3, 1.5],    
        'Goblin': [2.5, 1.8, 1.2], 
        'Skeleton': [1.5, 1, 0.8], 
        'Demon': [0.8, 0.3, 0.1]
    }

    for enemy in eyDict:
        for enemy_type_num in range(len(eyDict[enemy])):
            #amount of enemies
            amount_enemies = round_counter//10 + random.randint(0, round_counter//5)
            #multiplier for having more weaker enemies and less stronger enemies
            amount_enemies *= int(generate_multipliers[enemy][enemy_type_num])
            eyDict[enemy][enemy_type_num] = amount_enemies

    rnd.enemiesDict = eyDict

print("YOU SURVIVED", round_counter, "ROUNDS. CONGRATULATIONS,", player.name+".")