import random

class Card:
    """
    Represents a playing card with a suit and rank.
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠", "♥", "♣", "♦"]

    def __init__(self, suit, rank):
        """
        Initialize a Card with a suit and rank.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit  # private attribute for suit
        self._rank = rank  # private attribute for rank

    def __eq__(self, other):
        """
        Compare if two cards have the same rank.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare two cards based on their rank's position in RANKS.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Return a string representation like 'Q♣'.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Return a string representation for debugging.
        """
        return self.__str__()

    @property
    def rank(self):
        """
        Getter for rank.
        """
        return self._rank

class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        """
        Initialize a full deck of 52 cards.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Return string version of the entire deck.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffle the deck randomly.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deal (pop) one card from the top of the deck.
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)          # print unshuffled deck
    deck.shuffle()
    print(deck)          # print shuffled deck
    print(deck.deal())   # deal the top card

# Example of manual card creation:
# jack_clubs = Card("♠", "J")
# print(jack_clubs)
