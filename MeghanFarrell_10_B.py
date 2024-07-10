from decimal import Decimal, ROUND_DOWN

class Money:

    #Class for money operations.
    def __init__(self, dollars=0, cents=0):

        #Initialize with dollars and cents.
        self.total_cents = Decimal(dollars) * 100 + Decimal(cents)

    @property
    def dollars(self):

        #Get the dollar part of the currency.
        return self.total_cents // 100

    @property
    def cents(self):

        #Get the cent part of the currency.
        return self.total_cents % 100

    def __add__(self, other):

        #Add two Money objects.
        if isinstance(other, Money):
            return Money(cents=self.total_cents + other.total_cents)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Money' and '{type(other).__name__}'")

    def __sub__(self, other):

        #Subtract one Money object from another.
        if isinstance(other, Money):
            return Money(cents=self.total_cents - other.total_cents)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Money' and '{type(other).__name__}'")

    def __mul__(self, other):

        #Multiply a Money object by an integer or float.
        if isinstance(other, (int, float)):
            return Money(cents=(self.total_cents * Decimal(other)).quantize(Decimal('0.01'), rounding=ROUND_DOWN))
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Money' and '{type(other).__name__}'")

    def __str__(self):

        #String representation of the currency.
        return "${}.{:02d}".format(int(self.dollars), int(self.cents))


class BankAcct(Money):

    #Class for bank account operations, inheriting from Money.
    def __init__(self, name, account_number, dollars=0, cents=0, interest_rate=0.0):

        #Initialize a new bank account with the given details.
        super().__init__(dollars, cents)
        self.name = name
        self.account_number = account_number
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):

        #Adjust the interest rate for the account.
        self.interest_rate = new_rate

    def deposit(self, amount):

        #Deposit an amount into the account.
        if amount.total_cents > 0:
            self.total_cents += amount.total_cents
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):

        #Withdraw an amount from the account.
        if amount.total_cents > 0 and amount.total_cents <= self.total_cents:
            self.total_cents -= amount.total_cents
        else:
            raise ValueError("Invalid withdrawal amount")

    def get_balance(self):

        #Get the current balance of the account.
        return Money(cents=self.total_cents)

    def calculate_interest(self, days):

        #Calculate the interest for a given number of days.
        interest_amount = self.total_cents * Decimal(self.interest_rate / 100) * Decimal(days / 365)
        return Money(cents=interest_amount.quantize(Decimal('0.01'), rounding=ROUND_DOWN))

    def __str__(self):

        #Return a string representation of the account details.
        return (f"Account Name: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: {self}\n"
                f"Interest Rate: {self.interest_rate}%")

def test_bank_acct():

    #Test the functionality of the BankAcct class.
    account = BankAcct("John Doe", "123456789", 10, 0, 5.0)
    print(account)

    deposit_amount = Money(5, 0)
    account.deposit(deposit_amount)
    print(f"After depositing $5.00, the balance is: {account.get_balance()}")

    withdraw_amount = Money(3, 0)
    account.withdraw(withdraw_amount)
    print(f"After withdrawing $3.00, the balance is: {account.get_balance()}")

    account.adjust_interest_rate(4.5)
    print(f"After adjusting the interest rate to 4.5%, the balance is: {account.get_balance()}")

    interest = account.calculate_interest(30)
    print(f"Interest for 30 days: {interest}")

# Run the test function
test_bank_acct()