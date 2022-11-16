
import math

total = 0
for n in range(1,1001):
    partial_sum = 1

    for i in range(n):
        partial_sum = (partial_sum * n) % math.pow(10,10)

    total = total + partial_sum

print(total)