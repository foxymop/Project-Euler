
#TODO: These functions give a pass/fail if the criterion is met. It might be worthwhile to find the best
#TODO: subset of cards among the post-turn cards. IE: Royal Flush? yes-spades Full House? yes-7's over 2's


def royal_flush_criterion(s: set) -> bool:
    royal_flush_spades = {8, 9, 10, 11, 12}
    royal_flush_hearts = {21, 22, 23, 24, 25}
    royal_flush_diamonds = {34, 35, 36, 37, 38}
    royal_flush_clubs = {47, 48, 49, 50, 51}

    r = royal_flush_spades.issubset(s) or royal_flush_hearts.issubset(s) or royal_flush_diamonds.issubset(s) or royal_flush_clubs.issubset(s)

    return r

def straight_flush_criterion(s: set) -> bool:

    for i in range(4):
        x = i*13
        for j in range(8):
            if j==0:
                hand = set(range(x, x+4))
                hand.add(x+12)
                #print(hand)
                if hand.issubset(s):
                    return True
            else:
                hand = set(range(x+j, x+j+5))
                #if j==7:
                #    print(hand)
                if hand.issubset(s):
                    return True

    return False

def quads_criterion(s: set) -> bool:

    for i in range(13):
        hand = {i, i+13, i+26, i+39}
        if hand.issubset(s):
            return True

    return False

def full_house_criterion(s: set) -> bool:

    for i in range(13):
        for j in range(4):
            trips = {i, i+13, i+26, i+39}
            missing = i+j*13
            trips.remove(missing)
            #print(trips)

            for k in range(13):
                if k != i:
                    for l in range(4):
                        for m in range(4):
                            if m != l:
                                pair = {k, k + 13, k + 26, k + 39}
                                pair.discard(k+l*13)
                                pair.discard(k+m*13)
                                #print(pair)

                                hand = set()
                                hand.update(trips)
                                hand.update(pair)

                                if hand.issubset(s):
                                    return True

    return False

def flush_criterion(s: set) -> bool:

    for i in range(4):
        suit = set()
        for j in range(13):
            suit.add(j)
        if s.issubset(suit):
            return True

    return False

def straight_criterion(s: set) -> bool:

    suitless = set()
    for x in s:
        suitless.add(x%13)

    for x in range(9):
        straight = {x, x+1, x+2, x+3, x+4}
        if straight.issubset(suitless):
            return True

    return False

def trips_criterion(s: set) -> bool:

    suitless = []
    for x in s:
        suitless.append(x%13)

    for i in range(13):
        if suitless.count(i) == 3:
            return True

    return False

def two_pair_criterion(s: set) -> bool:

    suitless = []
    for x in s:
        suitless.append(x%13)

    pairs = 0
    for i in range(13):
        if suitless.count(i) == 2:
            pairs = pairs + 1

    if pairs > 1:
        return True

    return False

def one_pair_criterion(s: set) -> bool:

    suitless = []
    for x in s:
        suitless.append(x % 13)

    for i in range(13):
        if suitless.count(i) == 2:
            return True

    return False


