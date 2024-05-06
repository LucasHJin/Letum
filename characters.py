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
        self.tabbar = {}
        self.equipment = {
            'Head': "None",
            'Body': "None",
            'Ring': "None"
        }

    def refresh_current_health(self): #for after level up or clear room (REMEMBER)!
        self.current_health = self.health

    def check_status_bar(self):
        for effect in self.tabbar.keys():
            if effect=="Poison":
                pDamage = self.health*0.05
                for i in range(self.tabbar[effect]):
                    print(" ~ You have been poisoned for", pDamage, "damage. ~ ")
                    self.current_health -= pDamage
                self.tabbar[effect]-=1
            elif effect == "Stunned":
                #do something... (skip turn)
                temp = 1

            
    def check_dead(self):
        if self.current_health<=0:
            dead = True
        else:
            dead = False
        return dead

    def calc_health(self):
        self.health = 100 + self.stats['con'] // 2

    def calc_ac(self):
        self.armor_class = 35 + self.stats['dex'] // 3

    def calc_damage(self):
        self.attack_damage = 20 + self.stats['str'] // 2

    def refresh_stats(self):
        self.calc_health()
        self.calc_damage()
        self.calc_ac()

    def calc_exp(self):
        counter=0
        while self.exp>self.level*50:
            self.exp-=self.level*50
            counter+=1
        return counter
    
    def add_exp(self, amount):
        self.exp+=amount

    def level_up_once(self):
        print(" ~ Congratulations! You have leveled up. ~ ")
        print(" ~ You have 3 points to distribute among your stats. ~ ")
        print(" ~ Current stats:", self.stats, "~ ")
        
        for _ in range(3):
            stat_choice = input(" ~ Which stat would you like to increase? (str/dex/con): ~ ").lower()
            if stat_choice.lower() in self.stats:
                self.stats[stat_choice] += 1
            else:
                print(" ~ Invalid choice. Please choose from 'str', 'dex', or 'con'. ~ ")
        
        self.level += 1

        print(" ~ Level up complete! Your stats are now:", self.stats, "~ ")

        self.calc_health()
        self.calc_damage()
        self.calc_ac()
        self.refresh_current_health()

    def all_level_up(self):
        times = self.calc_exp()
        for i in range(times):
            self.level_up_once()

    def add_inventory(self, items):
        for i in items.keys():
            if i in self.inventory:
                self.inventory[i]+=items[i]
            else:
                self.inventory[i]=items[i]


