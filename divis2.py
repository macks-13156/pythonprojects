import random
import sys
import os
import math

def divis():
    clicker = 0
    for i in range(1, 3000):
        i, i + 1
        for a in range (1, 11):
            x = i%a
            #print (clicker)
            #print (i)
            if x == 0 and clicker <= a:
                clicker = a
                print (clicker)
                if clicker == 10:
                    print (i)







divis()
