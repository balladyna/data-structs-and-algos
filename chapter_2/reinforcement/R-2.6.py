# If the parameter to the make payment method of the CreditCard class were a negative number, that would have the
# effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative
# value is sent.
wrong_parameter_message = "Wrong type of parameter"


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        try:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        except TypeError:
            print(wrong_parameter_message)

    def make_payment(self, amount):
        while amount >= 0:
            try:
                self._balance -= amount
            except ValueError:
                print(wrong_parameter_message)


cc = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5309", 1000)


print(cc.get_limit()