import unittest
from blackjack import Dealer, Game
from card import Card


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer(cash_balance=100)

    def tearDown(self):
        del self.dealer

    def test_dealer_match_bet_negative_value(self):
        self.assertEqual(
            self.dealer.match_bet(-50), 50,
            'Match bet methods accepts negative value. Check if absolute value implemented or if try catch statement present.'
        )

    def test_dealer_match_bet_ten_dollar(self):
        self.assertEqual(
            self.dealer.match_bet(10), 10,
            'Match bet is not matching bets correctly.'
        )

    def test_dealer_match_bet_bigger_than_cash_balance_value(self):
        self.assertRaises(SystemExit, self.dealer.match_bet, 110)

    def test_dealer_match_bet_bigger_than_cash_balance_in_absolute_value(self):
        self.assertRaises(SystemExit, self.dealer.match_bet, -110)

    def test_dealer_match_bet_cash_balance_negative_value(self):
        self.dealer.match_bet(-10)
        self.assertEqual(
            self.dealer.cash_balance, 90,
            'Cash balance not being substracted while allocating bets.'
        )

    def test_dealer_match_bet_cash_balance_positive_value(self):
        self.dealer.match_bet(10)
        self.assertEqual(
            self.dealer.cash_balance, 90,
            'Cash balance not being substracted while allocating bets.'
        )

    def test_dealer_match_bet_cash_balance_equivalent_value(self):
        self.dealer.match_bet(100)
        self.assertEqual(
            self.dealer.cash_balance, 0,
            'Match bet is not set to to accept bet equal to the cash balance. Check method implementation.'
        )

    def test_dealer_is_soft_17_true_card_values_less_than_seventeen_and_two_cards(
        self
    ):
        self.dealer.hand.add_card(
            [Card('Spades', 'Jack'),
             Card('Diamonds', 'Five')]
        )
        self.assertTrue(
            self.dealer.is_soft_17(), 'Is soft 17 no detecting soft 17.'
        )

    def test_dealer_is_soft_17_true_card_values_less_than_seventeen_and_three_cards(
        self
    ):
        self.dealer.hand.add_card(
            [
                Card('Spades', 'Four'),
                Card('Diamonds', 'Five'),
                Card('Hearts', 'Two')
            ]
        )
        self.assertTrue(
            self.dealer.is_soft_17(), 'Is soft 17 no detecting soft 17.'
        )

    def test_dealer_is_soft_17_false_card_values_less_than_seventeen_and_four_cards(
        self
    ):
        self.dealer.hand.add_card(
            [
                Card('Spades', 'Four'),
                Card('Diamonds', 'Five'),
                Card('Hearts', 'Two'),
                Card('Clubs', 'Three')
            ]
        )
        self.assertFalse(
            self.dealer.is_soft_17(), 'Is soft 17 no detecting soft 17.'
        )

    def test_dealer_is_soft_17_false_seventeen_exactly(self):
        self.dealer.hand.add_card(
            [Card('Spades', 'Jack'),
             Card('Diamonds', 'Seven')]
        )
        self.assertFalse(
            self.dealer.is_soft_17(), 'Is soft 17 no detecting soft 17.'
        )

    def test_dealer_is_soft_17_false_superior_to_seventeen(self):
        self.dealer.hand.add_card(
            [Card('Spades', 'Jack'),
             Card('Diamonds', 'Queen')]
        )
        self.assertFalse(
            self.dealer.is_soft_17(), 'Is soft 17 no detecting soft 17.'
        )

    def test_dealer_return_card_to_deck_multiple_cards(self):
        self.dealer.hand.add_card(self.dealer.deck.deal_two_cards())
        self.dealer.return_cards_to_deck(self.dealer.hand.hand)
        self.assertEqual(
            len(self.dealer.deck), 52, 'Return card to deck not working.'
        )

    def test_dealer_return_card_to_deck_one_card(self):
        self.dealer.hand.add_card(self.dealer.deck.deal_one_card())
        self.dealer.return_cards_to_deck(self.dealer.hand.hand)
        self.assertEqual(
            len(self.dealer.deck), 52, 'Return card to deck not working.'
        )

    def test_dealer_add_cash_to_balance_negative(self):
        self.dealer.add_to_cash_balance(-10)
        self.assertEqual(
            self.dealer.cash_balance, 110,
            'Add cash to balance not working properly.'
        )

    def test_dealer_add_cash_to_balance_positive(self):
        self.dealer.add_to_cash_balance(10)
        self.assertEqual(
            self.dealer.cash_balance, 110,
            'Add cash to balance not working properly.'
        )

    def test_dealer_add_cash_to_balance_zero(self):
        self.dealer.add_to_cash_balance(0)
        self.assertEqual(
            self.dealer.cash_balance, 100,
            'Add cash to balance not working properly.'
        )


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game_10_decks = Game(number_of_decks=10)

    def tearDown(self):
        del self.game
        del self.game_10_decks

    def test_game_blackjack_check_numbers_of_decks(self):
        self.assertEqual(
            len(self.game_10_decks.dealer.deck), 520,
            'Number of decks is not correct.'
        )

    def test_game_blackjack_payout_dealer_bet_float(self):
        self.assertEqual(
            type(self.game.blackjack_payout(10.00)), int,
            'Blackjack payout not returning int.'
        )

    def test_game_blackjack_payout_dealer_bet_int(self):
        self.assertEqual(
            type(self.game.blackjack_payout(10)), int,
            'Blackjack payout not returning int.'
        )

    def test_game_blackjack_payout_dealer_bet_negative(self):
        self.assertGreaterEqual(
            self.game.blackjack_payout(-10), 15,
            'Blackjack payout not returning positive 3:2 blackjack payout.'
        )

    def test_game_blackjack_payout_dealer_bet_zero(self):
        self.assertEqual(
            self.game.blackjack_payout(0), 0,
            'Blackjack payout not returning zero whe zero inputed.'
        )

    def test_game_blackjack_payout_dealer_bet_positive(self):
        self.assertGreaterEqual(
            self.game.blackjack_payout(10), 15,
            'Blackjack payout not returning 3:2 blackjack payout.'
        )

    def test_game_blackjack_result_blackjack_player_wins_dealer_hand_value_less_than_21(
        self
    ):
        self.game.player.hand.add_card(
            [Card('Hearts', 'Ace'),
             Card('Spades', 'King')]
        )
        self.game.dealer.hand.add_card(
            [
                Card('Hearts', 'Three'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, 125,
            'Blackjack result is not working for player balckjack.'
        )

    def test_game_blackjack_result_blackjack_player_wins_dealer_hand_value_more_than_21(
        self
    ):
        self.game.player.hand.add_card(
            [Card('Hearts', 'Ace'),
             Card('Spades', 'King')]
        )
        self.game.dealer.hand.add_card(
            [
                Card('Hearts', 'Three'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, 125,
            'Blackjack result is not working for player blackjack.'
        )

    def test_game_blackjack_result_player_bust_dealer_less_than_21(self):
        self.game.player.hand.add_card(
            [
                Card('Hearts', 'Queen'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Four')
            ]
        )
        self.game.dealer.hand.add_card(
            [Card('Hearts', 'Two'),
             Card('Spades', 'Queen')]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.dealer.cash_balance, 120,
            'Blackjack result not working when player busts and dealer has low card values'
        )

    def test_game_blackjack_result_player_bust_dealer_more_than_21_equal_to_hand_player(
        self
    ):
        self.game.player.hand.add_card(
            [
                Card('Hearts', 'Two'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.dealer.hand.add_card(
            [
                Card('Hearts', 'Two'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.dealer.cash_balance, 120,
            'Blackjack result not working when player busts and dealer has equal card values'
        )

    def test_game_blackjack_result_player_bust_dealer_more_than_21_superior_to_hand_player(
        self
    ):
        self.game.player.hand.add_card(
            [
                Card('Hearts', 'Two'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.dealer.hand.add_card(
            [
                Card('Hearts', 'Four'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.dealer.cash_balance, 120,
            'Blackjack result not working when player busts and dealer has higher card values'
        )

    def test_game_blackjack_result_player_wins_dealer_bust_higher_than_21(
        self
    ):
        self.game.player.hand.add_card(
            [Card('Hearts', 'King'),
             Card('Spades', 'Eight')]
        )
        self.game.dealer.hand.add_card(
            [
                Card('Hearts', 'Four'),
                Card('Spades', 'King'),
                Card('Diamonds', 'Queen')
            ]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, 120,
            'Blackjack result not working when player wins, dealer busts with card values superior to 21.'
        )

    def test_game_blackjack_result_player_wins_dealer_bust_21(self):
        self.game.player.hand.add_card(
            [Card('Hearts', 'King'),
             Card('Spades', 'Eight')]
        )
        self.game.dealer.hand.add_card(
            [Card('Hearts', 'Ace'),
             Card('Spades', 'King')]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, 120,
            'Blackjack result not working when player wins, dealer busts with card values equal to 21.'
        )

    def test_game_blackjack_result_dealer(self):
        self.game.player.hand.add_card(
            [Card('Hearts', 'King'),
             Card('Spades', 'Eight')]
        )
        self.game.dealer.hand.add_card(
            [Card('Hearts', 'King'),
             Card('Spades', 'Nine')]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.dealer.cash_balance, 120,
            'Blackjack result not working when dealer wins and player card values less than 21.'
        )

    def test_game_blackjack_result_tie_blackjack(self):  # == > tie not working
        self.game.player.hand.add_card(
            [Card('Hearts', 'Ace'),
             Card('Spades', 'King')]
        )
        self.game.dealer.hand.add_card(
            [Card('Diamonds', 'Ten'),
             Card('Clubs', 'Ace')]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, self.game.dealer.cash_balance,
            'Blackjack result not working when dealer and player tie at 21.'
        )

    def test_game_blackjack_result_tie_less_than_blackjack(self):
        self.game.player.hand.add_card(
            [Card('Hearts', 'Seven'),
             Card('Spades', 'King')]
        )
        self.game.dealer.hand.add_card(
            [Card('Diamonds', 'Ten'),
             Card('Clubs', 'Seven')]
        )
        self.game.blackjack_result(10, 10)
        self.assertEqual(
            self.game.player.cash_balance, self.game.dealer.cash_balance,
            'Blackjack result not working when dealer and player tie at value less than 21.'
        )


if __name__ == '__main__':
    unittest.main()
