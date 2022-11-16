


pentagonal = []

for n in range(1,10000):
    pentagonal.append( int(n*(3*n-1)/2) )

print(pentagonal)


min_D = 1000000
for j in range(len(pentagonal)):
    for k in range(j, len(pentagonal)):
        jth = pentagonal[j]
        kth = pentagonal[k]
        if jth + kth in pentagonal and kth-jth in pentagonal:
            D = kth - jth
            print(D)
            if D < min_D:
                min_D = D

print(min_D)