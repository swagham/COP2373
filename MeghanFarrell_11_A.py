import random


# Define the Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Define the Deck class
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        if num > len(self.cards):
            raise ValueError("Not enough cards left to deal")
        return [self.cards.pop() for _ in range(num)]


# Function to print a hand of cards
def print_hand(hand):
    for index, card in enumerate(hand):
        print(f"{index + 1}: {card}")


# Main game function
def poker_game():
    deck = Deck()
    hand = deck.deal(5)

    print("Your initial hand:")
    print_hand(hand)

    # Prompt the user to select cards to replace
    indices_to_replace = input("Enter the card numbers to replace (e.g., 1, 3, 5): ")
    indices_to_replace = [int(x) - 1 for x in indices_to_replace.split(',') if x.strip().isdigit()]

    # Replace the selected cards
    for index in indices_to_replace:
        if 0 <= index < len(hand):
            hand[index] = deck.deal(1)[0]

    print("\nYour new hand:")
    print_hand(hand)


# Run the game
poker_game()