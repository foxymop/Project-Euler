
import hand_criteria as hc

# Ranks:
# 0 - Royal Flush
# 1 - Straight Flush
# 2 - Four of a Kind
# 3 - Full House
# 4 - Flush
# 5 - Straight
# 6 - Three of a Kind
# 7 - Two Pair
# 8 - One Pair
# 9 - High Card

def hand_rank(s: set) -> int:

    if hc.royal_flush_criterion(s):
        return 0
    elif hc.straight_flush_criterion(s):
        return 1
    elif hc.quads_criterion(s):
        return 2
    elif hc.full_house_criterion(s):
        return 3
    elif hc.flush_criterion(s):
        return 4
    elif hc.straight_criterion(s):
        return 5
    elif hc.trips_criterion(s):
        return 6
    elif hc.two_pair_criterion(s):
        return 7
    elif hc.one_pair_criterion(s):
        return 8
    else:
        return 9