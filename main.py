import pygame
import math
import time
import os
import pickle
from datetime import datetime 
from Saver import *
OpenedAt = datetime.now()
f = open('Save.txt','r+')
Names = ['Tom','Altin']
f.write(Names)
OrigionalNames = f.readline()
