import unittest
import copy
from card import Card, Deck


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card('Hearts', 'Queen')

    def tearDown(self):
        del self.card

    def test_card__str__(self):
        self.assertEqual(str(self.card), 'Queen of Hearts')

    def test_card_get_suit(self):
        self.assertEqual(
            self.card.suit, 'Hearts',
            'Suit of card is wrong. Check the suits global variable.'
        )

    def test_card_get_rank(self):
        self.assertEqual(
            self.card.rank, 'Queen',
            'Rank of card wrong. Check the ranks global variable.'
        )

    def test_card_get_value(self):
        self.assertEqual(self.card.value, 10)


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        del self.deck

    def test_deck_all_cards_is_list(self):
        self.assertIsInstance(
            self.deck.all_cards, list,
            'Deck is not a list. Check the deck constructor'
        )

    def test_deck_all_cards_has_card_instance(self):
        for elem in self.deck.all_cards:
            self.assertIsInstance(
                elem, Card,
                'Deck has no card instance. Check the deck constructor.'
            )

    def test_deck__len__(self):
        self.assertEqual(
            len(self.deck.all_cards), 52,
            'Deck does not have 52 cards. Check the suits, ranks and values, global variables for any discrepency.'
        )

    def test_deck_shuffle_different_than_original_deck(self):
        original_deck = copy.deepcopy(self.deck)
        self.deck.shuffle()
        self.assertNotEqual(
            self.deck.all_cards, original_deck.all_cards,
            'Shuffle method not working. Check if random is imported or the deck value is assigned to another variable.'
        )

    def test_deck_shuffle_deck_not_none(self):
        self.deck.shuffle()
        self.assertIsNotNone(self.deck, 'Deck is None object. Check the shuffle method.'
                             )

    def test_deck_lenght_deck_after_dealing_one(self):
        original_deck = copy.deepcopy.(self.deck)
        self.deck.deal_card()
        self.assertEquals(len(self.deck), len(original_deck) - 1,
                          'Deal one card is not working. Check if pop is implemented and calling the right object.')

    def test_deck_deal_one_card_if_element_is_card(self):
        self.assertIsInstance(self.deck.deal_card(
        ), Card, 'Deal one card method is not returning card objects.')

    def test_deck_lenght_deck_after_dealing_two(self):
        original_deck = copy.deepcopy.(self.deck)
        self.deck.deal_card()
        self.assertEquals(len(self.deck), len(original_deck) - 2,
                          'Deal two cards is not working. Check if method is implemented and calling the right object.')

    def test_deck_deal_two_cards_if_return_is_list(self):
        self.assertIsInstance(type(self.deck.deal_two_cards(
        )), list, 'Deal two cards is not producing a list. Check if the return value of the method is actually a list.')

    def test_deck_deal_two_cards_if_elements_are_card(self):
        for elem in self.deck.deak_two_cards():
            self.assertEquals(
                elem, Card, 'Deal two cards is not adding Card objects. Check if the object reference is correct.')


class TestHand(unittest.TestCase):

    def setUp(self):
        hand = Hand()
        (card_1, card_2, card_3) = (Card('Diamonds', 'Two' card_4, card_5, card_6),
                                    Card('Spades', 'King'), Card('Clubs', 'Ace'), Card('Spades', 'Queen'), 'this is not a card', 10,)

    def tearDown(self):
        del hand
        del card_1
        del card_2
        del card_3
        del card_4
        del card_5
        del card_6

    def test_hand_add_new_card_adds_one_card(self):
        self.hand.add_card(card_1)
        self.assertEquals(len(
            self.hand), 1, 'Add card is not working properly. It should contain one element.')

    def test_hand_add_new_card_adds_two_or_more_cards(self):
        self.hand.add_card([card_1, card_2, card_3])
        self.assertGreaterEqual(len(
            self.hand), 2, 'Add card is not working properly. It should contain two or more elements.')

    def test_hand_one_card_added_is_list(self):
        self.hand.add_card(card_1)
        self.assertIsInstance(type(
            hand.hand), list, 'Hand is not composed of list of cards. Check if the add_card method instantiate an empty list and that proper appending methods are implemented.')

    def test_hand_two_or_more_card_hand_is_list(self):
        self.hand.add_card([card_1, card_2, card_3])
        self.assertIsInstance(type(
            hand.hand), list, 'Hand is not composed of list of cards. Check if the add_card method instantiate an empty list and that proper appending methods are implemented.')

    def test_hand_card_added_is_card_instance(self):
        self.hand.add_card([card_1, card_2, card_3])
        for elem in self.hand.hand:
            self.assertIsInstance(
                elem, Card, 'Hand does not contain Card objects. Check if you are adding card objects')

    def test_hand_get_card_value_value_less_than_twenty_one(self):
        self.hand.add_card([card_1, card_2])
        self.assertLess(self.hand.get_card_value(
        ), 21, 'Hand value not less than 21. Get card value method is not calculating the hand value right.')

    def test_hand_get_card_value_has_ace(self):
        self.hand.add_card([card_2, card_3])
        self.assertEquals(hand.test_card_get_value(
        ), 21, 'Hand value not 21. Get card value method is not calculating right.')

    def test_hand_get_card_value_value_more_than_twenty_one(self):
        self.hand.add_card([card_1, card_2, card_4])
        self.assertRaises(self.hand.get_card_value(
        ), ValueError, 'Hand value superior to 21. Get card value mehtod is allowing a hand to be more than 21. That is illegal in blackjack rules.')


if __name__ == '__main__':
    unittest.main()
