from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        """
        Deal a 5-card poker hand from the deck.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards  # store the dealt cards

    @property
    def cards(self):
        """
        Return the list of cards in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Return string representation of the hand.
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if all cards have the same suit.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Check if hand is a full house (3 of a kind + a pair).
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Count total number of rank matches in the hand.
        Pair = 2, Two pair = 4, Trips = 6, Full House = 8, Quads = 12.
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if the hand has exactly one pair.
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Check if the hand has exactly two pairs.
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Check if the hand has three cards of the same rank.
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Check if the hand has four cards of the same rank.
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (5 consecutive ranks).
        """
        self.cards.sort()  # relies on Card.__gt__ for sorting
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

# Simulate to estimate straight probability
count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    print(hand)
    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a straight is {100 * matches / count}%")
