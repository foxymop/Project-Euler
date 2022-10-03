
import math

coded_triangle = []
for i in range(1, 2000):
    coded_triangle.append(int(i*(i+1)/2))
    #print(i*(i+1)/2)

#print(coded_triangle)

with open('words.txt') as file:
    for line in file:
        strings = line.split("\",\"")

#print(strings)

total = 0
for word in strings:
    sum = 0
    for letter in word:
        val = ord(letter) - 64
        #print(val)
        sum = sum + val
    if sum in coded_triangle:
        total = total + 1

print(total)