# Prices are in cents
CHEAP = 250
YUMMY = 400


class PaymentCard:
    def __init__(self, balance):
        # The balance is in cents
        self.balance = balance

    def eat_cheap(self):
        if self.balance >= CHEAP:
            self.balance -= CHEAP

    def eat_yummy(self):
        if self.balance >= YUMMY:
            self.balance -= YUMMY
    def balance_in_euros(self):
        return self.balance / 100
    def add_money(self, amount):
        if amount < 0:
            return

        self.balance += amount

        if self.balance > 15000:
            self.balance = 15000

    def __str__(self):
        balance_in_euros = round(self.balance / 100, 2)
        return "The card has {:0.2f} euros on it".format(balance_in_euros)


# Code to create an instance and test the functionality
if __name__ == "__main__":
    # Create a PaymentCard object with an initial balance
    my_card = PaymentCard(5000)  # 50.00 euros

    print(my_card)  # Should print initial balance

    my_card.eat_cheap()  # Spend some money
    print(my_card)  # Check balance after spending on cheap item

    my_card.eat_yummy()  # Spend some money on a yummy item
    print(my_card)  # Check balance after spending on yummy item

    my_card.add_money(2000)  # Add some money to the card
    print(my_card)  # Check balance after adding money

    my_card.add_money(-500)  # Try to add negative amount (should not change balance)
    print(my_card)  # Check balance after invalid add

    my_card.add_money(16000)  # Try to add more than max limit (should cap at 15000)
    print(my_card)  # Check balance after adding more than the limit

