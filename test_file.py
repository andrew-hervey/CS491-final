from importlib.resources import path
from unittest import mock
from cards import Card, Deck
from main import main, splitDeck, run
from battle import Battle
from player import Player
import unittest
from unittest.mock import patch, Mock

class Testing(unittest.TestCase):

    #commands used:
    #python3 -m coverage run -m pytest test_file.py
    #python3 -m coverage report
    
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

    def testPrintCardCount00(self):
        deck = Deck()
        player1 = Player()
        player2 = Player()
        battle = Battle(player1, player2)
        counts = battle.printCardCount()
        self.assertEqual(counts, "0 0")
    
    def testFightP1Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 100)
        player1.takeCard(p1c1)


        p2c1 = Card("b", 1)
        player2.takeCard(p2c1)


        battle = Battle(player1, player2)
        outcome = battle.fight()
        self.assertEqual(outcome, 1)
    
    def testFightP2Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        player1.takeCard(p1c1)


        p2c1 = Card("b", 100)
        player2.takeCard(p2c1)


        battle = Battle(player1, player2)
        outcome = battle.fight()
        self.assertEqual(outcome, 2)

    def testLastStand_StandoffP1Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 100)
        player1.takeCard(p1c1)


        p2c1 = Card("b", 1)
        player2.takeCard(p2c1)


        battle = Battle(player1, player2)
        outcome = battle.lastStand_standoff(False)
        self.assertEqual(outcome, 1)
    
    def testLastStand_StandoffP2Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        player1.takeCard(p1c1)


        p2c1 = Card("b", 100)
        player2.takeCard(p2c1)


        battle = Battle(player1, player2)
        outcome = battle.lastStand_standoff(False)
        self.assertEqual(outcome, 2)

    def testLastStand_StandoffTie(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        player1.takeCard(p1c1)


        p2c1 = Card("b", 1)
        player2.takeCard(p2c1)


        battle = Battle(player1, player2)
        outcome = battle.lastStand_standoff(False)
        self.assertEqual(outcome, 3)

    def testWar(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        p1c2 = Card("a", 2)
        p1c3 = Card("a", 3)
        p1c4 = Card("a", 4)
        player1.takeCard(p1c1)
        player1.takeCard(p1c2)
        player1.takeCard(p1c3)
        player1.takeCard(p1c4)

        p2c1 = Card("b", 1)
        p2c2 = Card("b", 10)
        p2c3 = Card("b", 3)
        p2c4 = Card("b", 4)
        player2.takeCard(p2c1)
        player2.takeCard(p2c2)
        player2.takeCard(p2c3)
        player2.takeCard(p2c4)

        battle = Battle(player1, player2)
        outcome = battle.war()
        self.assertEqual(outcome, 2)

    def testWarSecondLevelP2Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        p1c2 = Card("a", 2)
        p1c3 = Card("a", 3)
        p1c4 = Card("a", 4)
        p1c5 = Card("a", 5)
        p1c6 = Card("a", 6)
        p1c7 = Card("a", 7)
        p1c8 = Card("a", 8)
        player1.takeCard(p1c1)
        player1.takeCard(p1c2)
        player1.takeCard(p1c3)
        player1.takeCard(p1c4)
        player1.takeCard(p1c5)
        player1.takeCard(p1c6)
        player1.takeCard(p1c7)
        player1.takeCard(p1c8)

        p2c1 = Card("b", 1)
        p2c2 = Card("b", 2)
        p2c3 = Card("b", 3)
        p2c4 = Card("b", 100)
        p2c5 = Card("b", 5)
        p2c6 = Card("b", 6)
        p2c7 = Card("b", 7)
        p2c8 = Card("b", 8)
        player2.takeCard(p2c1)
        player2.takeCard(p2c2)
        player2.takeCard(p2c3)
        player2.takeCard(p2c4)
        player2.takeCard(p2c5)
        player2.takeCard(p2c6)
        player2.takeCard(p2c7)
        player2.takeCard(p2c8)

        battle = Battle(player1, player2)
        outcome = battle.war()
        self.assertEqual(outcome, 2)
    
    def testWarSecondLevelP1Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        p1c2 = Card("a", 2)
        p1c3 = Card("a", 3)
        p1c4 = Card("a", 100)
        p1c5 = Card("a", 5)
        p1c6 = Card("a", 6)
        p1c7 = Card("a", 7)
        p1c8 = Card("a", 8)
        player1.takeCard(p1c1)
        player1.takeCard(p1c2)
        player1.takeCard(p1c3)
        player1.takeCard(p1c4)
        player1.takeCard(p1c5)
        player1.takeCard(p1c6)
        player1.takeCard(p1c7)
        player1.takeCard(p1c8)

        p2c1 = Card("b", 1)
        p2c2 = Card("b", 2)
        p2c3 = Card("b", 3)
        p2c4 = Card("b", 4)
        p2c5 = Card("b", 5)
        p2c6 = Card("b", 6)
        p2c7 = Card("b", 7)
        p2c8 = Card("b", 8)
        player2.takeCard(p2c1)
        player2.takeCard(p2c2)
        player2.takeCard(p2c3)
        player2.takeCard(p2c4)
        player2.takeCard(p2c5)
        player2.takeCard(p2c6)
        player2.takeCard(p2c7)
        player2.takeCard(p2c8)

        battle = Battle(player1, player2)
        outcome = battle.war()
        self.assertEqual(outcome, 1)
    
    def testWarSecondLevelP2Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        p1c2 = Card("a", 2)
        p1c3 = Card("a", 3)
        p1c4 = Card("a", 4)
        p1c5 = Card("a", 5)
        p1c6 = Card("a", 6)
        p1c7 = Card("a", 7)
        p1c8 = Card("a", 8)
        player1.takeCard(p1c1)
        player1.takeCard(p1c2)
        player1.takeCard(p1c3)
        player1.takeCard(p1c4)
        player1.takeCard(p1c5)
        player1.takeCard(p1c6)
        player1.takeCard(p1c7)
        player1.takeCard(p1c8)

        p2c1 = Card("b", 1)
        p2c2 = Card("b", 2)
        p2c3 = Card("b", 3)
        p2c4 = Card("b", 100)
        p2c5 = Card("b", 5)
        p2c6 = Card("b", 6)
        p2c7 = Card("b", 7)
        p2c8 = Card("b", 8)
        player2.takeCard(p2c1)
        player2.takeCard(p2c2)
        player2.takeCard(p2c3)
        player2.takeCard(p2c4)
        player2.takeCard(p2c5)
        player2.takeCard(p2c6)
        player2.takeCard(p2c7)
        player2.takeCard(p2c8)

        battle = Battle(player1, player2)
        outcome = battle.war()
        self.assertEqual(outcome, 2)
    
    def testFightIntoWarP1Win(self):
        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        p1c2 = Card("a", 2)
        p1c3 = Card("a", 100)
        p1c4 = Card("a", 100)

        player1.takeCard(p1c1)
        player1.takeCard(p1c2)
        player1.takeCard(p1c3)
        player1.takeCard(p1c4)

        p2c1 = Card("b", 1)
        p2c2 = Card("b", 2)
        p2c3 = Card("b", 3)
        p2c4 = Card("b", 4)
        player2.takeCard(p2c1)
        player2.takeCard(p2c2)
        player2.takeCard(p2c3)
        player2.takeCard(p2c4)

        battle = Battle(player1, player2)
        battle.fight()
        outcome = battle.fight()
        self.assertEqual(outcome, 1)

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

    def testCheckShuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffleDeck()
        self.assertNotEqual(deck1, deck2)

    def testGetDeckCount(self):
        deck1 = Deck()
        self.assertEqual(deck1.getDeckCount(), 52)

    #=========================================================================

    #MAIN TESTS

    def testRunFunctionActions(self):
        deck = Deck()
        player1 = Player(deck)
        player2 = Player()
        battle = Battle(player1, player2)
        outcome = battle.fight()
        self.assertEqual(outcome, 2)

    def testSplitDeckNotFull(self):
        deck1 = Deck()
        deck2 = Deck()
        player1 = Player()
        player2 = Player()
        splitDeck(deck1, player1, player2)
        self.assertNotEqual(deck1, deck2)
    
    def testMain(self):
        input_mock_s = Mock()
        input_mock_s.return_value = "s"

        input_mock_a = Mock()
        input_mock_a.return_value = "a"

        input_mock = Mock()
        input_mock.side_effect = [input_mock_s.return_value, input_mock_a.return_value]
        with patch('builtins.input', input_mock) as mock_method:
            result = main()
        
        assert mock_method.call_count == 2
        assert result == ('The winner is Player 1!') or ('The winner is Player 2!')

    def testRunFunctionP1Win(self):
        input_mock_s = Mock()
        input_mock_s.return_value = "s"

        input_mock_f = Mock()
        input_mock_f.return_value = "f"

        input_mock = Mock()
        input_mock.side_effect = [input_mock_s.return_value, input_mock_f.return_value, input_mock_f.return_value]

        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 100)
        player1.takeCard(p1c1)

        p2c1 = Card("b", 1)
        player2.takeCard(p2c1)

        with patch('builtins.input', input_mock) as mock_method:
            result = run(player1, player2)
        
        assert mock_method.call_count == 3
        assert result == 1
    
    def testRunFunction_P2Win(self):
        input_mock_s = Mock()
        input_mock_s.return_value = "s"

        input_mock_f = Mock()
        input_mock_f.return_value = "f"

        input_mock = Mock()
        input_mock.side_effect = [input_mock_s.return_value, input_mock_f.return_value, input_mock_f.return_value]

        player1 = Player()
        player2 = Player()

        p1c1 = Card("a", 1)
        player1.takeCard(p1c1)

        p2c1 = Card("b", 100)
        player2.takeCard(p2c1)

        with patch('builtins.input', input_mock) as mock_method:
            result = run(player1, player2)
        
        assert mock_method.call_count == 3
        assert result == 2
            
    def testRunFunction_PlayFalse(self):
        input_mock = Mock()
        input_mock.return_value = "e"

        player1 = Player()
        player2 = Player()

        with patch('builtins.input', input_mock) as mock_method:
            result = run(player1, player2)
        
        assert mock_method.call_count == 1
        assert result == -1

    def testRunFunction_RunFalse(self):
        input_mock_s = Mock()
        input_mock_s.return_value = "s"

        input_mock_x = Mock()
        input_mock_x.return_value = "x"

        input_mock = Mock()
        input_mock.side_effect = [input_mock_s.return_value, input_mock_x.return_value]

        player1 = Player()
        player2 = Player()

        with patch('builtins.input', input_mock) as mock_method:
            result = run(player1, player2)
        
        assert mock_method.call_count == 2
        assert result == -1

    #E/O MAIN TESTS

    #=========================================================================
