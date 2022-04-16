import unittest

class Battle:
    def __init__(self, player1in, player2in):
        self.player1 = player1in
        self.player2 = player2in

    def compare(self, card1, card2):
        card1Val = card1.getCardVal()
        card2Val = card2.getCardVal()
        if card1Val > card2Val:
            return 1
        if card2Val > card1Val:
            return 2
        if card1Val == card2Val:
            return 3

    def fight(self):
        turnP1 = self.player1.playCard()
        turnP2 = self.player2.playCard()
        print("Player 1 played: " + turnP1.seeCard())
        print("Player 2 played: " + turnP2.seeCard())
        result = self.compare(turnP1, turnP2)
        if(result == 1):
            print("Skirmish won by Player 1 with the higher card")
            self.player1.takeCard(turnP1)
            self.player1.takeCard(turnP2)
            print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
        elif(result == 2):
            print("Skirmish won by Player 2 with the higher card")
            self.player2.takeCard(turnP1)
            self.player2.takeCard(turnP2)
            print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
        elif(result == 3):
            print("This is war!")
            outcome = self.war()
            if(outcome == 1):
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
                print("Player 1 won the war!")
                print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
            elif(outcome == 2):
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                print("Player 2 won the war!")
                print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
    
    def war(self):
        if len(self.player1.hand) == 1 or len(self.player2.hand) == 1:
            print("Not enough cards for war, it's a standoff!")
            turnP1 = self.player1.playCard()
            turnP2 = self.player2.playCard()
            print("Player 1 played: " + turnP1.seeCard())
            print("Player 2 played: " + turnP2.seeCard())
            result = self.compare(turnP1, turnP2)
            if(result == 1):
                print("Standoff won by Player 1 with the higher card")
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
                print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
                return 1
            elif(result == 2):
                print("Standoff won by Player 2 with the higher card")
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                print("-Player 1 has " + str(self.player1.countHand()) + " cards and Player 2 has " + str(self.player2.countHand()) + " cards-" + "\n")
                return 2
        if not self.player1.hand:
            print("Player 1 bled out, war over")
            return 0
        if not self.player2.hand:
            print("Player 2 bled out, war over")
            return 0

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
            #print("before war win for p1 hand" + str(self.player1.countHand()) + " :: p2 hand" + str(self.player2.countHand()))
            self.player1.takeCard(burnP1)
            self.player1.takeCard(burnP2)
            self.player1.takeCard(turnP1)
            self.player1.takeCard(turnP2)

            #print("p1 took cards")
            return 1
        elif(result == 2):
            #print("before war win for p2 hand" + str(self.player2.countHand()) + " :: p1 hand" + str(self.player1.countHand()))
            self.player2.takeCard(burnP1)
            self.player2.takeCard(burnP2)
            self.player2.takeCard(turnP1)
            self.player2.takeCard(turnP2)
            #print("p2 took cards")
            return 2
        elif(result == 3):
            print("War continues!")
            # for i in range(5):
            #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            outcome = self.war()
            if outcome == 1:
                #print("before war win for p1 hand" + str(self.player1.countHand()) + " :: p2 hand" + str(self.player2.countHand()))
                self.player1.takeCard(burnP1)
                self.player1.takeCard(burnP2)
                self.player1.takeCard(turnP1)
                self.player1.takeCard(turnP2)
                #print("after war win for p1 hand" + str(self.player1.countHand()) + " :: p2 hand" + str(self.player2.countHand()))
            if outcome == 2:
                #print("before war win for p2 hand" + str(self.player2.countHand()) + " :: p1 hand" + str(self.player1.countHand()))
                self.player2.takeCard(burnP1)
                self.player2.takeCard(burnP2)
                self.player2.takeCard(turnP1)
                self.player2.takeCard(turnP2)
                #print("after war win for p2 hand" + str(self.player2.countHand()) + " :: p1 hand" + str(self.player1.countHand()))
            return outcome
        
