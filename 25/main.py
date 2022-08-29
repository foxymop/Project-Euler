
import math

def fibonacci(n):

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print('1')
print('1')

n = 1
while(True):
    if fibonacci(n) > math.pow(10,10):
        print(fibonacci(n))
        break
    n = n + 1

print('Done!')