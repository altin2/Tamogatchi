class Tamo:
    def __init__(self):
        self.HP = 100
        self.Hunger = 100
        self.Happiness = 100
        self.Thirst = 100
        self.Age = 0
        self.Intellegence = 50
        self.Hygiene = 100
        self.weight = 10
        self.Action = False
    def showall(self):
        print(self.HP)
        print(self.Happiness)
        print(self.Hunger)
        print(self.Thirst)
        print(self.Age)
        print(self.Intellegence)
        print(self.Hygiene)
        print(self.weight)
        print(self.Action)

    def feed(self,amt):
        self.Hunger += amt
        if self.Hunger >=100: 
            self.weight = self.weight+((self.Hunger-100)/5)
        return self.Hunger,self.weight
    
    def exercise(self,hours):
        self.Hunger -=(hours*2)
        self.Thirst -=(hours*3)
        self.Hygiene -= (hours*4)
        self.Happiness = self.Happiness+(hours*2)

    def read(self,hours):
        self.Hunger -=hours
        self.Thirst -=hours*3
        self.Intellegence +=hours*2

    def clean(self, amt):
        if not self.Action:
            self.Hygiene += amt
        return self.Hygiene
    
    def grow(self, amt):

        self.Age += amt

        return self.Age
    
    def play(self, time):
        self.Happiness += 10
        self.Hygiene -= 10

        self.Hunger -= 10

    def away(self,hours):

        self.Hunger -= hours*2
tamo = Tamo()