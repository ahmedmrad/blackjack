'''Card

Card module contains most of the classes in order to create a deck containing cards
and a proper hand in blackjack.

Attributes:
    suits (tuple): playing card suit values, tuple of str
    ranks (tuple): playing card rank, tuple of str
    values (dict): playing card rank and their values, keys are playing card rank and values are playing card values in a blackjack game

'''

from random import shuffle
from functools import wraps

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


class Card():
    '''Card class to create a single instance of card

    Card objects hold the suit, rank and value of the playing card

    Args:
        suit (str) : Playing card suit.
        rank (str) : Playing card rank.

    Attributes:
        suit (str) : Playing card suit.
        rank (str) : Playing card rank.
        value (int) : Playing card value accroding to blackjack rules.
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():
    '''Deck class to create the full deck.

    A deck is constructed and filled with Card objects

    Attributes:
        all_cards (list) : List containing card objects
    '''

    def __init__(self, number_of_decks=1):
        self.all_cards = []
        self.number_of_decks = number_of_decks
        for i in range(self.number_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        '''Suffle card elements in deck

        This method Shuffles the cards in the deck. The shuffling happens inplace.
        '''
        shuffle(self.all_cards)

    def deal_one_card(self):
        '''Deal one card

        Deal card from the top of the deck.

        Returns:
            (Card) : Returns card object.
        '''
        return self.all_cards.pop()

    def deal_two_cards(self):
        '''Deal two cards

        Deal two cards from the top of the deck.

            (list) : Returns list of two card objects.
        '''

        return [self.all_cards.pop() for index in range(2)]


def card_object_check(method):

    @wraps(method)
    def inner(self, new_cards=None):
        if type(new_cards) == list:
            if any(not isinstance(elem, Card) for elem in new_cards):
                raise TypeError('List objects must be of type Card.')
            else:
                return method(self, new_cards)
        else:
            if not isinstance(new_cards, Card):
                raise TypeError(
                    f'List objects must be of type Card not {type(new_cards)}.'
                )
            else:
                return method(self, new_cards)

    return inner


class Hand():
    '''Hand class

    Hand class hold the dealt cards,
    store the extra cards if needed and determines
    the total value of the hand

    Attributes:
        hand (list) : list that holds the cards dealt, defaults to empty
    '''

    def __init__(self):
        self.hand = []

    @card_object_check
    def add_card(self, new_cards):
        ''' Add card

        Add Card method add the cards to the hand.
        The method handles adding two cards delt in the begining
        or adding one card when hitting during the game.

        Args:
            new_cards (list) : list / single Card object(s)
        returns:
            hand (list) : returns list of Card objects
        '''
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        list_hand = []
        if type(self.hand) == type([]):
            return ''.join(['| %-2s |' % (i, ) for i in self.hand])
        else:
            return str(self.hand)

    def __len__(self):
        return len(self.hand)

    def get_card_value(self):
        '''Get card values

        Calculate the total value of the current hand
        and adjust the ace value according to the total value

        Returns:
            total_value (int) : total value of the hand
        '''
        total_value = 0
        for card in self.hand:
            total_value += card.value
        if total_value < 21:
            for card in self.hand:
                if card.rank == 'Ace':
                    total_value += 10
        return total_value
