
import math
import numpy as np
from matplotlib import pyplot as plt






def combs(a, b):
    combos = 0

    for i in range(a):
        for j in range(b):
            combos = combos + (a-i)*(b-j)

    return combos



def c(num):
    return combs(num, num)

for x in range(100):
    for y in range(100):
        lim = 2000000
        if (abs(lim-combs(x,y)) < 200):
            print(combs(x,y))
            print(x,y)


print(36*77)