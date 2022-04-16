from cards import Card, Deck
import unittest
MAX_HAND = 7

class Player:
    def __init__(self):
        self.hand = []

    def takeCard(self, card):
        self.hand.append(card)

    def countHand(self):
        return len(self.hand)

    def flipCard(self):
        print(self.hand.seeCard())

    def playCard(self):
        # print("Player 1: " + self.flipCard())
        return self.hand.pop(0)