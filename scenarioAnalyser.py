import sys
import numpy as np
#Difference Method Solution to find Nach Equilibrium
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.

#Multiple Nach Equilibrium Test
##player1 = [[3, 8],
##           [0, 4]]
##player2 = [[3, 0],
##           [8, 4]]

#Matrices re-written in column-down format
player1 = [[7, 2, 3, 5],
           [7, 2, 90, 0],
           [7, 2, 3, 90],
           [7, 3, 3, 5]]

player2 = [[1, 1, 7, 4],
           [2, 90, 2, 2],
           [4, 4, 90, 4],
           [8, 0, 3, 5]]

difference = [[0, 0],
              [0, 0]]
dominant = [[0, 0],
            [0, 0]]

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
    #differenceMethod()
    #differenceComparision()
    #print("Difference Array: ", difference)
    #print("Dominant Strategies Bool Array: ", dominant)
    
    #greaterThanMethod()

    greaterThanMethod2(player1, sillyPlayer1)
    greaterThanMethod2(player2, sillyPlayer2)
    print(sillyPlayer1)
    print(sillyPlayer2)
    
    #greaterThanComparision()
    #print("Silly Strategies Bool Array: ", silly)

    #NB: Task 3 Addition for potential saddle point calculation
    #probabilityCalculation()
    #probabilityComparision()
    
    #completeComparision()
    #result()
    end()

#Finds Dominant Intersection through Difference Calculations
def differenceMethod():
    for x in range(2):
        for y in range(2):
            difference[x][y] = abs((player1[x][y])-(player2[x][y]))
            #print(x)
            #print(y)
            print("P1 ([{0}][{1}]): {2}".format(x,y,player1[x][y]))
            print("P2 ([{0}][{1}]): {2}".format(x,y,player2[x][y]))
            print("Difference: {0}".format(difference[x][y]))
            #print("Difference Array: ", difference) #If uncommented, show difference array progression through each iteration.
            print("")

def differenceComparision():
##    for x in range(2):
##        for y in range(2):
##            if difference[x][y] == difference[x][y]:
##                dominant[x][y] = 1
##                return
##            else:
##                dominant[x][y] = 0
##                return

##    for x in range(2):
##        for y in range(2):
##            if difference[x][y] == difference[x][y+1]:
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##                return
##            elif difference[x][y] == difference[x+1][y]:
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##                return
##            elif difference[x][y] == difference[x+1][y+1]:
##                print("([{0}][{1}]): True".format(x,y))
##                dominant[x][y] = 1
##                return
##            else:
##                print("([{0}][{1}]): False".format(x,y))
##                dominant[x][y] = 0
##                return

##    for x in range(2):
##        for y in range(2):
##            print("([{0}][{1}])".format(x,y))
##            if not(y == 1):
##                if difference[x][y] == difference[x][y+1]:
##                    dominant[x][y] = 1
##                    print("([{0}][{1}]): True".format(x,y))
##                
##            elif not(x == 1):
##                if difference[x][y] == difference[x+1][y]:
##                    dominant[x][y] = 1
##                    print("([{0}][{1}]): True".format(x,y))
##                
##            elif not(x == 1 or y == 1):
##                if difference[x][y] == difference[x+1][y+1]:
##                    print("([{0}][{1}]): True".format(x,y))
##                    dominant[x][y] = 1
##                
##            else:
##                print("([{0}][{1}]): False".format(x,y))
##                dominant[x][y] = 0

##    for x in range(2):
##        for y in range(2):
##            print("([{0}][{1}])".format(x,y))
##            if (y != 1) and (difference[x][y] == difference[x][y+1]):
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##            elif (x != 1) and (difference[x][y] == difference[x+1][y]):
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##            elif (y != 1 and x != 1) and (difference[x][y] == difference[x+1][y+1]):
##                print("([{0}][{1}]): True".format(x,y))
##                dominant[x][y] = 1
##            else:
##                print("([{0}][{1}]): False".format(x,y))
##                dominant[x][y] = 0

##    for x in range(2):
##        for y in range(2):
##            print("([{0}][{1}])".format(x,y))
##            if (y != 1) and (difference[x][y] == difference[x][y+1]):
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##            elif (x != 1) and (difference[x][y] == difference[x+1][y]):
##                dominant[x][y] = 1
##                print("([{0}][{1}]): True".format(x,y))
##            elif (y != 1 and x != 1) and (difference[x][y] == difference[x+1][y+1]):
##                print("([{0}][{1}]): True".format(x,y))
##                dominant[x][y] = 1
##            else:
##                print("([{0}][{1}]): False".format(x,y))
##                dominant[x][y] = 0
    return

def greaterThanMethod():
    #both for whether player 1 and player 2 win OR by column as to whether your own reward is greater
    for x in range(len(player1)):
        for y in range(len(player1)):
            if player1[x][0] < player1[y][0]:
                sillyPlayer1[x][0] = 1
                
            if player1[x][1] < player1[y][1]:
                sillyPlayer1[x][1] = 1

            if player1[x][2] < player1[y][2]:
                sillyPlayer1[x][2] = 1

            if player1[x][3] < player1[y][3]:
                sillyPlayer1[x][3] = 1



            if player2[x][0] < player2[y][0]:
                sillyPlayer2[x][0] = 1

            if player2[x][1] < player2[y][1]:
                sillyPlayer2[x][1] = 1
                
            if player2[x][2] < player2[y][2]:
                sillyPlayer2[x][2] = 1
                
            if player2[x][3] < player2[y][3]:
                sillyPlayer2[x][3] = 1

    print(sillyPlayer1)
    print(sillyPlayer2)
    
    return

def greaterThanMethod2(player, playerResult):
        for x in range(len(player)):
            for y in range(len(player)):
                for z in range(len(player)):
                    if player[x][z] < player[y][z]:
                        playerResult[x][z] = 1

def greaterThanComparision():
    

#Find equilibrium by looking for matching 0 result values

#Sub Procedures for the System's UI elements in later development.
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
