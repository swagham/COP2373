from decimal import Decimal

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


def test_money_operations():

    #Test function for Money class operations.
    m1 = Money(10, 25)  # $10.25
    m2 = Money(5, 50)   # $5.50

    # Addition
    m3 = m1 + m2
    print(f"Addition: {m1} + {m2} = {m3}")

    # Subtraction
    m4 = m1 - m2
    print(f"Subtraction: {m1} - {m2} = {m4}")

    # Multiplication
    m5 = m1 * 2
    print(f"Multiplication: {m1} * 2 = {m5}")


# Run the test function
test_money_operations()