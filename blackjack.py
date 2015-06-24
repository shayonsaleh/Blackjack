import random

class Card(object):
    """Standard playing card.
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    
    def __init__(self, suit=0, rank=1):
        if suit < 0 or suit > 3 or rank < 1 or rank > 13:
            raise ValueError('Suit must be 0-3 and rank 1-13')
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        """Returns card as string representation."""
        return '%s of %s' % (Card.ranks[self.rank - 1],
                             Card.suits[self.suit])
    
    def __cmp__(self, other):
        """Compares cards by suit and rank.
        
        Positive = this > other
        Negative = other > this
        0 = this == other
        """
        tup1 = self.suit, self.rank
        tup2 = other.suit, other.rank
        return cmp(tup1, tup2)
    
class Deck(object):
    """Standard playing card deck.
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                new_card = Card(suit, rank)
                self.cards.append(new_card)
    
    def __str__(self):
        rest_of_cards = []
        for card in self.cards:
            rest_of_cards.append(str(card))
        return '\n'.join(rest_of_cards)
    
    def add_card(self, card):
        """Adds card to deck."""
        self.cards.append(card)
        
    def add_deck(self, other_deck):
        """Adds all the cards from other deck."""
        self.cards.extend(other_deck.cards)
        
    def insert_card(self, card, index=0):
        """Insert card at given position. Add exceptions."""
        self.cards.insert(card, index)
        
    def remove_card(self, card):
        """Removes card to deck."""
        self.cards.remove(card)
        
    def draw_card(self, index=0):
        """Draw card from top of deck."""
        self.cards.pop(index)
        
    def find_card(self, card):
        """Return index of first match of card in deck."""
        return self.cards.index(card)
        
    def count_card(self, card):
        """Return number of times card appears in deck."""
        return self.cards.count(card)
        
    def shuffle(self):
        """Shuffle deck."""
        random.shuffle(self.cards)
        
    def sort(self):
        """Sorts the deck."""
        self.cards.sort()
    
        
class Hand(object):
    """Represents a player's hand."""
    
    def __init__(self, name=''):
        self.cards = []
        self.name = name
        
class Dealer(object):
    """Represents house. Shuffles, deals cards, and has a hand."""
    pass

if __name__ == '__main__':
    print "Hello World!"
