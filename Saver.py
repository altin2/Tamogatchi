import pygame

class Tamo:
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.name = None
        self.HP = 100
        self.Hunger = 100
        self.Happiness = 100
        self.Thirst = 100
        self.Age = 0
        self.Intellegence = 50
        self.Hygiene = 100
        self.weight = 10
        self.Strength = 50
        self.LastOnline = 0
        self.Action = False

    def carryOver(self):

        return self.Age, self.Intellegence, self.weight, self.Strength

    def showall(self):
        print(self.HP)
        print(self.Happiness)
        print(self.Hunger)
        print(self.Thirst)
        print(self.Age)
        print(self.Intellegence)
        print(self.Hygiene)
        print(self.weight)
        print(self.Strength)
        print(self.Action)
    
    def getterAtt(self): 
        return self.HP, self.Hunger, self.Happiness, self.Thirst, self.Age, self.Intellegence, self.Hygiene, self.weight, self.Strength,self.LastOnline, self.Action,self.name

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
        self.Strength += (hours*2)

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

    #These are to change the variables that go down passively over time
    #they will need to be called each tick in the main while loop
    def checkHunger(self, frameRate):

        if self.Hunger == 0:
            self.HP -= (1/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (0.5/frameRate)
            if self.Hunger > 100:
                self.weight += (1/frameRate)

    def checkThirst(self, frameRate):
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0:
            self.Hunger -= (0.5/frameRate)

    def checkHygiene(self, frameRate):

        if self.Hygiene <= 5:
            self.HP -= (0.5/frameRate)

    def checkAge(self,frameRate, multiplyer = 1):

        growRate = 0.1*multiplyer
        self.Age += (growRate/frameRate)

    def retrunAge(self):

        return self.Age
    
    def checkEvolve(self, evolution):

        if self.Age < 5:
            return 'egg', evolution

        elif (self.Age >= 5) and (self.Age < 10):
            if evolution == 0:
                check_evo = 1
            
            else:
                check_evo = evolution

            return 'child', check_evo
        
        elif (self.Age >= 10) and (self.Age < 50):
            
            if evolution == 1:
                check_evo = 2
            else:
                check_evo == evolution
            
            if evolution != check_evo:
                if (self.Intellegence >= 80) and not(self.Strength > 60):
                    return 'intelligent',check_evo
                    
                elif (self.Strength >= 80) and not(self.Intellegence > 60):
                    return 'strong',check_evo
                    
                else:
                    return 'balanced',check_evo
                
            else:
                return 'same',evolution
        
        #keep adding onto this

class egg(Tamo):

    def __init__(self, state = 0):

        Tamo.__init__(self)
        self.HP = 25
        self.Strength = 10

        if state == 0:
            self.image = pygame.image.load('eggStage1.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif state == 1:
            self.image = pygame.image.load('eggStage2.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif state == 2:
            self.image = pygame.image.load('eggStage3.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif state == 3:
            self.image = pygame.image.load('eggStage4.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]

    def feed(self):

        return 'too young'
    
    def excercise(self):
        
        return 'too young'
    
    def read(self):
        
        return 'too young'
    
class toddler(Tamo):

    def __init__(self):

        Tamo.__init__(self)
        self.HP = 50
        self.Strength = 25
        
        self.state = 0

        if self.state == 0:
            self.image = pygame.image.load('tamoToddler.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]

        elif self.state == 1:
            self.image = pygame.image.load('toddlerPlayAnim1.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]

        elif self.state == 2:
            self.image = pygame.image.load('toddlerPlayAnim2.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]
        
        elif self.state == 3:
            self.image = pygame.image.load('toddlerPlayAnim3.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]
        
        elif self.state == 4:
            self.image = pygame.image.load('toddlerPlayAnim4.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]
        
        elif self.state == 5:
            self.image = pygame.image.load('toddlerPlayAnim5.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]
        
        elif self.state == 6:
            self.image = pygame.image.load('toddlerPlayAnim6.png')
            self.rect = self.image.get_rect()
            #self.rect.topleft = [x_pos,y_pos]

    def setState(self, amt):

        self.state = amt

    def checkHunger(self, frameRate):

        if self.Hunger == 0:
            self.HP -= (1/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (1/frameRate)
            if self.Hunger > 100:
                self.weight += (1/frameRate)

    def checkThirst(self, frameRate):
        #less health and uses food and water quicker
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0:
            self.Hunger -= (1/frameRate)

    def play(self, time):
        self.Happiness += 20
        self.Hygiene -= 10

        self.Hunger -= 15

class balanced1(Tamo):

    def __init__(self,a,i,w,s):

        Tamo.__init__(self)
        self.Age = a
        self.Intellegence = i
        self.Weight = w
        self.Strength = s

class strong1(Tamo):
    #uses hunger and thirst quicker but makes strength quicker
    
    def __init__(self,a,i,w,s):

        Tamo.__init__(self)
        self.Age = a
        self.Intellegence = i
        self.Weight = w
        self.Strength = s

    def checkHunger(self, frameRate):

        if self.Hunger == 0:
            self.HP -= (1/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (1/frameRate)
            if self.Hunger > 100:
                self.weight += (1/frameRate)

    def checkThirst(self, frameRate):
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0:
            self.Hunger -= (1/frameRate)

    def exercise(self,hours):
        self.Hunger -=(hours*2)
        self.Thirst -=(hours*3)
        self.Hygiene -= (hours*4)
        self.Happiness = self.Happiness+(hours*2)
        self.Strength += (hours*4)

class intelligent1(Tamo):
    #uses hunger and thirst quicker but makes intellegence quicker
    
    def __init__(self,a,i,w,s):

        Tamo.__init__(self)
        self.Age = a
        self.Intellegence = i
        self.Weight = w
        self.Strength = s

    def checkHunger(self, frameRate):

        if self.Hunger == 0:
            self.HP -= (1/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (1/frameRate)
            if self.Hunger > 100:
                self.weight += (1/frameRate)

    def checkThirst(self, frameRate):
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0:
            self.Hunger -= (1/frameRate)

    def read(self,hours):
        self.Hunger -=hours
        self.Thirst -=hours*3
        self.Intellegence +=hours*4