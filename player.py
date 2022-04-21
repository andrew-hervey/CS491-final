from cards import Card, Deck
import unittest
import random

class Player:
    def __init__(self, deck=[]):
        if not isinstance(deck, type(Deck)):
            self.hand = []
            return
        else:
            self.hand = deck
            return

    #adds card to bottom of stack
    def takeCard(self, card):
        self.hand.append(card)

    #returns amount of cards in hand
    def countHand(self):
        return len(self.hand)

    #pops card from top of stack
    def playCard(self):
        return self.hand.pop(0)

    def shuffleHand(self):
        for i in range(len(self.hand) - 1, 0, -1):
            rand = random.randint(0, i)
            self.hand[i], self.hand[rand] = self.hand[rand], self.hand[i]


    
