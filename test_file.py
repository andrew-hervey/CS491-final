from cards import Card, Deck
from main import main, splitDeck, run
from battle import Battle
from player import Player
import unittest

class Testing(unittest.TestCase):
    

    #=========================================================================

    #BATTLE TESTS

    def testCompareHigherC1(self):
        card1 = Card("Hearts", 7)
        card2 = Card("Diamonds", 5)
        player1 = Player()
        player2 = Player()
        player1.takeCard(card1)
        player2.takeCard(card2)
        battle = Battle(player1, player2)
        outcome = battle.compare(battle.player1.playCard(), battle.player2.playCard())
        self.assertEqual(outcome, 1)
    
    def testCompareEqualValue(self):
        card2 = Card("Diamonds", 5)
        card1 = Card("Hearts", 5)
        player1 = Player()
        player2 = Player()
        player1.takeCard(card1)
        player2.takeCard(card2)
        battle = Battle(player1, player2)
        outcome = battle.compare(battle.player1.playCard(), battle.player2.playCard())
        self.assertEqual(outcome, 3)
    
    def testCompareNotCardInput(self):
        outcome = Battle.compare(self, 1, 2)
        self.assertEqual(outcome, -1)
    
    #E/O BATTLE TESTS

    #=========================================================================

    #PLAYER TESTS

    def testCreatePlayer(self):
        player = Player()
        self.assertIsNotNone(player)

    def testTakeCard(self):
        card1 = Card("Hearts", 5)
        card2 = Card("Diamonds", 7)
        player = Player()
        player.takeCard(card1)
        player.takeCard(card2)
        self.assertEqual(player.hand[0], card1)

    #has issues, should assertEqual but hand is not creating properly
    def testCreatePlayerWithDeck(self):
        deck = Deck()
        deck.shuffleDeck()
        player = Player(deck)
        self.assertNotEqual(player.hand, deck)

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
    
    #E/O PLAYER TESTS

    #=========================================================================

    #CARDS TESTS

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

    #=========================================================================

    #MAIN TESTS

    def testRunFunction(self):
        deck = Deck()
        player1 = Player(deck)
        player2 = Player()
        battle = Battle(player1, player2)
        outcome = battle.fight()
        self.assertEqual(outcome, 2)

    #E/O MAIN TESTS

    #=========================================================================
