import unittest
from blackjack import Dealer


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()
        self.dealer_bust = Dealer(cash_balance=10)

    def tearDown(self):
        del self.dealer
        del self.dealer_bust

    def test_dealer_match_bet_negative_value(self):
        pass

    def test_dealer_match_bet_ten_dollar(self):
        pass

    def test_dealer_match_bet_cash_balance(self):
        pass

    def test_dealer_match_bet_superior_to_cash_balance(self):
        pass

    def test_dealer_collect_card_dealer_hand_and_player_hand_both_have_two_cards_each(
        self
    ):
        pass

    def test_dealer_collect_card_both_hands_are_empty(self):
        pass

    def test_dealer_collect_card_hand_empty_and_hand_full(self):
        pass

    def test_dealer_collect_card_dealer_both_hands_are_full(self):
        pass

    def test_dealer_return_card_to_deck(self):
        pass


# self.assertRaises(SystemExit):

if __name__ == '__main__':
    unittest.main()
