import math

primes = []
with open('primes.txt') as file:
    for line in file:
        num = line.split(",")
        for n in num:
            if not n == "\n":
                primes.append(int(n))

squares = []
for i in range(50):
    squares.append(int(math.pow(i, 2)))


def Goldbach_Err(n):
    if n not in primes and not n % 2 == 0:
        fits = False
        for s in squares:
            if 2 * s > n:
                break
            for p in primes:
                if n == p + 2 * s:
                    fits = True
                if p + 2 * s > n:
                    break
        return fits

    else:
        return True

number = 1
for n in range(2, 100000):
    if not Goldbach_Err(n):
        number = n
        break


print(number)