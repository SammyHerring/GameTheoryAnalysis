import sys
#Difference Method Solution to find Nach Equilibrium
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.
player1 = [[3, 8],
           [0, 4]]
player2 = [[3, 0],
           [8, 4]]
difference = [[0, 0],
              [0, 0]]
dominant = [[0, 0],
             [0, 0]]
silly = [[0, 0],
         [0, 0]]

#Proposed method for producing entire solution checking for both dominant and silly solutions.
def Main():
    differenceMethod()
    differenceComparision()
    print("Dominant Strategies Bool Array: ", dominant)
    #greaterThanMethod()
    print("Silly Strategies Bool Array: ", silly)
    #greaterThanComparision()

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
    for x in range(2):
        for y in range(2):
            if player1[x][y] == player2[x][y]:
                dominant[x][y] = 1
                return
            else:
                dominant[x][y] = 0
                return

def greaterThanMethod():
    
    return

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
