
import math

def high_card(P1H, P2H):

    H1 = []
    H2 = []

    for x in P1H:
        H1.append(x%13)
    for x in P2H:
        H2.append(x%13)

    HC1 = max(H1)
    HC2 = max(H2)

    if HC1 > HC2:
        return 1
    elif HC2 > HC1:
        return 2
    else:
        H1 = set(H1)
        H1.remove(HC1)
        H2 = set(H2)
        H2.remove(HC2)
        return high_card(H1, H2)


def find_winner(Rank, P1Hand, P2Hand):

    if Rank == 9: # High Card

        return high_card(P1Hand, P2Hand)

    if Rank == 8: # One Pair

        H1 = []
        H2 = []
        for x in P1Hand:
            H1.append(x%13)
        for x in P2Hand:
            H2.append(x%13)

        H1Pair = 0
        H2Pair = 0

        for i in range(13):
            if H1.count(i) == 2:
                H1Pair = i
            if H2.count(i) == 2:
                H2Pair = i

        if H1Pair > H2Pair:
            return 1
        elif H2Pair > H1Pair:
            return 2
        else:

            HC1 = set(H1)
            HC1.remove(H1Pair)
            HC2 = set(H2)
            HC2.remove(H2Pair)
            return high_card(HC1, HC2)

    if Rank == 7: # Two Pair
        H1 = []
        H2 = []
        for x in P1Hand:
            H1.append(x % 13)
        for x in P2Hand:
            H2.append(x % 13)

        H1Pair = [0,0]
        H2Pair = [0,0]
        j = 0
        k = 0
        for i in range(13):
            if H1.count(i) == 2:
                H1Pair[j] = i
                j = j+1
            if H2.count(i) == 2:
                H2Pair[k] = i
                k = k+1
        if H1Pair[0] > H2Pair[0]:
            return 1
        elif H2Pair[0] > H1Pair[0]:
            return 2
        else:
            if H1Pair[1] > H2Pair[1]:
                return 1
            elif H2Pair[1] > H2Pair[1]:
                return 2
            else:
                HC1 = set(H1)
                HC1.remove(H1Pair[0])
                HC1.remove(H1Pair[1])
                HC2 = set(H2)
                HC2.remove(H2Pair[0])
                HC2.remove(H2Pair[1])
                return high_card(HC1, HC2)

    if Rank == 6: # Trips

        H1 = []
        H2 = []
        for x in P1Hand:
            H1.append(x%13)
        for x in P2Hand:
            H2.append(x%13)

        H1Trip = 0
        H2Trip = 0

        for i in range(13):
            if H1.count(i) == 3:
                H1Trip = i
            if H2.count(i) == 3:
                H2Trip = i

        if H1Trip > H2Trip:
            return 1
        elif H2Trip > H1Trip:
            return 2
        else:
            #actually don't need this code because it's impossible to have two hands with equal trips
            HC1 = set(H1)
            HC1.remove(H1Trip)
            HC2 = set(H2)
            HC2.remove(H2Trip)
            return high_card(HC1, HC2)

    if Rank == 5: # Straight
        return high_card(P1Hand, P2Hand)

    if Rank == 4: # Flush

        H1 = list(P1Hand)
        H2 = list(P2Hand)

        Suit1 = math.floor(H1[0]/13)
        Suit2 = math.floor(H2[0]/13)

        if Suit1 > Suit2:
            return 1
        elif Suit2 > Suit1:
            return 2
        else:
            return high_card(P1Hand, P2Hand)

    if Rank == 3: # Full House

        H1 = []
        H2 = []
        for x in P1Hand:
            H1.append(x % 13)
        for x in P2Hand:
            H2.append(x % 13)

        H1Trip = 0
        H2Trip = 0

        for i in range(13):
            if H1.count(i) == 3:
                H1Trip = i
            if H2.count(i) == 3:
                H2Trip = i

        if H1Trip > H2Trip:
            return 1
        else:
            return 2

    if Rank == 2: # Quads

        H1 = []
        H2 = []
        for x in P1Hand:
            H1.append(x%13)
        for x in P2Hand:
            H2.append(x%13)


        H1Q = 0
        H2Q = 0

        for i in range(13):
            if H1.count(i) == 4:
                H1Q = i
            if H2.count(i) == 4:
                H2Q = i

        if H1Q > H2Q:
            return 1
        else:
            return 2

    if Rank == 1: # Straight Flush

        H1 = list(P1Hand)
        H2 = list(P2Hand)

        Suit1 = math.floor(H1[0] / 13)
        Suit2 = math.floor(H2[0] / 13)

        if Suit1 > Suit2:
            return 1
        elif Suit2 > Suit1:
            return 2
        else:
            return high_card(P1Hand, P2Hand)

    if Rank == 0: # Royal Flush

        H1 = list(P1Hand)
        H2 = list(P2Hand)

        Suit1 = math.floor(H1[0] / 13)
        Suit2 = math.floor(H2[0] / 13)

        if Suit1 > Suit2:
            return 1
        else:
            return 2

    return 0
