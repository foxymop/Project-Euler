
import math


my_list = []
for a in range(2,101):
    for b in range(2,101):
        if math.pow(a,b) not in my_list:
            my_list.append(math.pow(a,b))


print(len(my_list))

