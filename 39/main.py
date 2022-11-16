import math


save_sols = []

for p in range(10,1001):

    solutions = 0

    for x in range( 1 , int(p / (math.sqrt(2) + 2)) ):
        for y in range( x+1 , math.floor(math.sqrt(math.pow(p,2)-math.pow(x,2))) ):
            if math.pow(x,2) + math.pow(y,2) == math.pow(p-x-y, 2):
                solutions = solutions + 1

    save_sols.append(solutions)
    if solutions == 8:
        print(p)


print(max(save_sols))