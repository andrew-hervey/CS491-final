from cards import Card, Deck
import unittest
MAX_HAND = 7

class Player:
    def __init__(self):
        self.hand = []

    #adds card to bottom of stack
    def takeCard(self, card):
        self.hand.append(card)

    #returns amount of cards in hand
    def countHand(self):
        return len(self.hand)

    #prints card name and number
    def flipCard(self):
        print(self.hand.seeCard())

    #pops card from top of stack
    def playCard(self):
        return self.hand.pop(0)

class Testing(unittest.TestCase):
    def testCreatePlayer(self):
        player = Player()
        self.assertIsNotNone(player)

    def testCountHand(self):
        player = Player()
        card = Card("Diamonds", 5)
        player.takeCard(card)
        self.assertEqual(player.countHand(),1)    

    def testPlayCard(self):
        player = Player()
        card = Card("Diamonds", 5)
        player.takeCard(card)
        self.assertIsInstance(player.playCard(),Card)