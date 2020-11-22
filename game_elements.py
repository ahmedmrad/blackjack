'''Blackjack

Blackjack modules contains most of the classes in order to play a blackjack game

Attributes:
    suits (tuple): playing card suit values, tuple of str
    ranks (tuple): playing card rank, tuple of str
    values (dict): playing card rank and their values, keys are playing card rank and values are playing card values in a blackjack game

Todo:

'''

from random import shuffle

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
        all_cards (:obj: `list` of :obj: `Card`) : deck containing all cards
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
        shuffle(self.all_cards)

    def deal_one_card(self):
        '''Deal one card

        Deal card from the top of the deck.
        '''
        return self.all_cards.pop()

    def deal_two_cards(self):
        '''Deal two cards

        Deal two cards from the top of the deck.
        '''

        return [self.all_cards.pop() for index in range(2)]


class Hand():
    '''Hand class

    Hand class hold the dealt cards,
    store the extra cards if needed and determines
    the total value of the hand

    Attributes:
        hand (list) : list that holds the cards dealt
    '''

    def __init__(self):
        self.hand = []

    def add_card(self, new_cards):
        ''' Add card method

        Args:
            new_cards ()
        '''
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        list_hand = []
        if type(self.hand) == type([]):
            return ' '.join(['| %-2s |' % (i,) for i in self.hand])
        else:
            return str(self.hand)

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
                if total_value > 21:
                    break
        return total_value


class Bank():
    '''Bank class

    Bank class instantiates the amount of mony available for
    both the dealer and the player. The class comes with a deposit and widthraw method.

    Args:
        name (str) : name of the person's account, the dealer's bank or the player's bank.
        gambling_account (int) = value of money available for gambling

    Attributes:
        name (str) : name of the person's account, the dealer's bank or the player's bank.
        gambling_account (int) = value of money available for gambling
    '''

    def __init__(self, name='dealer', gambling_account=100, **kwargs):
        self.name = name
        self.gambling_account = gambling_account
        super().__init__(**kwargs)

    def __str__(self):
        return f'The {self.name} has {self.gambling_account} $ in the bank.'

    def deposit(self, amount):
        '''deposit method

        Deposit the bets to the gambling account.

        Args:
            amount (int) : amount to be deposited
        '''
        self.gambling_account += amount

    def widthraw(self, amount):
        '''widthraw method

        Widthraw money if bet is lost.

        Args:
            amount (int) : amount to be deposited
        '''
        self.gambling_account -= amount


class Player(Bank, Hand):

    def __init__(self, name, gambling_account, **kwargs):
        super().__init__(name=name, gambling_account=gambling_account, **kwargs)
        Hand.__init__(self)


class PlayerMoves(Hand, Bank, Dealer):
    ''' Player class

    Player class implements players and dealers and the methods each players needs

    Args:
        name (str) : name of the player, defaults to dealer

    Attributes:
        name (str) : name of the player, defaults to dealer
    '''

    def __init__(self, name='player'):

        self.name = name

    def hit(self):
        '''Add another card
        '''
        pass

    def stand(self):
        '''Take no more card
        '''
        pass

    def double_down(self):
        '''The player is allowed to increase the initial bet up to 100% in exchange for committing to stand after receiving exactly one more card. The additional bet is placed in the betting box next to the original bet.
        '''
        pass

    def split(self):
        '''If the first two cards of a hand have the same value, the player can split them into two hands, by moving a second bet equal to the first into an area outside the betting box. The dealer separates the two cards and draws an additional card on each, placing one bet with each hand. the hands are treated as independent new hands, with the player winning or losing their wager separately for each hand.
        '''
        pass

    def surrender(self):
        '''When the player surrenders, the house takes half the player's bet and returns the other half to the player. Only when dealer gets a blackjack
        '''
        pass


class Game:
    """docstring for ClassName"""

    def __init__(self,):
        def __init__()
        self.arg = arg
