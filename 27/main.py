
import math

#for n in range(10):
#    print(n**2 + 72*n -61)

primes = []

with open('primes.txt') as file:
    for line in file:
        num = line.split(",")
        for n in num:
            if not n == "\n":
                primes.append(int(n))

print('len primes')
print(len(primes))

consecutive = 0
save_a = 0
save_b = 0

for a in range(-1000, 1000):

    for b in range(-1000, 1001):

        n = -1
        is_prime = True
        while(is_prime):
            n = n + 1
            value = math.pow(n,2) + a*n + b
            is_prime = value in primes



        if n > consecutive:
            consecutive = n
            save_a = a
            save_b = b
            print(consecutive)

print(consecutive, save_a, save_b)