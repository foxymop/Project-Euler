
from sympy.ntheory import factorint

print(factorint(20))

dict = factorint(20)


print(len(dict.keys()))

consec = 0
for n in range(200000):
    prime_fact = factorint(n)
    if len(prime_fact) > 3:
        consec = consec + 1
    else:
        consec = 0

    if consec == 4:
        print(n-3)

