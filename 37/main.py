

primes = []

with open('primes.txt') as file:
    for line in file:
        num = line.split(",")
        for n in num:
            if not n == "\n":
                primes.append(int(n))

sum = 0
for prime in primes:

    trunc = str(prime)

    truncs_prime = True
    for i in range(1, len(trunc)):
        left_trunc = trunc[i:]
        right_trunc = trunc[:i]
        #print(right_trunc)
        #print(left_trunc)
        if int(left_trunc) not in primes or int(right_trunc) not in primes:
            truncs_prime = False
            break

    if truncs_prime and int(trunc) > 7:
        print(trunc, truncs_prime)
        sum = sum + int(trunc)

print("Done!")
print(sum)
