class Character:
    def __init__(self, name, srn, dex, con, level, exp):
        self.name = name
        self.stats = {
            'str': srn,
            'dex': dex,
            'con': con,
        }
        self.level = level
        self.health = 10
        self.armor_class = 0
        self.attack_damage = 0
        self.exp = exp

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

    def level_up(self):
        print("Congratulations! You have leveled up.")
        print("You have 3 points to distribute among your stats.")
        print("Current stats:", self.stats)
        
        for _ in range(3):
            stat_choice = input("Which stat would you like to increase? (str/dex/con): ").lower()
            if stat_choice in self.stats:
                self.stats[stat_choice] += 1
            else:
                print("Invalid choice. Please choose from 'str', 'dex', or 'con'.")
        
        self.level += 1

        print("Level up complete! Your stats are now:", self.stats)

        self.calc_health()
        self.calc_damage()
        self.calc_ac()


