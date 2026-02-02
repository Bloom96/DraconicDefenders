class MyChar:
    def __init__(self, name, hp, mp, level, char_class, char_race):
        self.Name = name
        self.HP = hp
        self.MP = mp
        self.Level = level
        self.Char_class = char_class
        self.Char_race = char_race
    
    # CHANGE: Only do math here. Do not try to touch the UI.
    def take_damage(self, amount):
        self.HP -= amount
        if self.HP < 0: 
            self.HP = 0 # Prevent negative HP