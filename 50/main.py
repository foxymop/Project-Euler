
import sympy

primes = []
with open('primes_under_a_million.txt') as file:
    for line in file:
        strings = line.split(",")
        strings.pop()
        p = list(map(int, strings))
        primes.extend(p)


sum1 = 0
for i in range(6):
    sum1 = sum1 + primes[i]
print(sum1)
print(sympy.isprime(sum1))

sum2 = 0
for i in range(3, 21+3):
    sum2 = sum2 + primes[i]
print(sum2)
print(sympy.isprime(sum2))

partial_sums = []
sum3 = 0
index = 0
while(sum3<1000000):
    sum3 = sum3 + primes[index]
    partial_sums.append(sum3)
    index = index + 1
partial_sums.pop()

print(partial_sums[5])

print(len(partial_sums))

highest = 0
for i in range(len(partial_sums)):
    for j in range(len(partial_sums)):
        num = partial_sums[j]-partial_sums[i]
        if sympy.isprime(num) and num > highest:
            highest = num

print(highest)




