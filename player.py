from cards import Card, Deck
import unittest

class Player:
    def __init__(self, deck=[]):
        self.hand = []
        if isinstance(deck, type(Deck)):
            self.hand = deck
        else:
            print("Not a deck object")

    #adds card to bottom of stack
    def takeCard(self, card):
        self.hand.append(card)

    #returns amount of cards in hand
    def countHand(self):
        return len(self.hand)

    #pops card from top of stack
    def playCard(self):
        return self.hand.pop(0)

class Testing(unittest.TestCase):
    def testCreatePlayer(self):
        player = Player()
        self.assertIsNotNone(player)

    def testCountHandNoCards(self):
        player = Player()
        self.assertEqual(player.countHand(),0)  
    
    def testCountHandOneCard(self):
        player = Player()
        card = Card("Diamonds", 5)
        player.takeCard(card)
        self.assertEqual(player.countHand(),1)    

    def testPlayCardWorks(self):
        player = Player()
        card = Card("Diamonds", 5)
        player.takeCard(card)
        self.assertIsInstance(player.playCard(),Card)

    
