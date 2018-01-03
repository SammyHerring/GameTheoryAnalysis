import sys
import numpy as np
#Dominant + Stupid Strategies Method Solution to find Nach Equilibrium

#Dominant Solution NB:
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.

#Multiple Nach Equilibrium Test Data
player12x2 = [[3, 8],
           [0, 4]]
player22x2 = [[3, 0],
           [8, 4]]

##difference2x2 = [[0, 0],
##              [0, 0]]

##dominant2x2 = [[0, 0],
##            [0, 0]]

#Matrices re-written in column-down format
player1 = [[7, 2, 3, 5],
           [7, 2, 90, 0],
           [7, 2, 3, 90],
           [7, 3, 3, 5]]

player2 = [[1, 1, 7, 4],
           [2, 90, 2, 2],
           [4, 4, 90, 4],
           [8, 0, 3, 5]]

#Dominant Strategy Matrices
difference = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

dominantResult = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

#Stupid Strategy Matrices and Variables
stupidPlayer1 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

stupidPlayer2 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

stupidResult = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

equilibriumFound = False

#Proposed method for producing entire solution checking for both dominant and stupid solutions.
def Main():
    differenceMethod(player1, player2, difference)
    differenceComparision()
    printMatrix(difference, "Difference Array", True)
    printMatrix(dominantResult, "Dominant Array", True)

    greaterThanMethod(player1, stupidPlayer1)
    greaterThanMethod(player2, stupidPlayer2)
    print("Game Theory Scenario Analyser")
    print("NB: Player Data Sets are entered by in a horizontal format\nrelative to their strategies.\n")
    
    printMatrix(player1, "Player 1 Data Set", True)
    printMatrix(player2, "Player 2 Data Set", True)

    print("Stupid Strategy Calculation")
    print("If you find that both players have a '0' Stupid Strategy Result this shows\na scenario where both players do not fail.\n")
    printMatrix(stupidPlayer1, "Stupid Strategy Player 1 Results", True)
    printMatrix(stupidPlayer2, "Stupid Strategy Player 2 Results", True)
    
    greaterThanComparision(player1, player2, stupidPlayer1, stupidPlayer2)
    
    #print("Stupid Strategies Bool Array: ", stupidResult)

    #NB: Task 3 Addition for potential saddle point calculation
    #probabilityCalculation()
    #probabilityComparision()
    
    #completeComparision()
    #result()
    end()

#Finds Dominant Intersection through Difference Calculations
def differenceMethod(player1, player2, difference):
    for x in range(len(player1 and player2)):
        for y in range(len(player1 and player2)):
            difference[x][y] = abs((player1[x][y])-(player2[x][y]))

def differenceComparision():
    for x in range(len(player1 or player2)):
        for y in range(len(player1 or player2)):
            
            print("([{0}][{1}])".format(x,y))
            try: 
                if (difference[x][y] == difference[x][y+1]):
                    dominantResult[x][y] = 1
                    print("([{0}][{1}]): True".format(x,y))
                elif (difference[x][y] == difference[x+1][y]):
                    dominantResult[x][y] = 1
                    print("([{0}][{1}]): True".format(x,y))
                elif (difference[x][y] == difference[x+1][y+1]):
                    print("([{0}][{1}]): True".format(x,y))
                    dominantResult[x][y] = 1
                else:
                    print("([{0}][{1}]): False".format(x,y))
                    dominantResult[x][y] = 0
            except:
                pass

def greaterThanMethod(player, playerResult):
    for x in range(len(player)):
        for y in range(len(player)):
            for z in range(len(player)):
                #print(x,y,z)
                if player[x][z] < player[y][z]:
                    playerResult[x][z] = 1

def greaterThanComparision(player1, player2, playerResult1, playerResult2):
    #Find equilibrium by looking for matching 0 result values
    for x in range(len(playerResult1 and playerResult2)):
        for y in range(len(playerResult1 and playerResult2)):
            if playerResult1[x][y] == 0 and playerResult2[x][y] == 0:
                print("Nach Equilibrium Found at Index: [{0}][{1}] with the values '{2}' and '{3}' respectively.".format(x, y, player1[x][y], player2[x][y]))
                equilibriumFound = True

#Sub Procedures and Functions for UI elements
def printMatrix(matrix, title, newLine):
    print(title,":")
    print('\n'.join([''.join(['{:4}'.format(int(item)) for item in row]) for row in matrix]))
    if (newLine): print("")

def userConfirm(question): #Require the user to confirm a qustion and return a boolean result
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return userConfirm("Please confirm using yes or no")


def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
