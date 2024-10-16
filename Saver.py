import pygame
import os
#hi 
class Tamo(pygame.sprite.Sprite):
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
        self.Temp = 50
    def checkdeath(self):
        if self.HP <= 0:
            print("TAMO IS DEAD")
            return True
    def resetstats(self):
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
        self.Temp = 50

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
        return self.HP, self.Hunger, self.Happiness, self.Thirst, self.Age, self.Intellegence, self.Hygiene, self.weight, self.Strength,self.LastOnline, self.Action, self.name, self.Temp
    def feed(self,amt):
        self.Hunger += amt
        if self.Hunger >=100: 
            self.weight = self.weight+((self.Hunger-100)/5)
        return self.Hunger,self.weight
    def drink(self,amt):
        self.Thirst += amt
        if self.Thirst >= 100:
            self.Thirst = 100
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
            if self.Hygiene < 100:
                self.Hygiene += amt
            if self.Hygiene >= 100:
                self.Hygiene = 100

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

        if self.Hunger <= 0:
            if self.weight <= 20:
                self.HP -= (1/frameRate)
            else:
                self.weight -= (0.5/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (1/frameRate)

    def checkThirst(self, frameRate):
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0 and self.Hunger >0:
            self.Thirst -= (0.5/frameRate)
    def checkHygiene(self, frameRate):

        if self.Hygiene <= 5:
            self.HP -= (0.5/frameRate)
        else:
            self.Hygiene -= (0.2/frameRate)
    def checkAge(self,frameRate, multiplyer = 1):

        growRate = 0.1*multiplyer
        self.Age += (growRate/frameRate)
    def retrunAge(self):

        return self.Age
    def checkEvolve(self, evolution):

        if self.Age < 5:
            return ('egg', evolution)

        elif (self.Age >= 5) and (self.Age < 10):
            if evolution == 0:
                check_evo = 1
            
            else:
                check_evo = evolution

            return ('toddler', check_evo)
        
        elif (self.Age >= 10) and (self.Age < 50):
            
            if evolution == 1:
                check_evo = 2
            else:
                check_evo = evolution
            
            if evolution != check_evo:
                if (self.Intellegence >= 80) and not(self.Strength > 60):
                    return ('intelligent',check_evo)
                    
                elif (self.Strength >= 80) and not(self.Intellegence > 60):
                    return ('strong',check_evo)
                    
                else:
                    return ('balanced',check_evo)
                
            else:
                return ('same',evolution)
        
        #keep adding onto this

    def checkHP(self):
        print(':)')

class egg(Tamo):

    def __init__(self, state = 0):
        pygame.sprite.Sprite.__init__(self)
        Tamo.__init__(self)
        self.HP = 25
        self.Strength = 10
        self.Temp = 50
        self.state = state
        self.image = pygame.image.load('tamoImages\eggStage1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [310,310]
    
    def updateState(self):
        if self.Age < 2:
            self.image = pygame.image.load('tamoImages\eggStage1.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif self.Age < 3:
            self.image = pygame.image.load('tamoImages\eggStage2.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif self.Age < 4:
            self.image = pygame.image.load('tamoImages\eggStage3.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]
        elif self.Age < 5:
            self.image = pygame.image.load('tamoImages\eggStage4.png')
            self.rect = self.image.get_rect()
            self.rect.center = [310,310]

    def feed(self,amt):

        return 'too young'
    
    def excercise(self):
        
        return 'too young'
    
    def read(self):
        
        return 'too young'
    
    def heat(self):

        self.Temp += 20

    def checkHunger(self, frameRate):

        return 'too young'

    def checkThirst(self, frameRate):
        
        return 'too young'
    
    def checkTemp(self, frameRate):

        if self.Temp <= 0 or self.Temp >= 100:
            self.HP -= (2/frameRate)
            self.Temp -= (1/frameRate)
        
        else:
            self.Temp -= (1/frameRate)

    def checkHP(self):
        
        if self.HP > 25:
            self.HP = 25
  
class toddler(Tamo):

    def __init__(self, age, state = 0):
        pygame.sprite.Sprite.__init__(self)
        Tamo.__init__(self)
        self.HP = 50
        self.Strength = 25
        self.Age = age
        self.image = pygame.image.load('tamoImages\gotchiToddler.png')
        self.rect = self.image.get_rect()
        self.x_cord = 340
        self.y_cord = 360
        self.state = state

    def updateState(self):
        if self.state == 0:
            self.image = pygame.image.load('tamoImages\gotchiToddler.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

        elif self.state == 1:
            self.image = pygame.image.load('tamoImages\gtPlayAnim1.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

        elif self.state == 2:
            self.image = pygame.image.load('tamoImages\gtPlayAnim2.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 3:
            self.image = pygame.image.load('tamoImages\gtPlayAnim3.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 4:
            self.image = pygame.image.load('tamoImages\gtPlayAnim4.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 5:
            self.image = pygame.image.load('tamoImages\gtPlayAnim5.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 6:
            self.image = pygame.image.load('tamoImages\gtPlayAnim6.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

    def setState(self, amt):

        self.state = amt

    def checkHunger(self, frameRate):

        if self.Hunger <= 0:
            if self.weight <= 20:
                self.HP -= (2/frameRate)
            else:
                self.weight -= (0.5/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (2/frameRate)
            
    def checkThirst(self, frameRate):
        #less health and uses food and water quicker
        
        if self.Thirst == 0:
            self.HP -= (1/frameRate)
        
        elif self.Thirst > 0:
            self.Thirst -= (1/frameRate)

    def play(self, time):
        self.Happiness += 20
        self.Hygiene -= 10

        self.Hunger -= 15
    
    def checkHP(self):
        
        if self.HP > 50:
            self.HP = 50

class balanced1(Tamo):
    
    def __init__(self,a,i,w,s):
        pygame.sprite.Sprite.__init__(self)
        Tamo.__init__(self)
        self.Age = a
        self.Intellegence = i
        self.Weight = w
        self.Strength = s

        self.image = pygame.image.load('tamoImages\gotchiBalance.png')
        self.rect = self.image.get_rect()
        self.rect.center = [340,360]

class strong1(Tamo):
    #uses hunger and thirst quicker but makes strength quicker
    
    def __init__(self,a,i = 50,w = 50,s = 100,state = 0):
        pygame.sprite.Sprite.__init__(self)
        Tamo.__init__(self)
        self.Age = a
        self.Intellegence = i
        self.Weight = w
        self.Strength = s
        self.state = state
        self.image = pygame.image.load('tamoImages\gotchiStrong.png')
        self.rect = self.image.get_rect()
        self.x_cord = 340
        self.y_cord = 360

    def updateState(self):
        if self.state == 0:
            self.image = pygame.image.load('tamoImages\gotchiStrong.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

        elif self.state == 1:
            self.image = pygame.image.load('tamoImages\gsPlayAnim1.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

        elif self.state == 2:
            self.image = pygame.image.load('tamoImages\gsPlayAnim2.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 3:
            self.image = pygame.image.load('tamoImages\gsPlayAnim3.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 4:
            self.image = pygame.image.load('tamoImages\gsPlayAnim4.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 5:
            self.image = pygame.image.load('tamoImages\gsPlayAnim5.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 6:
            self.image = pygame.image.load('tamoImages\gsPlayAnim6.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 7:
            self.image = pygame.image.load('tamoImages\gsPlayAnim7.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]
        
        elif self.state == 8:
            self.image = pygame.image.load('tamoImages\gsPlayAnim8.png')
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_cord,self.y_cord]

    def checkHunger(self, frameRate):

        if self.Hunger <= 0:
            if self.weight <= 20:
                self.HP -= (1/frameRate)
            else:
                self.weight -= (0.5/frameRate)
        
        elif self.Hunger > 0:
            self.Hunger -= (2/frameRate)

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
        pygame.sprite.Sprite.__init__(self)
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