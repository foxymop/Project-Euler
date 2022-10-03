
import math

x = math.pow(9,5)

y = math.pow(1,4) + math.pow(6,4) + math.pow(3,4) + math.pow(4,4)


answer = 0
for n in range(1000, 1000000):

    number = n
    sum = 0
    while(number>0):
        digit = number % 10
        number = number // 10
        sum = sum + math.pow(digit, 5)


    if n == sum:
        print(n)
        answer = answer + n

print(answer)