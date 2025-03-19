from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):


        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

deck = Deck()
deck.shuffle()
hand = PokerHand(deck)
print(hand)

