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


#Make descriptions for each with conditionals
print("Welcome to the mystical realm of Letum, where Gods are born and killed. What is your name, oh fine warrior?")
name = input("  >>  ")
print("Of what origin are you? [Enter your stats below (str, dex, con)]")
stats = input("  >>  ").split()
print("And what mighty weapon do you wield? [Sword, Dagger, Staff]")
weapon_input = input("  >>  ")

player = Character(name=name, str=int(stats[0]), dex=int(stats[1]), con=int(stats[2]), level=1, exp=0)

if weapon_input.lower()=="sword":
    weapon = Sword(name="Old Iron Sword", rarity="Common", character=player)

player.refresh_stats()

print(player.health)
print(player.attack_damage)
print(weapon.damage_multiplier)
print(weapon.damage)
print(weapon.slash())