import unittest
import copy
from card import Card, Deck, Hand, card_object_check


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
        self.deck_multiple = Deck(10)

    def tearDown(self):
        del self.deck
        del self.deck_multiple

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

    def test_deck_imlements_multiple(sefl):
        self.assertEqual(
            len(self.self.deck_multiple), 520,
            'Multiple decks not implemented.'
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
        self.assertIsNotNone(
            self.deck, 'Deck is None object. Check the shuffle method.'
        )

    def test_deck_lenght_deck_after_dealing_one(self):
        original_deck = copy.deepcopy(self.deck)
        self.deck.deal_one_card()
        self.assertEqual(
            len(self.deck),
            len(original_deck) - 1,
            'Deal one card is not working. Check if pop is implemented and calling the right object.'
        )

    def test_deck_deal_one_card_if_element_is_card(self):
        self.assertIsInstance(
            self.deck.deal_one_card(), Card,
            'Deal one card method is not returning card objects.'
        )

    def test_deck_lenght_deck_after_dealing_two(self):
        original_deck = copy.deepcopy(self.deck)
        self.deck.deal_two_cards()
        self.assertEqual(
            len(self.deck),
            len(original_deck) - 2,
            'Deal two cards is not working. Check if method is implemented and calling the right object.'
        )

    def test_deck_deal_two_cards_if_return_is_list(self):
        self.assertEqual(
            type(self.deck.deal_two_cards()), list,
            'Deal two cards is not producing a list. Check if the return value of the method is actually a list.'
        )

    def test_deck_deal_two_cards_if_elements_are_card(self):
        for elem in self.deck.deal_two_cards():
            self.assertIsInstance(
                elem, Card,
                'Deal two cards is not adding Card objects. Check if the object reference is correct.'
            )


class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

        (
            self.card_1, self.card_2, self.card_3, self.card_4, self.card_5,
            self.card_6, self.card_7
        ) = (
            Card('Diamonds', 'Two'), Card('Spades', 'King'),
            Card('Clubs', 'Ace'), Card('Spades',
                                       'Queen'), 'this is not a card', 10, 9.5
        )

    def tearDown(self):
        del self.hand
        del self.card_1
        del self.card_2
        del self.card_3
        del self.card_4
        del self.card_5
        del self.card_6
        del self.card_7

    def test_hand_add_new_card_adds_one_card(self):
        self.hand.add_card(self.card_1)
        self.assertEqual(
            len(self.hand), 1,
            'Add card is not working properly. It should contain one element.'
        )

    def test_hand_add_new_card_adds_two_or_more_cards(self):
        self.hand.add_card([self.card_1, self.card_2, self.card_3])
        self.assertGreaterEqual(
            len(self.hand), 2,
            'Add card is not working properly. It should contain two or more elements.'
        )

    def test_hand_one_card_added_is_list(self):
        self.hand.add_card(self.card_1)
        self.assertEqual(
            type(self.hand.hand), list,
            'Hand is not composed of list of cards. Check if the add_card method instantiate an empty list and that proper appending methods are implemented.'
        )

    def test_hand_two_or_more_card_hand_is_list(self):
        self.hand.add_card([self.card_1, self.card_2, self.card_3])
        self.assertEqual(
            type(self.hand.hand), list,
            'Hand is not composed of list of cards. Check if the add_card method instantiate an empty list and that proper appending methods are implemented.'
        )

    def test_hand_card_added_is_card_instance(self):
        self.hand.add_card([self.card_1, self.card_2, self.card_3])
        for elem in self.hand.hand:
            self.assertIsInstance(
                elem, Card,
                'Hand does not contain Card objects. Check if you are adding card objects'
            )

    def test_hand_card_added_decorator_type_error_int(self):
        self.assertRaises(TypeError, self.hand.add_card, self.card_5)

    def test_hand_card_added_decorator_type_error_int(self):
        self.assertRaises(TypeError, self.hand.add_card, self.card_6)

    def test_hand_card_added_decorator_type_error_int(self):
        self.assertRaises(TypeError, self.hand.add_card, self.card_7)

    def test_hand_card_added_decorator_type_error_list_mixed_card_object_and_other_type(
        self
    ):
        self.assertRaises(
            TypeError, self.hand.add_card,
            [self.card_4, self.card_5, self.card_6]
        )

    def test_hand_card_added_decorator_type_error_list_other_type(self):
        self.assertRaises(
            TypeError, self.hand.add_card,
            [self.card_5, self.card_6, self.card_7]
        )

    def test_hand_get_card_value_value_less_than_twenty_one(self):
        self.hand.add_card([self.card_1, self.card_2])
        self.assertLess(
            self.hand.get_card_value(), 21,
            'Hand value not less than 21. Get card value method is not calculating the hand value right.'
        )

    def test_hand_get_card_value_has_ace(self):
        self.hand.add_card([self.card_2, self.card_3])
        self.assertEqual(
            self.hand.get_card_value(), 21,
            'Hand value not 21. Get card value method is not calculating right.'
        )

    def test_hand_get_card_value_value_more_than_twenty_one(self):
        self.hand.add_card([self.card_1, self.card_2, self.card_4])
        self.assertGreater(
            self.hand.get_card_value(), 21,
            'Hand value is not greater than 21. Get card calue not calculating hand value right.'
        )


if __name__ == '__main__':
    unittest.main()
