
Triangular = []
Pentagonal = []
Hexagonal = []

for n in range(1,100000):

    Triangular.append(n*(n+1)/2)
    Pentagonal.append(n*(3*n-1)/2)
    Hexagonal.append(n*(2*n-1))


for i in range(len(Hexagonal)):
    num = Hexagonal[i]
    if num in Pentagonal and num in Triangular:
        print(num)


print("Done!")