'''Blackjack

Blackjack modules contains most of the classes in order to play a blackjack game

Attributes:
    suits (tuple): playing card suit values, tuple of str
    ranks (tuple): playing card rank, tuple of str
    values (dict): playing card rank and their values, keys are playing card rank and values are playing card values in a blackjack game

Todo:

'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace'
)

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 1
}


class Card:
    '''Card class to create a single instance of card

    Card objects hold the suit, rank and value of the playing card

    Args:
        suit (str): Playing card suit.
        rank (str): Playing card rank.

    Attributes:
        suit (str): Playing card suit.
        rank (str): Playing card rank.
        value (int): Playing card value accroding to blackjack rules.
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def get_suit(self):
        '''Access the suit value.

        This method returns the suit value.

        Returns:
            suit (str): Playing card suit.
        '''
        return self.suit

    def get_rank(self):
        '''Access the rank value.

        This method returns the rank value

        Returns:
            rank (str): Playing card rank
        '''
        return self.rank

    def get_value(self):
        '''Access the card value.

        This method returns the card value.

        Returns:
            value (int): Playing card value
        '''
        return self.value


class Deck:
    '''Deck class to create the full deck.

    A deck is constructed and filled with Card objects

    Attributes:
        all_cards (:obj: `list` of :obj: `Card`): deck containing all cards
    '''

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        '''Suffle card elements in deck

        This method Shuffles the cards in the deck. The shuffling happens inplace.
        '''
        random.shuffle(self.all_cards)


''' better in game
    def deal_card(self):
        return self.all_cards.pop()
'''


class Player():
    """docstring for Player"""

    def __init__(self, arg):
        self.arg = arg


class Hand():
    """docstring for hand"""

    def __init__(self, arg):
        self.arg = arg
