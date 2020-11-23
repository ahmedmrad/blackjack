import pyinputplus as pyip
import sys

BLACK_JACK = 21
'''int: Black jack module level variable

'''


class Player():
    '''Player class

    Player class implements a player object with several methods
    in order to play blackjack.

    Args:
        name (str) : Name of the player.
        cash_balance (int) : Player cash balance.
    Attributes:
        name (str) : Name of the player.
        cash_balance (int) : Player cash balance.
        maximum_bet (str) : Maximum bet the player is alowed to make in one turn.
        minimum_bet (int) : Minimun bet that the player is allowed to make.
        hand (Hand) : Hand object.
    '''

    def __init__(self, name='player', cash_balance=100):
        self.name = name
        self.cash_balance = cash_balance
        self.maximum_bet = cash_balance - 10
        self.minimum_bet = 10
        self.hand = Hand()

    def get_balance(self):
        '''Get balance method

        Get balance methods prints the player's name
        and the cash balance.
        '''
        print('The {} has {} $ in the bank.'.join(self.name, self.cash_balance))

    def bet(self):
        '''Bet a certain ammount

        Bet a certain ammount during a game of Blakcjack according to one's
        own fund.
        The change in the cash balance should be reflected.

        Args:
            bet_amount (int) : amount to be deposited
        '''

        bet_amount = pyip.inputNum('Faites vos jeux: ', min=self.minimum_bet)
        if bet_amount < self.maximum_bet:
            if self.cash_balance > bet_amount:
                self.cash_balance -= bet_amount
                print('Les jeux sont faits')
                return bet_amount
            else:
                print('You no longet have money in you balance. Goodbye.')
                sys.exit()

    def hit(self):
        '''Hit method

        Hit method asks if the player wants to hit or stay.

        Returns:
            (bool) : True if hit False if Stay
        '''
        print('Those are the cards you have: ')
        print(self.hand)
        print('Your had value is {}.'.join(self.hand.get_card_value()))
        hit_stay = pyip.inputMenu(['hit', 'stay'], numbered=True)
        if hit_stay == 'hit':
            return True
        else:
            return False


class Dealer():
    ''' Dealer class

    Dealer class

    '''

    def __init__(self, name='dealer', cash_balance=100, number_of_decks=1):
        self.name = name
        self.cash_balance = cash_balance
        self.number_of_decks = number_of_decks
        self.deck = Deck(self.number_of_decks)
        self.hand = Hand()

    def match(self, bet_amount):
        pass
    def collect_card(self):
        pass

    def discard_card(self):
        pass

class Game:
    """docstring for ClassName"""

    def __init__(self,):
        def __init__()
        self.arg = arg
