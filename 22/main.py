


with open('names.txt') as file:
    for line in file:
        strings = line.split(",")


        for i in range(len(strings)):
            strings[i] = strings[i].replace('"', '')

        strings.sort()


def sum_name(name):

    sum = 0
    for i in range(len(name)):
        sum = sum + ord(name[i]) - 64

    return sum


print(strings[937])
eval = (937 + 1) * sum_name(strings[937])
print(eval)


sum = 0
for i in range(len(strings)):
    sum = sum + (i + 1) * sum_name(strings[i])

print(sum)




#for i in range(len(strings)):
    #call sum_name(strings[i])