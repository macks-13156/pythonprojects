import random
import sys
import os
import math

#global max = 0

def palfind():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            a = i*j
            strn = str(a)
            reverse = strn[::-1]
            ispal = strn == reverse
            if ispal:
                if max < a:
                    max = a
                    print (a)


palfind()
