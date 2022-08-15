
# This is the main file for the program that runs the solution to ProjectEuler #54.
#
# It reads the input file line by line, determines the winner of the hand given the
# cards both players are dealt, and then increments a counter for the winner.
# The output of the program is simply the win counter for player 1.


#TODO: write a tiebreaker file... rank is determined for each hand but not which number
#TODO: for pairs, what the high card is, which suit for flush etc...


import hand_indices
import hand_rank
import tiebreaker
import math


with open('poker.txt') as file:

    P1Wins = 0
    P2Wins = 0
    hand = 0
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
        #print(P2Hand)

        # Convert the hands from text to numbers, and from a list to a set:
        P1Hand_Num = hand_indices.hand_indices(P1Hand)
        P2Hand_Num = hand_indices.hand_indices(P2Hand)

        #print(P1Hand_Num)
        #print(P2Hand_Num)

        P1Rank = hand_rank.hand_rank(P1Hand_Num)
        P2Rank = hand_rank.hand_rank(P2Hand_Num)

        #print(P1Rank)
        #print(P2Rank)


        P1W = False
        if P1Rank < P2Rank:
            P1W = True
        elif P2Rank < P1Rank:
            P1W = False
        else:
            W = tiebreaker.find_winner(P1Rank, P1Hand_Num, P2Hand_Num)
            if W == 1:
                P1W = True

        if P1W:
            P1Wins = P1Wins + 1
        else:
            P2Wins = P2Wins + 1

        hand = hand+1
        print(hand)

        #print(P1Rank, P2Rank, P1W)


    print(P1Wins, P2Wins)
