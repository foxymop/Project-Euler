
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

def is_perfect(n):

    return n == sum_factors(n)

def is_abundant(n):

    return n < sum_factors(n)

def is_deficient(n):

    return n > sum_factors(n)

max_check = 28123
check = 2000
abundants = []
for i in range(math.ceil(max_check)):
    if is_abundant(i):
        abundants.append(i)


num_abundants = len(abundants)

print(len(abundants))
print(abundants)

def is_sum_abundants(n):
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            if n == abundants[i] + abundants[j]:
                return True

    return False

def next_biggest(array_a, int_i):
    nextbig = [m for m in array_a if m > int_i]
    if nextbig:
        return min(nextbig)
    else:
        return num_abundants

def next_smallest(array_a, int_i):
    nextsmall = [m for m in array_a if m < int_i]
    if nextsmall:
        return max(nextsmall)
    else:
        return 0

def is_sum_abundants_2(n, indices):
    up_lim = 6965
    bot_lim = 0
    if n < 24:
        return False
    elif n > 28123:
        return True
    else:

        print(indices[-1], abundants[int(indices[-1])])

        if n == (abundants[int(indices[-1])] + abundants[int(indices[-2])]): # if we have a match
            return True
        if indices[-1] and indices[-2] == bot_lim: # if we have reached the bottom of the list
            return False
        elif indices[-1] and indices[-2] == up_lim: # if we have reached the top of the list
            return False
        else:
            if n < (abundants[int(indices[-1])] + abundants[int(indices[-2])]): # if we have to go down
                new_index = math.floor(next_smallest(indices, int(indices[-1])) + indices[-1] / 2) # may need to try ceil
                if indices.count(new_index) < 2:
                    indices.append(new_index)
                    return is_sum_abundants_2(n, indices)
                else:
                    return False
            else: # if we have to go up
                new_index = math.ceil(next_biggest(indices, int(indices[-1])) + indices[-1] / 2)
                if indices.count(new_index) < 2:
                    indices.append(new_index)
                    return is_sum_abundants_2(n, indices)
                else:
                    return False

def is_sum_abundants_3(a):
    for i in range(0, len(abundants)):
        for j in range(i, len(abundants)):
            if a == abundants[i] + abundants[j]:
                return True
    return False





#midpoint = math.ceil(num_abundants/2)

#count = 0
#indices = [midpoint, midpoint]
#for i in range(11, 37):
#for i in range(32, 33):
#    print(i, is_sum_abundants_2(i, indices))


sum = 0
for i in range (0, max_check):
    #print(i, is_sum_abundants_3(i))
    if not is_sum_abundants_3(i):
        sum = sum + i

print(sum)