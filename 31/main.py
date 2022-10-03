
import math

coins = [.01, .02, .05, .1, .2, .5, 1]

# 1 way to make 1 cent
# 3 ways to make 2 cents
# 4 ways to make 5 cents
# 11 ways to make 10 cents

x1 = 11

# 20 cents
#x2 = math.pow(x1, 2) + 1 - (x1-1)*(x1-2)/2
#x2 = 1
#for i in range(x1+1):
#    x2 = x2 + i
#print(x2)

x2 = (x1+1)*x1/2 + 1
print(x2)

# 50 cents
#x3 = math.pow(x2, 2)*x1 + 1 - (x2-1)*(x2-2)/2
#x3 = 1
#for i in range(x2+1):
#    x3 = x3 + i

# 40 cents
x3 = (x2+1)*x2/2
#print(x3)

# 50 cents
x4 = (x2+1)*x2/2 + 1
print(x4)

dec = 0
sum = 1
for i in range(11):
    sum = sum + (x2-dec+1)*(x2-dec)/2
    dec = dec + 11 - i

print(sum)
x4 = sum

dec = 0
sum = 67
for i in range(11):
    j = 11 - i
    dec = dec + j
    sum = sum + (67-dec)*j


print(sum)
x4=sum

# 1 dollar
#x4 = math.pow(x3, 2) + 1 - (x3-1)*(x3-2)/2
#x4 = 1
#for i in range(x3+1):
#    x4 = x4 + i

x5 = (x4+1)*x4/2 + 1
print(x5)

# 2 dollars
#x5 = math.pow(x4, 2) + 1 - (x4-1)*(x4-2)/2
#x5 = 1
#for i in range(x4+1):
#    x5 = x5 + i

x6 = (x5+1)*x5/2 + 1

print('%.2f' % x6)