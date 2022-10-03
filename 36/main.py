

sum = 0
for i in range(1000000):

    dec_pal = False
    bin_pal = False

    number = i
    reverse = 0
    while(number>0):
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10

    if i == reverse:
        dec_pal = True
        #print('palindrome!', i)


    number_bin = int("{0:b}".format(i))
    binary = number_bin
    reverse_bin = 0
    while(number_bin>0):
        remainder = number_bin % 10
        reverse_bin = (reverse_bin * 10) + remainder
        number_bin = number_bin // 10


    if binary == reverse_bin:
        bin_pal = True
        #print('palindrome!', bin(i))


    if dec_pal and bin_pal:
        print(i, bin(i), ": Palindrome in base 10 and 2.")
        sum = sum + i

print(sum)