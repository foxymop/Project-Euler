
# Read the question wrong.
# Redo algorithm.

import math

primes = []

with open('primes.txt') as file:
    for line in file:
        strings = line.split(", ")
        primes = list(map(int, strings))

#print(len(primes))

a = len(primes)

for i in range(a):
    if primes[i] > 369:
        b = i
        break

for i in range(b):
    if primes[i] > 85:
        c = i
        break

#print(a, b, c)
#print(primes[a-1], primes[b-1], primes[c-1])

lim = 50000000
#lim = 50
pyramids = []

for i in range(a):
    for j in range (b):
        sum = math.pow(primes[i],2) + math.pow(primes[j],3)
        if sum > lim:
            break
        for k in range(c):
            sum = math.pow(primes[i],2) + math.pow(primes[j],3) + math.pow(primes[k], 4)
            if sum < lim:
                pyramids.append(sum)
            else:
                break

print(max(pyramids))
unique_pyramids = set(pyramids)

print(len(unique_pyramids))

