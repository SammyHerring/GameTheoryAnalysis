import sys
#Dominant + Stupid Strategies Methods Solution to find Nach Equilibrium

#Dominant Strategy NB:
#To find a dominant solution with the goal to find the nach equilibrium, we may calculate the difference between players.
#When this difference is equal, a nach equilibrium has been found for that scenario.

#Stupid Strategy NB:
#Stupid Solutions are found by considering whether there are better payouts in other rows relative to the current value being considered.
#If there are no better values then the strategy is considered stupid and given a '1' value. Therefore, leaving any values with a remaining '0'
#to be considered non-stupid values. If there are '0' values in both players 'Stupid Strategy Results' then the Nach Equilibrium has been found.

#Multiple Nach Equilibrium Test Data to show Saddle Point Problem
player12x2 = [[3, 8],
              [0, 4]]
player22x2 = [[3, 0],
              [8, 4]]

difference2x2 = [[0, 0],
                 [0, 0]]

dominantResult2x2 = [[0, 0],
                     [0, 0]]

stupidPlayer12x2 = [[0, 0],
                    [0, 0]]

stupidPlayer22x2 = [[0, 0],
                    [0, 0]]

#Example Data Set posed in the assignment used for scenario 1
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

#Main Script from which other functions are called to complete processes
def Main():
    print("Game Theory Scenario Analyser")
    print("NB: Player Data Sets are entered by in a horizontal format\nrelative to their strategies.\n")

    selection = userConfirm("Select scenario to consider.\nEnter 1 for Example Posed or 2 for Saddle Point Example")
    if selection == 1:
            #Example Scenario given in Assignment solved using Silly Strategies
            print("Running Scenario for Example Posed in Assignment using Stupid Strategies")
            print("\n--Program Start--\n")
            printMatrix(player1, "Player 1 Data Set", True)
            printMatrix(player2, "Player 2 Data Set", True)
            
            print("NB: If you find that both players have a '0' Stupid Strategy Result this shows\na scenario where both players do not fail by having poor payouts.\nTherefore, where both players have a '0' we may identify the Nach Equilibrium.\n")

            greaterThanMethod(player1, stupidPlayer1)
            greaterThanMethod(player2, stupidPlayer2)
            
            printMatrix(stupidPlayer1, "Stupid Strategy Player 1 Results", True)
            printMatrix(stupidPlayer2, "Stupid Strategy Player 2 Results", True)

            greaterThanComparision(player1, player2, stupidPlayer1, stupidPlayer2)
            end()
    elif selection == 2:
            #Proof utilised in Task 3 to show Saddle Point and Nach Equilibrium using multiple strategies
            print("Running Scenario for Example Posed in Assignment using Stupid Strategies")
            print("\n--Program Start--\n")
            printMatrix(player12x2, "Player 1 Data Set", True)
            printMatrix(player22x2, "Player 2 Data Set", True)
            
            print("NB: Dominant Strategy Function For 2x2 Matrices Only.\nDominant Strategy shown if both players have the same value in the matrix.\nA matrix with only a single '1' suggests that there is no dominant strategy\nfor either players. As you need 'two' or more sets of '1' to find a Nach Equilibrium.\n")
            
            differenceMethod(player12x2, player22x2, difference2x2)
            differenceComparision()
            
            printMatrix(difference2x2, "Difference Array", True)
            printMatrix(dominantResult2x2, "Dominant Strategy Array", True)

            dominantSolutionCheck(dominantResult2x2)

            print("\nNB: If you find that both players have a '0' Stupid Strategy Result this shows\na scenario where both players do not fail by having poor payouts.\nTherefore, where both players have a '0' we may identify the Nach Equilibrium.\n")
            greaterThanMethod(player12x2, stupidPlayer12x2)
            greaterThanMethod(player22x2, stupidPlayer22x2)

            printMatrix(stupidPlayer12x2, "Stupid Strategy Player 1 2x2 Results", True)
            printMatrix(stupidPlayer22x2, "Stupid Strategy Player 2 2x2 Results", True)

            greaterThanComparision(player12x2, player22x2, stupidPlayer12x2, stupidPlayer22x2)
            
            end()
    else:
            print("Scenario not selected.")
    end()

#Finds Dominant values by calculating the difference between the players matrices
def differenceMethod(player1, player2, difference):
    for x in range(len(player1 and player2)):
        for y in range(len(player1 and player2)):
            difference[x][y] = abs((player1[x][y])-(player2[x][y]))

#Compare the values in the difference matrix against each other to see if there is a matching value somewhere else in the array
def differenceComparision():
    for x in range(len(player1 or player2)):
        for y in range(len(player1 or player2)):
            try:
                if (difference2x2[x][y] == difference2x2[x][y+1]):
                    dominantResult2x2[x][y] = 1
                elif (difference2x2[x][y] == difference2x2[x+1][y]):
                    dominantResult2x2[x][y] = 1
                elif (difference2x2[x][y] == difference2x2[x+1][y+1]):
                    dominantResult2x2[x][y] = 1
                else:
                    dominantResult2x2[x][y] = 0
            except:
                pass

#Check to see if there are '2 or more' dominant values to show the Nach Equilibrium
def dominantSolutionCheck(dominantResult2x2):
    solutionFound = 0
    for x in range(len(dominantResult2x2)):
        for y in range(len(dominantResult2x2)):
                if dominantResult2x2[x][y] == 1:
                    solutionFound += 1
    if solutionFound < 2:
        print("No dominant solution found. Saddle point detected.")
    else:
        print("Nach Equilibrium detected.")
                    
#Compare every value in the player arrays against the other row values. If there are better alternative values,
#then the current value being checked is considered 'stupid' and marked with a '1'.
def greaterThanMethod(player, playerResult):
    for x in range(len(player)):
        for y in range(len(player)):
            for z in range(len(player)):
                if player[x][z] < player[y][z]:
                    playerResult[x][z] = 1

#If there are '0's at the same index location in both result matrices, then this value is the Nach Equilibrium
def greaterThanComparision(player1, player2, playerResult1, playerResult2):
    equilibriumFound = False
    #Find equilibrium by looking for matching 0 result values
    for x in range(len(playerResult1 and playerResult2)):
        for y in range(len(playerResult1 and playerResult2)):
            if playerResult1[x][y] == 0 and playerResult2[x][y] == 0:
                print("Nach Equilibrium Found at Index: [{0}][{1}] with the values '{2}' and '{3}' respectively.".format(x, y, player1[x][y], player2[x][y]))
                equilibriumFound = True
    if (not equilibriumFound):
        print("Equilibrium Not Found")

#Sub Procedures and Functions for UI elements
#Print a matrix using the appropriate formatting
def printMatrix(matrix, title, newLine):
    print(title,":")
    print('\n'.join([''.join(['{:4}'.format(int(item)) for item in row]) for row in matrix]))
    if (newLine): print("")

#Checks which scenario the user would like the system to consider and prevents an invalid entry
def userConfirm(question): #Require the user to select a question to solve
    reply = str(input(question+': ')).lower().strip()
    if reply[0] == '1':
        return int(reply[0])
    if reply[0] == '2':
        return int(reply[0])
    else:
        return userConfirm("Please confirm using 1 or 2.")

def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
