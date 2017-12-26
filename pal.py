import random
import sys
import os
import math

container = []

def numgen():
    for i in range(100, 1000):
        i, i + 1
        a = i*i
        container.append(a)
        #print (a)
        #container[::-1]

def palcheck(n):
    for i in n:
        strn = str(i)
        reverse = strn[::-1]
        ispal = strn == reverse
        print (ispal)
        if ispal:
            print ("{}*{}={}".format(strn,i,i))



numgen()
print (palcheck(container[::-1]))
