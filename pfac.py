import random
import sys
import os
import math

container = [2, 3, 5]

def sqr(n):
    x = n**(0.5)
    print (x)

sqr(4)




def pfac(n):
    if n == 1:
        print ("1 not Prime")
        return
    n**(0.5)
    math.ceil(n)
    for i in container:
        if n%(container[i]) == 0:
            container.append(n)
            print (container)
        else:
            print (n)


pfac(9)
