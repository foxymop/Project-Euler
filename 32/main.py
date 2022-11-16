


products = []

for i in range(1, 100):
    digits_used = []
    numbers_i = str(i)
    for a in numbers_i:
        digits_used.append(a)

    for j in range(100,10000):
        digits_use = digits_used[:]

        numbers_j = str(j)
        for a in numbers_j:
            digits_use.append(a)

        product = i*j
        numbers_p = str(product)
        for a in numbers_p:
            digits_use.append(a)

        #print(digits_use)

        nine_digits = len(digits_use) == 9
        all_digits = True
        for k in range(1,10):
            if str(k) not in digits_use:
                all_digits = False

        if nine_digits and all_digits:
            products.append(product)



print(products)

print(6952+7852+5796+5346+4396+7254+7632)