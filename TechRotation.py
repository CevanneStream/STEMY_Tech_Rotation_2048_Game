import random
import copy
from pynput.keyboard import Key, Listener

# ---------------------------------------------------------------- Functions

# counts the number of 2s and 4s
def countNumOf2And4s():
    count = 0
    for row in valueList:
        for element in row:
            if element == 2 or element == 4:
                count += 1
    return count


# count the number of 0s
def countNumof0s():
    count = 0
    for row in valueList:
        for element in row:
            if element == 0:
                count += 1
    return count

# count number of 2048s
def count2048():
    count = 0
    for row in valueList:
        for element in row:
            if element == 2048:
                count += 1
    return count

# check for moves
def checkForMoves():
    # check for horizontally adjacent pieces, where x is the row and y is the column
    for x in range(len(valueList)):
        for y in range(len(valueList[x])-1):
            if valueList[x][y] == valueList[x][y+1]:
                return True
    # check for vertically adjacent pieces, where x is the row and y is the column
    for x in range(len(valueList)-1):
        for y in range(len(valueList[x])):
            if valueList[x][y] == valueList[x+1][y]:
                return True
    return False


# add a piece to a random position on the board
def addPiece():
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    # if there's no empty (0) spots
    if (countNumof0s() == 0 and checkForMoves() == False):
        print("Game Over")
        exit()
    # otherwise pick a position
    elif (countNumof0s() > 0):
        # make sure there isn't already a piece there
        while (valueList[row][column] != 0):
            row = random.randint(0, 3)
            column = random.randint(0, 3)
        # the value of the piece is either 2 or 4, chosen with equal probability
        valueList[row][column] = random.randint(1, 2) * 2


# prints the board to the console
def printBoard():
    #print(countNumof0s())
    print("\n-----------------")
    for row in valueList:
        print("| ", end="")
        for element in row:
            print(element, end=" | ")
        print("\n-----------------")
    print("")

# ---------------------------------------------------------------- Key Functions


def leftKeyPressed():
    oldValueList = copy.deepcopy(valueList)

    for row in valueList:
        # removes all zeros (blanks) in the row
        while row.count(0) > 0:
            row.remove(0)
        # then appends zeros (blanks) to the corresponding side
        while len(row) < 4:
            row.append(0)
        # merges pieces
        if row[0] == row[1]:
            row[0] *= 2
            row[1] = 0
            if row[2] == row[3]:
                row[2] *= 2
                row[3] = 0
            row[1] = row[2]
            row[2] = row[3]
            row[3] = 0
        elif row[1] == row[2]:
            row[1] *= 2
            row[2] = 0
            row[2] = row[3]
            row[3] = 0
        elif row[2] == row[3]:
            row[2] *= 2
            row[3] = 0
    #print(oldValueList != valueList)
    if oldValueList != valueList:
        addPiece()
    printBoard()


def rightKeyPressed():
    oldValueList = copy.deepcopy(valueList)

    for row in valueList:
        # removes all zeros (blanks) in the row
        while row.count(0) > 0:
            row.remove(0)
        # then appends zeros (blanks) to the corresponding side
        while len(row) < 4:
            row.insert(0, 0)
        # merges pieces
        if row[3] == row[2]:
            row[3] *= 2
            row[2] = 0
            if row[1] == row[0]:
                row[1] *= 2
                row[0] = 0
            row[2] = row[1]
            row[1] = row[0]
            row[0] = 0
        elif row[2] == row[1]:
            row[2] *= 2
            row[1] = 0
            row[1] = row[0]
            row[0] = 0
        elif row[1] == row[0]:
            row[1] *= 2
            row[0] = 0

    if oldValueList != valueList:
        addPiece()
    printBoard()

def downKeyPressed():
    oldValueList = copy.deepcopy(valueList)

    # rotate the original list 90 degrees clockwise and operate on it like the left key
    # this is how we move blocks down
    # later we map it back to the original
    sidewaysValueList = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(0, len(valueList)):
        for y in range(0, len(valueList[x])):
            sidewaysValueList[x][y] = valueList[3-y][x]

    # the rest is the left key, but operated on the sideways list
    for row in sidewaysValueList:
        # removes all zeros (blanks) in the row
        while row.count(0) > 0:
            row.remove(0)
        # then appends zeros (blanks) to the corresponding side
        while len(row) < 4:
            row.append(0)
        # merges pieces
        if row[0] == row[1]:
            row[0] *= 2
            row[1] = 0
            if row[2] == row[3]:
                row[2] *= 2
                row[3] = 0
            row[1] = row[2]
            row[2] = row[3]
            row[3] = 0
        elif row[1] == row[2]:
            row[1] *= 2
            row[2] = 0
            row[2] = row[3]
            row[3] = 0
        elif row[2] == row[3]:
            row[2] *= 2
            row[3] = 0
    for x in range(0, len(sidewaysValueList)):
        for y in range(0, len(sidewaysValueList[x])):
            valueList[x][y] = sidewaysValueList[y][3-x]

    if oldValueList != valueList:
        addPiece()
    printBoard()

def upKeyPressed():
    oldValueList = copy.deepcopy(valueList)

    # rotate the original list 90 degrees clockwise and operate on it like the right key
    # this is how we move blocks down
    # later we map it back to the original
    sidewaysValueList = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(0, len(valueList)):
        for y in range(0, len(valueList[x])):
            sidewaysValueList[x][y] = valueList[3-y][x]

    # the rest is the right key, but operated on the sideways list
    for row in sidewaysValueList:
        # removes all zeros (blanks) in the row
        while row.count(0) > 0:
            row.remove(0)
        # then appends zeros (blanks) to the corresponding side
        while len(row) < 4:
            row.insert(0, 0)
        # merges pieces
        if row[3] == row[2]:
            row[3] *= 2
            row[2] = 0
            if row[1] == row[0]:
                row[1] *= 2
                row[0] = 0
            row[2] = row[1]
            row[1] = row[0]
            row[0] = 0
        elif row[2] == row[1]:
            row[2] *= 2
            row[1] = 0
            row[1] = row[0]
            row[0] = 0
        elif row[1] == row[0]:
            row[1] *= 2
            row[0] = 0
    for x in range(0, len(sidewaysValueList)):
        for y in range(0, len(sidewaysValueList[x])):
            valueList[x][y] = sidewaysValueList[y][3-x]

    if oldValueList != valueList:
        addPiece()
    printBoard()

# ---------------------------------------------------------------- Pynput Functions


def on_press(key):
    if key == Key.right:
        rightKeyPressed()
    elif key == Key.left:
        leftKeyPressed()
    elif key == Key.up:
        upKeyPressed()
    elif key == Key.down:
        downKeyPressed()
    if countNumof0s() == 0 and checkForMoves() == False:
        print("Game Over")
        exit()
    if count2048() > 0:
        print("You won!")


def on_release(key):
    # print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# ---------------------------------------------------------------- The Actual Program


# stores the value at each position in 4x4 grid
valueList = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

while countNumOf2And4s() < 2:
    # places a 2-2 or 2-4 in a random position in the list to initialize the board
    rowNum = random.randint(0, 3)
    columnNum = random.randint(0, 3)
    valueList[rowNum][columnNum] = random.randint(1, 2) * 2
    
    count4s = 0
    for row in valueList:
        for element in row:
            if element == 4:
                count4s += 1
    if(count4s == 2):
        valueList[rowNum][columnNum] = 2
    
printBoard()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
"""
# non blocking
listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
"""










