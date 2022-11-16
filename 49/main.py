

import sympy

digits = [0,1,2,3,4,5,6,7,8,9]
n = [0,0,0,0]

#for l1 in range(10):
#    n[0] = digits[l1]
#    digits1 = digits.copy()
#    digits1.pop(l1)
#    for l2 in range(9):
#        n[1] = digits1[l2]
#        digits2 = digits1.copy()
#        digits2.pop(l2)
#        for l3 in range(8):
#            n[2] = digits2[l3]
#            digits3 = digits2.copy()
#            digits3.pop(l3)
#            for l4 in range(7):
#                n[3] = digits3[l4]

for n[0] in range(10):
    for n[1] in range(10):
        for n[2] in range(10):
            for n[3] in range(10):

                list_of_permutations = []

                for i in range(4):
                    m = n.copy()
                    perm = str(m[i])
                    m.pop(i)
                    for j in range(3):
                        l = m.copy()
                        perm1 = perm + str(l[j])
                        l.pop(j)
                        for k in range(2):
                            h = l.copy()
                            perm2 = perm1 + str(h[k])
                            h.pop(k)
                            perm2 = perm2 + str(h[0])
                            list_of_permutations.append(int(perm2))

                #print(list_of_permutations)


                list0 = list_of_permutations.copy()
                for elem1 in list0:
                    for elem2 in list0:
                        for elem3 in list0:
                            if not elem1 == elem2 and not elem2 == elem3 and not elem1 == elem3:
                                if elem2 > elem1 and elem3 > elem2:
                                    if elem2-elem1 == elem3-elem2:
                                        if sympy.isprime(elem1) and sympy.isprime(elem2) and sympy.isprime(elem3):
                                            if not elem1 == 163 and not elem1 == 379:
                                                print([elem1, elem2, elem3])
                                                list0.remove(elem1)
                                                list0.remove(elem2)
                                                list0.remove(elem3)



print('Done!')