class BankAccount:

    def __init__(self, balance):
        self.balance = balance


    def _add_money_(self, amount):
        self.balance += amount

    def _extract_money_(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def _extract_money_(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("\n----🔴 Does not have sufficient funds to carry out the operation----")
        super()._extract_money_(amount)


class AccountBalance:

    @staticmethod
    def print_Status(BankAccount):
        print("\n ====The balance of the Account is 💲", BankAccount.balance )
        print("\n")


ba = SavingsAccount(balance = 0, min_balance = 500)


ba._add_money_(3500)
ba._add_money_(9000)

try:
    ba._extract_money_(10000)
    ba._extract_money_(20000)

except ValueError as e:
    print(e)

AccountBalance = AccountBalance()
AccountBalance.print_Status(ba)

