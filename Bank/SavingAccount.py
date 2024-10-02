from bank import BankAccount

class SavingAccount(BankAccount):
    def __int__(self, name, current_balance, minimum_balance, interest_rate):
        super().__init__(name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * (self.interest_rate * 100)
        self.deposit(interest)
        print(f"Applied Interest: ${interest:.2f}")
        print(f"New Balance: ${self.current_balance:.2f}")