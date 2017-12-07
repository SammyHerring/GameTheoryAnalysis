#Difference Method Solution to find Nach Equilibrium
#Proof of Concept to find the dominant solutions to produce a nach equilibrium where difference values are equal.
#We may prove the nach equilibrium result by selecting the intersection with the maximum original input value.
player1 = [[3, 8],
           [0, 4]]
player2 = [[3, 0],
           [8, 4]]
difference = [[0, 0],
              [0, 0]]

#Finds Dominant Intersection through Difference Calculations
def differenceMethod():
    for x in range(2):
        for y in range(2):
            difference[x][y] = abs((player1[x][y])-(player2[x][y]))
            print(x)
            print(y)
            print("P1: ", player1[x][y])
            print("P2: ", player2[x][y])
            print("Difference: {0}".format(difference[x][y]))
            print("Difference Array: ", difference)

differenceMethod()
