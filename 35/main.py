
primes = []

with open('primes.txt') as file:
    for line in file:
        num = line.split(",")
        for n in num:
            if not n == "\n":
                primes.append(int(n))

def is_circular(i):

    number = i
    digits = []
    while (number > 0):
        digits.insert(0, number % 10)
        number = number // 10

    circular = True
    for j in range(len(digits)):
        digits.append(digits.pop(0))
        num = 0
        for k in range(len(digits)):
            num = num + 10**k * digits[len(digits)-k-1]

        if num not in primes:
            circular = False
            break

    return circular

print(is_circular(97))

count = 0
for i in primes:
    if is_circular(i):
        count = count + 1

print(count)


