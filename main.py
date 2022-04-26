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
        return str("The winner is Player " + str(winner) + "!")

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
        userIn1 = input('>')
        if(userIn1 == "e"):
            play = False
            return -1
        elif(userIn1 == "s"):
            while run == True:
                print("Press:\n- f for a single round\n- r for 100 rounds\n- a for full game\n- x to exit")
                userIn2 = input('>>')
                if userIn2 == "f":
                    if player1.hand and player2.hand:
                        battle = Battle(player1, player2)
                        battle.fight()
                    elif not player1.hand:
                        return 2
                    elif not player2.hand:
                        return 1
                elif userIn2 == "r":
                    for i in range(100):
                        if player1.hand and player2.hand:
                            battle = Battle(player1, player2)
                            battle.fight()
                        elif not player1.hand:
                            return 2
                        elif not player2.hand:
                            return 1
                elif userIn2 == "a":
                    count = 0
                    while run:
                        if (count % 26) == 0:
                            player1.shuffleHand()
                            player2.shuffleHand()
                            print("Hands reshuffled, 26th round in sequence")
                        else:
                            pass

                        print("Round: " + str(count))
                        if player1.hand and player2.hand:
                            battle = Battle(player1, player2)
                            battle.fight()
                            count+=1
                        elif not player1.hand:
                            print("The game automatically ran for " + str(count) + " rounds")
                            return 2
                        elif not player2.hand:
                            print("The game automatically ran for " + str(count) + " rounds")
                            return 1
                elif userIn2 == "x":
                    run == False
                    return -1
                else:
                    print("Not a command")
        else:
            print("Not a command")

if __name__ == "__main__":
    main()