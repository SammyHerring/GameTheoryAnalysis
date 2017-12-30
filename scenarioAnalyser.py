import sys
import numpy as np
#Difference + Silly Strategies Method Solution to find Nach Equilibrium

#Dominant Solution NB:
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.

#Multiple Nach Equilibrium Test Data
player12x2 = [[3, 8],
           [0, 4]]
player22x2 = [[3, 0],
           [8, 4]]

#Matrices re-written in column-down format
player1 = [[7, 2, 3, 5],
           [7, 2, 90, 0],
           [7, 2, 3, 90],
           [7, 3, 3, 5]]

player2 = [[1, 1, 7, 4],
           [2, 90, 2, 2],
           [4, 4, 90, 4],
           [8, 0, 3, 5]]

difference = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
dominant = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

##difference = [[0, 0],
##              [0, 0]]
##dominant = [[0, 0],
##            [0, 0]]

sillyPlayer1 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

sillyPlayer2 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

sillyResult = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

#Proposed method for producing entire solution checking for both dominant and silly solutions.
def Main():
##    differenceMethod(player1, player2, difference)
##    differenceComparision()
##    print("Difference Array: ")
##    printMatrix(difference)
##    print("")
##    print("Dominant Array: ")
##    printMatrix(dominant)
##    print("")

    greaterThanMethod(player1, sillyPlayer1)
    greaterThanMethod(player2, sillyPlayer2)

    print("Player 1: ")
    printMatrix(player1)
    print("")
    print("Player 2: ")
    printMatrix(player2)
    print("")
    print("")
    print("Silly Player 1 Results: ")
    printMatrix(sillyPlayer1)
    print("")
    print("Silly Player 2 Results: ")
    printMatrix(sillyPlayer2)
    print("")
    
    greaterThanComparision(sillyPlayer1, sillyPlayer2)
    
    #print("Silly Strategies Bool Array: ", silly)

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
            #print("P1 ([{0}][{1}]): {2}".format(x,y,player1[x][y]))
            #print("P2 ([{0}][{1}]): {2}".format(x,y,player2[x][y]))
            #print("Difference: {0}".format(difference[x][y]))
            #print("Difference Array: ", difference) #If uncommented, show difference array progression through each iteration.
            #print("")

def differenceComparision():
    for x in range(len(player1 or player2)):
        for y in range(len(player1 or player2)):
            
            print("([{0}][{1}])".format(x,y))
            try: 
                if (difference[x][y] == difference[x][y+1]):
                    dominant[x][y] = 1
                    print("([{0}][{1}]): True".format(x,y))
                elif (difference[x][y] == difference[x+1][y]):
                    dominant[x][y] = 1
                    print("([{0}][{1}]): True".format(x,y))
                elif (difference[x][y] == difference[x+1][y+1]):
                    print("([{0}][{1}]): True".format(x,y))
                    dominant[x][y] = 1
                else:
                    print("([{0}][{1}]): False".format(x,y))
                    dominant[x][y] = 0
            except:
                pass
    

def greaterThanMethod(player, playerResult):
    for x in range(len(player)):
        for y in range(len(player)):
            for z in range(len(player)):
                #print(x,y,z)
                if player[x][z] < player[y][z]:
                    playerResult[x][z] = 1

def greaterThanComparision(playerResult1, playerResult2):
    #Find equilibrium by looking for matching 0 result values
    for x in range(len(playerResult1 and playerResult2)):
        for y in range(len(playerResult1 and playerResult2)):
            if playerResult1[x][y] == 0 and playerResult2[x][y] == 0:
                print("Nach Equilibrium Found: ", x,y)
    return

#Sub Procedures and Functions for UI elements
def printMatrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

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
