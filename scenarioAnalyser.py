import sys
import numpy as np
#Dominant + Stupid Strategies Method Solution to find Nach Equilibrium

#Dominant Solution NB:
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.

#Multiple Nach Equilibrium Test Data to show Saddle Point Problem
player12x2 = [[3, 8],
              [0, 4]]
player22x2 = [[3, 0],
              [8, 4]]

difference2x2 = [[0, 0],
                 [0, 0]]

dominantResult2x2 = [[0, 0],
                     [0, 0]]

#Matrices re-written in column-down format
player1 = [[7, 2, 3, 5],
           [7, 2, 90, 0],
           [7, 2, 3, 90],
           [7, 3, 3, 5]]

player2 = [[1, 1, 7, 4],
           [2, 90, 2, 2],
           [4, 4, 90, 4],
           [8, 0, 3, 5]]

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
    print("\n--Program Start--\n")
    print("Game Theory Scenario Analyser")
    print("NB: Player Data Sets are entered by in a horizontal format\nrelative to their strategies.\n")
    
    printMatrix(player1, "Player 1 Data Set", True)
    printMatrix(player2, "Player 2 Data Set", True)

    print("Dominant Strategy Calculation")
    print("For 2x2 Matrices Only")
    differenceMethod(player12x2, player22x2, difference2x2)
    differenceComparision()
    printMatrix(difference2x2, "Difference Array", True)
    printMatrix(dominantResult2x2, "Dominant Array", True)

    print("Stupid Strategy Calculation")
    print("If you find that both players have a '0' Stupid Strategy Result this shows\na scenario where both players do not fail.\n")
    greaterThanMethod(player1, stupidPlayer1)
    greaterThanMethod(player2, stupidPlayer2)
    
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
            try: 
                if (difference[x][y] == difference[x][y+1]):
                    dominantResult[x][y] = 1
                elif (difference[x][y] == difference[x+1][y]):
                    dominantResult[x][y] = 1
                elif (difference[x][y] == difference[x+1][y+1]):
                    dominantResult[x][y] = 1
                else:
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

def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
