# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'


class Card(object):
    ''' Represents a standard playing card. '''

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # ranks are the same... it's a tie
        return 0


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)


class Hand(Deck):
    ''' Represents a hand of playing cards. '''

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


hand = Hand('new hand')
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print hand