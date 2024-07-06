class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):

        #Initialize a new bank account with the given details.
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):

        #Adjust the interest rate for the account.
        self.interest_rate = new_rate

    def deposit(self, amount):

        #Deposit an amount into the account.
        if amount > 0:
            self.amount += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):

        #Withdraw an amount from the account.
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

    def get_balance(self):

        #Get the current balance of the account.
        return self.amount

    def calculate_interest(self, days):

        #Calculate the interest for a given number of days.
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):

        #Return a string representation of the account details.
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate}%"


# Test Function
def test_bank_acct():
    #Test the functionality of the BankAcct class.
    account = BankAcct("John Doe", "123456789", 1000.0, 5.0)
    print(account)

    account.deposit(500.0)
    print(f"After depositing $500, the balance is: ${account.get_balance():.2f}")

    account.withdraw(300.0)
    print(f"After withdrawing $300, the balance is: ${account.get_balance():.2f}")

    account.adjust_interest_rate(4.5)
    print(f"After adjusting the interest rate to 4.5%, the balance is: ${account.get_balance():.2f}")

    interest = account.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")


# Running the test function
test_bank_acct()