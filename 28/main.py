

print(1+3+5+7+9+13+17+21+25+31+37+43+49)

#8,16,24

sum = 0
x = 1
for i in range(1, 502):
    if i == 1:
        sum = sum + 1
    else:
        for j in range(1,5):
            x = x + 2*(i-1)
            sum = sum + x


print(sum)