
# This file accepts a hand of five cards in the format that Project Euler
# defines (ie AS for Ace of Spades, TC for Ten of Clubs) and returns the
# indices of the cards in the deck (ie 51 for Ace of Spades, 8 for Ten of Clubs).



# Let's index the cards in the deck from 0 to 51,
#  0 to 12 = 2 to Ace of Spades
# 13 to 25 = 2 to Ace of Hearts
# 26 to 38 = 2 to Ace of Diamonds
# 39 to 51 = 2 to Ace of Clubs

Clubs = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
Diamonds = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD']
Hearts = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH']
Spades = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS']

deck = []
deck.extend(Clubs)
deck.extend(Diamonds)
deck.extend(Hearts)
deck.extend(Spades)

def hand_indices(hand_text):

    hand_numbers = set()
    for card in hand_text:
        hand_numbers.add(deck.index(card))

    return hand_numbers


