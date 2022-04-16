import unittest
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def seeCard(self):
        if(self.value == 11):
            return str("Jack of " + str(self.suit))
        elif(self.value == 12):
            return str("Queen of " + str(self.suit))
        elif(self.value == 13):
            return str("King of " + str(self.suit))
        elif(self.value == 1):
            return str("Ace of " + str(self.suit))
        else:
            return str(str(self.value) + " of " + str(self.suit))

    def getCardVal(self):
        return self.value

    def getCardSuit(self):
        return self.suit

    # def setCardVal(self,val):
    #     print("value set")
    #     self.value = val

class Deck:
    def __init__(self):
        self.cards = []
        self.newDeck()

    def newDeck(self):
        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for num in range(1,14):
                self.cards.append(Card(suit,num))

    def shuffleDeck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def drawCard(self):
        return self.cards.pop(0)


class Testing(unittest.TestCase):
    def testCardCreationValue(self):
        card = Card("Diamonds", 5)
        self.assertEqual(5, card.getCardVal())

    def testCardCreationSuit(self):
        card = Card("Diamonds", 5)
        self.assertEqual("Diamonds", card.getCardSuit())

    def testSeeCard(self):
        card = Card("Diamonds", 5)
        self.assertEqual("5 of Diamonds", card.seeCard())

    def checkShuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffleDeck()
        self.assertNotEqual(deck1, deck2)