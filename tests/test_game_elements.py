import unittest
import copy
from game_elements import Card, Deck


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card('Hearts', 'Queen')

    def tearDown(self):
        del self.card

    def test_card__str__(self):
        self.assertEqual(str(self.card), 'Queen of Hearts')

    def test_card_get_suit(self):
        self.assertEqual(
            self.card.get_suit(), 'Hearts',
            'Suit of card is wrong. Check the suits global variable.'
        )

    def test_card_get_rank(self):
        self.assertEqual(
            self.card.get_rank(), 'Queen',
            'Rank of card wrong. Check the ranks global variable.'
        )

    def test_card_get_value(self):
        self.assertEqual(self.card.get_value(), 10)


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
        non_shuffled_deck = copy.deepcopy(self.deck)
        self.deck.shuffle()
        self.assertNotEqual(
            self.deck.all_cards, non_shuffled_deck.all_cards,
            'Shuffle method not working. Check if random is imported or.'
        )

    def test_deck_shuffle_deck_not_none(self):
        self.deck.shuffle()
        self.assertIsNotNone(
            self.deck, 'Deck is None object. Check the shuffle method.'
        )


class TestPlayer(unittest.TestCase):
    pass


class TestHand(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
