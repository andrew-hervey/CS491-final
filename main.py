from cards import Deck
from player import Player
from battle import Battle
import unittest

def main():
    player1 = Player()
    player2 = Player()
    deck = Deck()
    splitDeck(deck, player1, player2)
    winner = run(player1, player2)
    if winner == 1 or winner == 2:
        print("The winner is Player " + str(winner) + "!")

def splitDeck(deck, player1, player2):
    deck.shuffleDeck()
    deck.shuffleDeck()
    for i in range(26):
        player1.takeCard(deck.drawCard())
        player2.takeCard(deck.drawCard())
    

def run(player1, player2):
    run = True
    play = True

    while play == True:    
        print("Press s to start or e to exit")
        userIn = input('>')
        if(userIn == "e"):
            play = False
        elif(userIn == "s"):
            while run == True:
                print("Press:\n- f for a single round\n- r for 100 rounds\n- a for full game\n- x to exit")
                userIn = input('>')
                if(userIn == "f"):
                    if player1.hand and player2.hand:
                        battle = Battle(player1, player2)
                        battle.fight()
                    elif not player1.hand:
                        return 2
                    elif not player2.hand:
                        return 1
                elif(userIn == "r"):
                    for i in range(100):
                        if player1.hand and player2.hand:
                            battle = Battle(player1, player2)
                            battle.fight()
                        elif not player1.hand:
                            return 2
                        elif not player2.hand:
                            return 1
                elif(userIn == "a"):
                    count = 0
                    while run:
                        if player1.hand and player2.hand:
                            battle = Battle(player1, player2)
                            battle.fight()
                            count+=1
                        elif not player1.hand:
                            print("The game ran for " + str(count) + " rounds")
                            return 2
                        elif not player2.hand:
                            print("The game ran for " + str(count) + " rounds")
                            return 1
                elif(userIn == "x"):
                    run = False
                else:
                    print("Not a command")
        else:
            print("Not a command")




if __name__ == "__main__":
    main()

class Testing(unittest.TestCase):
    def testRunFunction(self):
        deck = Deck()
        player1 = Player(deck)
        player2 = Player()
        battle = Battle(player1, player2)
        outcome = battle.fight()
        self.assertEqual(outcome, 1)