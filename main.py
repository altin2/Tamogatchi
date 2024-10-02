import pygame
import math
import time
import os
f = open('SaveFile.txt','w')
f.write('Hello World')
print(f.mode)
f.close()
print("Hello World")
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




    

