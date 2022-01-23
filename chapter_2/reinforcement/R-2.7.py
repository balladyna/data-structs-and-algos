# The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new
# account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter
# constructor syntax should continue to produce an account with zero balance.


class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0, nonzero_balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._nonzero_balance = nonzero_balance if nonzero_balance != 0 or not None else balance

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
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


cc = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5309", 1000)

