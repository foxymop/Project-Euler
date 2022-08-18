
import math

def factorize(n):    # (cf. https://stackoverflow.com/a/15703327/849891)
    l = 1
    u = math.ceil(n/2)

    for i in range(u):
        if n % (i+1) == 0:
            yield i+1

def sum_factors(n):

    sum = 0
    mygenerator = factorize(n)
    for i in mygenerator:
        sum = sum + i

    return sum


print(sum_factors(220))
print(sum_factors(284))

num = 0
sum = 0
for i in range(10000):
    s_f = sum_factors(i)
    if sum_factors(s_f) == i and i > s_f:
        print(s_f, i)
        num = num + 1
        sum = sum + s_f + i

print(sum)
