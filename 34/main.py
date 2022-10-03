
import math

for i in range(1, 50000):

    number = i
    digits = []
    while (number > 0):
        #print( number % 10)
        digits.append(number % 10)
        number = number // 10

    #print(digits)

    sum = 0
    for j in digits:
        sum = sum + math.factorial(j)

    #print(sum)

    if sum == i:
        print(sum)

print("Done!")