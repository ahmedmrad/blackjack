'''Blackjack

Blackjack module defines a player, dealer and game class. Most of the game logic is implemented in this module.

Attributes:
    BLACK_JACK (int) : Blackjack score value of 21

todos:
    - Make sure some class instance only take values superior to minimun.
    - Write the edge test cases
'''

import pyinputplus as pyip
import sys
from card import Card, Deck, card_object_check, Hand

BLACK_JACK = 21


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

        Get balance methods prints the player's nameand cash balance.
        '''
        print(
            'The {} has {} $ in the bank.'.join(self.name, self.cash_balance)
        )

    def bet(self):
        '''Bet a certain ammount

        Asks the user to bet a certain ammount during a game of Blakcjack according to one's own fund.
        The change in the cash balance should be reflected.

        Args:
            bet_amount (int) : amount to be betted
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

    Dealer class, implements the main methods a dealer would use in playing the game.

    Args:
        name (str) : Dealer name, defaults to dealer.
        cash_balance (int) : Dealer's cash balance, defaults to 100
        number_of_decks (int) : Number of decks to be created.
    Attributes:
        name (str) : Dealer name, defaults to dealer.
        cash_balance (int) : Dealer's cash balance, defaults to 100
        number_of_decks (int) : Number of decks to be created.
        deck (Deck) : Deck object
        hand (Hand) : Hand object
    '''

    def __init__(self, name='dealer', cash_balance=1000, number_of_decks=1):
        self.name = name
        self.cash_balance = cash_balance
        self.number_of_decks = number_of_decks
        self.deck = Deck(self.number_of_decks)
        self.hand = Hand()

    def get_balance(self):
        '''Get balance method

        Get balance methods prints the dealer's name and cash balance.
        '''
        print(
            'The {} has {} $ in the bank.'.join(self.name, self.cash_balance)
        )

    def match_bet(self, bet_amount):
        if self.cash_balance > bet_amount:
            self.cash_balance -= bet_amount
            return bet_amount
        else:
            print('The bank went bust.')
            sys.exit()

    def collect_card(self, dealer_hand, player_hand):
        '''Collect card

        Collect card method collects cards from both the player's and the dealer's respective hands.

        Args:
            dealer_hand (list) : List of Card objects.
            player_hand (list) : List of Card objects.

        Returns:
            collected_cards (list) : List of Card objects.
        '''
        collected_cards = []
        collected_cards.extend(dealer_hand.hand + player_hand.hand)
        return collected_card

    @card_object_check
    def return_cards_to_deck(self, collected_cards):
        '''Return cards to deck

        Method that returns collected cards to deck.

        Args:
            collected_cards (list) : List of card objects made of the player's and the dealer's respective hands.
        '''
        if type(new_cards) == type([]):
            self.deck.all_cards.extend(new_cards)
        else:
            self.deck.all_cards.append(new_cards)


'''
    def discard_card(self,cards_collected):
        pass
'''


class Game():
    '''Game

    Game Class

    Args:


    Attributes:

    '''

    def __init__(self):
        self.player = Player('player_1', 100)
        self.dealer = Dealer(number_of_decks=1)
        self.discard = []

    def play
