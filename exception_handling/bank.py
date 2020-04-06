class BankAccount():

    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        """Add money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will increase
        """
        try:
            self.balance += amount
            return self.balance
        except TypeError:
            print('(Error): The add_money method requires a numeric value')
            

    def withdraw_money(self, amount):
        """Withdraw money to a bank account

        Arguments:
          amount - A numerical value by which the bank account's balance will decrease
        """
        try:
            if amount < self.balance:
                self.balance -= amount
                return self.balance
            else:
                print(f"You cannot withdraw ${amount}. You only have ${self.balance} in your account")
        except TypeError:
            print('(Error): The withdraw_money method requires a numeric value')
            


bank = BankAccount()

bank.add_money(50)
bank.withdraw_money(60)
bank.withdraw_money("60")

print(bank.balance)
