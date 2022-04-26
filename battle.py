from cards import Card
from player import Player
import unittest

class Battle:
    def __init__(self, player1in, player2in):
        self.player1 = player1in
        self.player2 = player2in

    def compare(self, card1, card2):
        if type(card1) == Card and type(card2) == Card:
            c1val = card1.getCardVal()
            c2val = card2.getCardVal()
            if c1val > c2val:
                return 1
            elif c1val < c2val:
                return 2
            elif c1val == c2val:
                return 3
        else:
            print("error return compare")
            return -1


    def printCardCount(self):
        strReturn = str(str(self.player1.countHand()) + " " + str(self.player2.countHand()))
        if self.player1.countHand() == 1:
            print("-Player 1 has " + str(self.player1.countHand()) + " card and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
            return strReturn
        elif self.player2.countHand() == 1:
            print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " card-" + "\n")             
            return strReturn
        else:
            print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
            return strReturn

    def fight(self):
        self.lastStand_standoff(False)   
        if self.player1.countHand() == 0:
            return 2
        elif self.player2.countHand() == 0:
            return 1
        else:
            pass

        turnP1 = self.player1.playCard()
        turnP2 = self.player2.playCard()
        print("Player 1 played: " + turnP1.seeCard())
        print("Player 2 played: " + turnP2.seeCard())
        result = self.compare(turnP1, turnP2)
        if(result == 1):
            print("Skirmish won by Player 1 with the higher card")
            self.player1.takeCard(turnP1)
            self.player1.takeCard(turnP2)
            self.printCardCount()
            return
        elif(result == 2):
            print("Skirmish won by Player 2 with the higher card")
            self.player2.takeCard(turnP1)
            self.player2.takeCard(turnP2)
            self.printCardCount()
            return
        elif(result == 3):
            print("This is war!")
            outcome = self.war()
            if(outcome == 1):
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
                print("Player 1 won the war!")
                self.printCardCount()
                return
            elif(outcome == 2):
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                print("Player 2 won the war!")
                self.printCardCount()
                return
        else:
            print("error during fight")


    def lastStand_standoff(self, isWar):
        if self.player1.countHand() == 1 or self.player2.countHand() == 1:
            if self.player1.countHand() == 1 and isWar == False:
                print("One card in player 1's hand, last stand!!")
            elif self.player2.countHand() == 1 and isWar == False:
                print("One card in player 2's hand, last stand!!")
            else:
                pass
            
            if isWar == True:
                print("Not enough cards for war, it's a standoff!")
            else:
                pass
            
            turnP1 = self.player1.playCard()
            turnP2 = self.player2.playCard()
            print("Player 1 played: " + turnP1.seeCard())
            print("Player 2 played: " + turnP2.seeCard())
            result = self.compare(turnP1, turnP2)
            if(result == 1):
                print("Standoff won by Player 1 with the higher card")
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
                self.printCardCount()
                return 1
            elif(result == 2):
                print("Standoff won by Player 2 with the higher card")
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                self.printCardCount()
                return 2
            elif(result == 3):
                print("Tie in standoff, there is no victor")
                self.player1.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                self.printCardCount()
                return 3

        elif not self.player1.hand:
            print("Player 1 bled out, war over")
            return 1
        elif not self.player2.hand:
            print("Player 2 bled out, war over")
            return 2

    def war(self):
        if self.player1.countHand() < 3 or self.player2.countHand() < 3:
            self.lastStand_standoff(True)
            return
        else:
            pass

        burnP1 = self.player1.playCard()
        burnP2 = self.player2.playCard()
        print("Player 1 burned: " + burnP1.seeCard())
        print("Player 2 burned: " + burnP2.seeCard())
        turnP1 = self.player1.playCard()
        turnP2 = self.player2.playCard()
        print("Player 1 played: " + turnP1.seeCard())
        print("Player 2 played: " + turnP2.seeCard())
        result = self.compare(turnP1, turnP2)
        if(result == 1):
            print("before war win for p1 hand" + str(self.player1.countHand()) + " :: p2 hand" + str(self.player2.countHand()))
            self.player1.takeCard(burnP1)
            self.player1.takeCard(burnP2)
            self.player1.takeCard(turnP1)
            self.player1.takeCard(turnP2)

            print("p1 took cards")
            return 1
        elif(result == 2):
            print("before war win for p2 hand" + str(self.player2.countHand()) + " :: p1 hand" + str(self.player1.countHand()))

            self.player2.takeCard(burnP1)
            self.player2.takeCard(burnP2)
            self.player2.takeCard(turnP1)
            self.player2.takeCard(turnP2)
            return 2
        elif(result == 3):
            print("War continues!")
            outcome = self.war()
            if outcome == 1:
                self.player1.takeCard(burnP1)
                self.player1.takeCard(burnP2)
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
            if outcome == 2:
                self.player2.takeCard(burnP1)
                self.player2.takeCard(burnP2)
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
            return outcome
        
