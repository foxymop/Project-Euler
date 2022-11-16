


three = []
for n in range(6, 59):
    num = 17*n
    digits = str(num)


    distinct = True
    for digit in digits:
        if digits.count(digit) > 1:
            distinct = False
    if distinct:
        three.append(digits)

#print(three)
print(len(three))


four = []
for n in range(len(three)):
    for i in range(10):
        if str(i) not in three[n]:
            if int(str(i) + three[n][:-1]) % 13 == 0:
                four.append(str(i) + three[n])

print(len(four))

five = []
for n in range(len(four)):
    for i in range(10):
        if str(i) not in four[n]:
            if int(str(i) + four[n][:-2]) % 11 == 0:
                five.append(str(i) + four[n])

print(len(five))

six = []
for n in range(len(five)):
    for i in range(10):
        if str(i) not in five[n]:
            if int(str(i) + five[n][:-3]) % 7 == 0:
                six.append(str(i) + five[n])

print(len(six))

seven = []
for n in range(len(six)):
    for i in range(10):
        if str(i) not in six[n]:
            if int(str(i) + six[n][:-4]) % 5 == 0:
                seven.append(str(i) + six[n])

print(len(seven))

eight = []
for n in range(len(seven)):
    for i in range(10):
        if str(i) not in seven[n]:
            if int(str(i) + seven[n][:-5]) % 3 == 0:
                eight.append(str(i) + seven[n])

print(len(eight))

nine = []
for n in range(len(eight)):
    for i in range(10):
        if str(i) not in eight[n]:
            if int(str(i) + eight[n][:-6]) % 2 == 0:
                nine.append(str(i) + eight[n])

print(len(nine))

ten = []

for n in range(len(nine)):
    for i in range(10):
        if str(i) not in nine[n]:
            ten.append(str(i) + nine[n])

#print(ten)

sum = 0
for n in range(len(ten)):
    sum = sum + int(ten[n])

print(sum)