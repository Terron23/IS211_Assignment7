
import random
import sys


#Die class creates the die object and seeds to 0.
class Die():
    def __init__(self):
        self.value = 0

    #Method to roll the die returning a random int between 1 and 6
    def roll(self):
        self.value = random.randint(1,6)


#Player class creates player object and function for the decision the player makes to roll or hold.
class Player():
    def __init__(self):
        self.turn = False
        self.roll = True
        self.hold = False
        self.score = 0


    #Method allows player to enter r or h and then sets the corresponding player attribute.  Catches invalid entry.
    def Hold_or_Roll(self):
        print('Enter "h" to HOLD or "r" to ROLL? ')
        question = input()
        print(question)
        if question.lower() == 'h':
            self.hold = True
            self.roll = False

        elif question.lower() == 'r':
            self.hold = False
            self.roll = True

        else:
            print('Invalid.  Enter "h" or "r".')
            self.Hold_or_Roll()


#Game class executes the game for exactly 2 players and keeps score for the round and the total game score.
class Game():
    def __init__(self, player1, player2, die):
        self.turn_score = 0
        self.die = die
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = "P1"
        self.player2.name = "P2"


        #Selects a random player to start the game and then calls the turn method.
        print("A RANDOM PLAYER WILL BE SELECTED TO START")
        choose_player = random.randint(1, 2)
        if choose_player == 1:
            self.current_player = player1
            
            print("P1 STARTS GAME.")
        elif choose_player == 2:
            self.current_player = player2
            print("\n")
            print("P2 STARTS GAME")
        self.turn()


    #Method executes the 'turn' by rolling the die and adding scores or switching to next player if 1 is rolled.
    def turn(self):
        self.die.roll()  #Rolls the die.

        if (self.die.value == 1):       #For rolls = 1, output and then call score_card
            print("YOU ROLLED A 1. NO POINTS AWARDED. NEXT PLAYER ROLLS")
            print("P1 TOTAL GAME SCORE:", self.player1.score)
            print("P2 TOTAL GAME SCORE", self.player2.score)
            self.turn_score = 0
            self.score_card()

        else:
            self.turn_score = self.turn_score + self.die.value      #For value > 1, sum the turn scores with die value.

            print("You rolled a:", self.die.value)
            print("Your turn score is", self.turn_score)
            print ("P1 TOTAL GAME SCORE:", self.player1.score)
            print ("P2 TOTAL GAME SCORE:", self.player2.score)

            self.current_player.Hold_or_Roll()      #Calls method to decide whether to hold or roll

            if (self.current_player.hold == True and self.current_player.roll == False): #Player selected hold
                self.current_player.score = self.current_player.score + self.turn_score   #Scores added to total
                self.score_card()                                                 #Resets turn score and checks totals

            elif (self.current_player.hold == False and self.current_player.roll == True): #Player is rolling
                self.turn()                                               #Calls this turn method to keep rolling.

    #Method resets turn score, ends the game or toggles between players if no one has scored 100 points
    def score_card(self):
        self.turn_score = 0
        if self.player1.score >= 100:
            print ("P1 WINS")
            print ("Score:", self.player1.score)
            self.endgame()

        elif self.player2.score >= 100:
            print ("P2 WINS")
            print ("Score:", self.player2.score)
            self.endgame()

        #Toggles between players if no winner and sets player as current player for the round.
        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            print ("\n")
            print (self.current_player.name, "IS NOW PLAYING")
            self.turn()

    #Method ends game when a player has scored 100 points.
    def endgame(self):
        sys.exit()

#Main function instantiates 2 players, one die and one game objects.
def main():
    player1 = Player()
    player2 = Player()
    die = Die()
    Game(player1, player2, die)



if __name__ == '__main__':
    main()