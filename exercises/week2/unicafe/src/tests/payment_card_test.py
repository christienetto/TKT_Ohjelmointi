import unittest
from payment_card import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        self.card = PaymentCard(1000)

    def test_constructor_sets_the_balance_right(self):
        self.assertEqual(str(self.card), "The card has 10.00 euros on it")


    def test_able_to_add_money(self):
        self.card.add_money(2500)

        self.assertEqual(self.card.balance_in_euros(), 35.0)


    def test_decrese_money(self):
        self.card.take_money(500)

        self.assertEqual(self.card.balance_in_euros(), 5.0)

    def test_min_money(self):
        self.card.take_money(1500)

        self.assertEqual(self.card.balance_in_euros(), 10.0)

    def test_min_money_true(self):
        value = self.card.take_money(1500)

        self.assertEqual(value, False)

    def test_card_exists(self):
        self.assertNotEqual(self.card, None)
