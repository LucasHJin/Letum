import random
import os

class Character:
    def __init__(self, name, srn, dex, con, level, exp):
        self.name = name
        self.stats = {
            'str': srn,
            'dex': dex,
            'con': con,
        }
        self.level = level
        self.exp = exp
        self.health = 10
        self.armor_class = 0
        self.attack_damage = 0
        self.inventory = {
            'Gold': 0,
            'Health Potion': 0
        }
        self.current_health = self.health
        self.tabbar = {
            "Poison": 0,
            "Stunned": 0,
            "Weakened": 0,
            "Buffed": 0
        }
        self.equipment = {
            'Head': "None",
            'Body': "None",
            'Ring': "None"
        }
        self.needed_exp = 40
        self.stat_points = 0
        self.is_buffed = False

    def refresh_current_health(self): #for after level up or clear room 
        self.current_health = self.health

    def check_status_bar(self): 
        if self.tabbar["Poison"]>0: #works now
            pDamage = int(self.health*0.05)
            print(" ~ You have been poisoned for", pDamage, "damage. ~ ")
            self.current_health -= pDamage
            self.tabbar["Poison"]-=1 #WORKS
        if self.tabbar["Weakened"]>0:
            self.tabbar["Weakened"]-=1 
        if self.tabbar["Buffed"]==0 and self.is_buffed:
            for st in self.stats:
                self.stats[st]-=5
            self.is_buffed = False
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff
        if self.tabbar["Buffed"]>0 and not self.is_buffed:
            for st in self.stats:
                self.stats[st]+=5
            self.is_buffed = True
            self.tabbar["Buffed"]-=1
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff



            

    def use_health_potion(self):
        self.inventory['Health Potion'] -= 1
        add_health = random.randint(25, 50)
        self.current_health += add_health
        if self.current_health > self.health:
            self.current_health = self.health
        print("Quickly uncorking your health potion, you guzzle it down and feel your body rejuvenate. [+"+str(add_health)+"HP]")
        print("  >>  Health:", self.current_health)

            
    def check_dead(self):
        if self.current_health<=0:
            dead = True
        else:
            dead = False
        return dead

    def calc_health(self):
        self.health = 100 + self.stats['con'] * 2

    def calc_ac(self):
        self.armor_class = 20 + self.stats['dex'] * 2

    def calc_damage(self):
        self.attack_damage = 15 + self.stats['str'] * 3

    def calc_needed_exp(self):
        self.needed_exp = 40*self.level

    def refresh_stats(self):
        self.calc_health()
        self.calc_damage()
        self.calc_ac()
        self.calc_needed_exp()
        self.refresh_current_health()

    def calc_exp(self):
        counter=0
        while self.exp>=self.needed_exp:
            self.exp-=self.needed_exp
            counter += 1
            self.level += 1
            self.calc_needed_exp()
        return counter

    def assign_stat_points(self, repeated_num):
        print("Current Stats:")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        print("  >>  Available Stat Points:", self.stat_points)
        print("{---------------------------------------------------------------}")
        for _ in range(repeated_num):
            print(" ~ Which stat would you like to increase? (str/dex/con) ~ ")
            stat_choice = input("  >>  ")
            good = False
            if stat_choice.lower() in self.stats:
                self.stats[stat_choice] += 1
            else:
                while not good:
                    print(" ~ Invalid choice. Please choose from 'str', 'dex', or 'con'. ~ ")
                    stat_choice = input("  >>  ")
                    if stat_choice.lower() in self.stats:
                        self.stats[stat_choice] += 1
                        good = True
                        print("{---------------------------------------------------------------}")
                        if self.stats.choice.lower() == 'str':
                            print("  >>  Strength:", self.stats['str'], "↑")
                        elif self.stats.choice.lower() == 'dex':
                            print("  >>  Dexterity:", self.stats['dex'], "↑")
                        else:
                            print("  >>  Constitution:", self.stats['con'], "↑")
                        print("{---------------------------------------------------------------}")
        print(" ~ Level up complete! Your stats are now: ~ ")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        input("[Enter any button to continue.]")


        self.calc_health()
        self.calc_damage()
        self.calc_ac()
        self.refresh_current_health()

    def all_level_up(self):
        os.system('cls')
        times = self.calc_exp()
        for _ in range(times):
            self.stat_points += 2
        self.assign_stat_points(self.stat_points)
        self.refresh_stats()

    def add_inventory(self, items):
        for i in items.keys():
            if i in self.inventory:
                self.inventory[i]+=items[i]
            else:
                self.inventory[i]=items[i]


