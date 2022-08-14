
# This is the main file for the program that runs the solution to ProjectEuler #54.
#
# It reads the input file line by line, determines the winner of the hand given the
# cards both players are dealt, and then increments a counter for the winner.
# The output of the program is simply the win counter for player 1.


#TODO: write a tiebreaker file... rank is determined for each hand but not which number
#TODO: for pairs, what the high card is, which suit for flush etc...


import hand_indices
import hand_rank

with open('oneline.txt') as file:
    # For every line in the input file, split the data into the two players' hands:
    for line in file:

        #print(line.split())
        cards = line.split()

        P1Hand = []
        P2Hand = []
        for i in range(5):
            P1Hand.append(cards[i])
            P2Hand.append(cards[i+5])

        #print(P1Hand)
        print(P2Hand)

        # Convert the hands from text to numbers, and from a list to a set:
        P1Hand_Num = hand_indices.hand_indices(P1Hand)
        P2Hand_Num = hand_indices.hand_indices(P2Hand)

        #print(P1Hand_Num)
        print(P2Hand_Num)

        P1Rank = hand_rank.hand_rank(P1Hand_Num)
        P2Rank = hand_rank.hand_rank(P2Hand_Num)

        #print(P1Rank)
        print(P2Rank)