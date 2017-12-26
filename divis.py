import random
import sys
import os
import math

def divis():
    clicker = 0
    for i in range(1, 24000000):
        i, i + 1
        for a in range (1, 21):
            x = i%a
            #print (clicker)
            if x == 0 and clicker < a:
                clicker = a
                #print (i)
                if clicker == 20:
                    print (i)





divis()
