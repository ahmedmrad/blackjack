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
BLACK_JACK_PAYOUT = 3 / 2


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

    def show_balance(self):
        '''Show balance method

        Show balance methods prints the player's nameand cash balance.
        '''
        print(
            'The {} has {} $ in the bank.'.join(self.name, self.cash_balance)
        )

    def get_balance(self):
        '''Get balance

        Get balance returns the player's cash balance
        '''
        return self.cash_balance

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

    def add_to_cash_balance(self, bet_amount):
        '''Add to cash balance

        Add to cash balance method add bet winnings to the player's cash balance.

        Args:
            bet_amount (int) : winning bet amount
        '''
        self.cash_balance += bet_amount


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

    def show_balance(self):
        '''Show balance method

        Show balance methods prints the dealer's name and cash balance.
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

    def is_soft_17(self):
        '''Is soft 17

        Is soft 17 method checks if the dealer's hand is a soft 17 or no.

        Returns:
            (bool) : True if dealer cards value is 17, False if otherwise
        '''
        if self.hand.get_card_value() < 17:
            return True
        else:
            return False

    def collect_card(self, dealer_hand, player_hand):
        '''Collect card

        Collect card method collects cards from both the player's and the dealer's respective hands.

        Args:
            dealer_hand (list) : List of Card objects.
            player_hand (list) : List of Card objects.

        Returns:
            round_cards (list) : List of Card objects.
        '''
        round_cards = []
        round_cards.extend(dealer_hand.hand + player_hand.hand)
        return round_cards

    @card_object_check
    def return_cards_to_deck(self, discard_pot):
        '''Return cards to deck

        Method that returns collected round cards to deck.

        Args:
            discard_card (list) : List of card objects made of the player's and the dealer's respective hands.
        '''
        if type(discard_pot) == type([]):
            self.deck.all_cards.extend(discard_pot)
        else:
            self.deck.all_cards.append(discard_pot)

    def add_to_cash_balance(self, bet_amount):
        '''Add to cash balance

        Add to cash balance method add bet winnings to the Dealer's cash balance.

        Args:
            bet_amount (int) : winning bet amount
        '''
        self.cash_balance += bet_amount


class Game():
    '''Game

    Game Class


    Attributes:
        player (Player) : Player instance
        dealer (Dealer) : Dealer instance
    '''

    def __init__(self, name_player, player_cash_balance, dealer_cash_balance, number_of_decks):
        self.name_player = name_player
        self.player_cash_balance = player_cash_balance
        self.dealer_cash_balance = dealer_cash_balance
        self.number_of_decks = number_of_decks
        self.player = Player('player_1', 100)
        self.dealer = Dealer(number_of_decks=1)
        self.discard_pot = []

    def player_balance(self):
        '''Player balance

        Player balance method

        Returns:
            (int) : Cash balance of player.
        '''
        print('Welcome to blackjack: ')
        self.player.show_balance()
        return self.player.get_balance()

    def bets(self):
        '''Bets

        Bets method, both player and dealer make their bets.

        Returns:
            player_bet (int) : player bet amount
            dealer_bet (int) : dealer bet amount
        '''
        player_bet = self.player.bet()
        dealer_bet = self.dealer.match_bet()
        return player_bet, dealer_bet

    def blackjack_payout(self, dealer_bet):
        '''Blackjack payout

        Blackjack payout method readjusts the dealer cash balance and gives out the proper payout.

        Args:
            dealer_bet (int) : Original matched bet.
        Returns:
            blackjack_payout (int) : Blackjack payout following 3:2 rule.
         '''
            dealer_bet += self.dealer.match_bet(0.5 * dealer_bet)
            return int(dealer_bet)

    def deal_cards(self):
        ''' Deal card

        Deal card method distributes cards to both player and dealer hands
        '''
        print('The dealer is dealing the cards.')
        self.dealer.deck.shuffle()
        self.player.hand.add_card(self.dealer.deck.deal_two_cards())
        self.dealer.hand.add_card(self.dealer.deck(deal_two_cards()))

    def adjust_player_hand(self):
        '''Adjust hand

        Adjust hand method, prompts the player to hit or stay and check and adjusts cards accordingly.
        '''
        hit = self.player.hit()
        if hit == True:
            self.player.add_card(self.dealer.deal_on())

    def adjust_dealer_hand(self):
        '''Adjust dealer hand

        Adjust dealer hand method adjusts dealer hand if soft 17 is true.
        '''
        if is_soft_17() == True:
            self.dealer.add_card(dealer.deck.deal_one_card())

    def blackjack_payouts(self, player_bet, dealer_bet):
        '''Blackjack

        Blackjack logic handler method. Handles most of the game logic.

        Args:
            player_bet (int) : Player bet amount.
            dealer_bet (int) : Dealer bet amount.
        '''
        if (self.player.hand.get_card_value() == BLACK_JACK) and (self.dealer.hand.get_card_value != BLACK_JACK):
            print('Blackjack, player wins')
            dealer_bet_updated = self.dealer.blackjack_payout(dealer_bet)
            self.player.add_to_cash_balance(dealer_bet_updated)
        elif (self.player.get_card_value() > BLACK_JACK):
            print('Bust, dealer wins.')
            self.dealer.add_to_cash_balance(player_bet + dealer_bet)
        elif(self.player.get_card_value() < BLACK_JACK) and (self.dealer.get_card_value() > BLACK_JACK):
            print('Dealer bust. Player wins.')
            self.player.add_to_cash_balance(player_bet, dealer_bet)
        elif (self.player.get_card_value() < BLACK_JACK) and (self.player.get_card_value() > self.dealer.get_card_value()):
            print('Player wins.')
            self.player.add_to_cash_balance(player_bet, dealer_bet)
        elif (self.player.get_card_value() < BLACK_JACK) and (self.dealer.get_card_value() > self.player.get_card_value()):
            print('Dealer wins.')
            self.dealer.add_to_cash_balance(player_bet + dealer_bet)
        elif self.player.get_card_value() == self.dealer.get_card_value():
            print('Tie, nobody wins')
            self.player.add_to_cash_balance()
#

    def discard_card(self):
        '''Discard card

        Discard card method
        '''
        round_cards = self.dealer.collect_card(
            self.player.hand, self.dealer.hand)
        self.discard_pot.extend(round_cards)
        return discard_pot

    def return_cards_to_deck_and_reshuffle(self, discard_pot):
        '''Return cards to deck and reshuffle

        Return cards to deck and reshuffle method

        Args:
            discard_pot (list) : List of Card objects.
        '''
        self.dealer.return_cards_to_deck(discard_pot)
        self.dealer.deck.shuffle()

    def exit_game(self):
        '''Exit game

        Exit game method prompts player if he wants to continue game of not.
        Returns:
            (bool) : True if exit game, False if keep on playing
        '''
        exit_game = pyip.inputMenu(
            ['Exit game', 'Keep on playing'], numbered=True)
        if exit_game == 'Exit game':
            return True
        else:
            return False
