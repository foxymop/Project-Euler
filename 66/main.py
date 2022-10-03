
import math

squares = []
for i in range(1, 100000):
    squares.append(math.pow(i, 2))


save_x = 0
for D in range(1001):
    if D in squares:
        a = 0
    else:
        minimal_found = False
        for idx, x in enumerate(squares):
            for y in squares[0:idx]:
                if x - D * y == 1:
                    print(x, D, y)
                    minimal_found = True
                    if x > save_x:
                        save_x = x
                    break
            if minimal_found:
                break




print('Highest x: ', save_x)