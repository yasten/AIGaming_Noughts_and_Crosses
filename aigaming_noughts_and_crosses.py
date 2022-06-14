#   _   _                   _     _            _              _    ____                             
#  | \ | | ___  _   _  __ _| |__ | |_ ___     / \   _ __   __| |  / ___|_ __ ___  ___ ___  ___  ___ 
#  |  \| |/ _ \| | | |/ _` | '_ \| __/ __|   / _ \ | '_ \ / _` | | |   | '__/ _ \/ __/ __|/ _ \/ __|
#  | |\  | (_) | |_| | (_| | | | | |_\__ \  / ___ \| | | | (_| | | |___| | | (_) \__ \__ \  __/\__ \
#  |_| \_|\___/ \__,_|\__, |_| |_|\__|___/ /_/   \_\_| |_|\__,_|  \____|_|  \___/|___/___/\___||___/
#                     |___/                                                                         
botName='yaseenteng-defbot'

import random
import json
from random import randint


# priorities are:
# 1. win by getting 3 in a row
# 2. block oppenent getting 3 in a row
# 3. claim the centre
# 4. take a corner
# 5. take a side

def calculateMove(gameState):

    ret = dict()

    if MyTwoInRow(gameState) != -1:  # Check for winning move
        ret['Position'] = MyTwoInRow(gameState)
        return ret

    if OppTwoInRow(gameState) != -1:  # Check to block opponent's winning move
        ret['Position'] = OppTwoInRow(gameState)
        return ret

    pos = centre_or_rand(gameState)
    print('My move is '+str(pos)+' OpponentId: '+gameState['OpponentId'])
    ret['Position'] = pos
    return ret

# Takes the center if available and otherwise guesses position
def centre_or_rand(gameState):

    if gameState['Board'][4] == " ":  # Take center square if available
        return(4)

    # If center square is taken, guess a corner.
    if (gameState['Board'][0] == " ") or (gameState['Board'][2] == " ") or (gameState['Board'][6] == " ") or (gameState['Board'][8] == " "):

           move = random.sample([0, 2, 6, 8], 1)
           while(gameState['Board'][move[0]] != " "): #If taken...
                move = random.sample([0, 2, 6, 8], 1)

           return(move[0])

    # Else guess randomly
    move = random.sample([1, 3, 5, 7], 1)
    while(gameState['Board'][move[0]] != " "): #If taken...
        move = random.sample([1, 3, 5, 7], 1) #... keep random guessing until found one
    return(move[0])

def OppTwoInRow(gameState): #Returns the (first) location that will block your opponent from winning, returns -1 otherwise
    myRole = gameState["Role"]
    if(myRole=="X"):
        oppRole = "O"
    else:
        oppRole = "X"
    if(((gameState['Board'][1]==oppRole and gameState['Board'][2]==oppRole)or(gameState['Board'][3]==oppRole and gameState['Board'][6]==oppRole)or(gameState['Board'][4]==oppRole and gameState['Board'][8]==oppRole))and gameState['Board'][0]==" "):
        move = 0
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][2]==oppRole)or(gameState['Board'][4]==oppRole and gameState['Board'][7]==oppRole))and gameState['Board'][1]==" "):
        move = 1
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][1]==oppRole)or(gameState['Board'][4]==oppRole and gameState['Board'][6]==oppRole)or(gameState['Board'][5]==oppRole and gameState['Board'][8]==oppRole))and gameState['Board'][2]==" "):
        move = 2
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][6]==oppRole)or(gameState['Board'][4]==oppRole and gameState['Board'][5]==oppRole))and gameState['Board'][3]==" "):
        move = 3
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][8]==oppRole)or(gameState['Board'][1]==oppRole and gameState['Board'][7]==oppRole)or(gameState['Board'][2]==oppRole and gameState['Board'][6]==oppRole)or(gameState['Board'][3]==oppRole and gameState['Board'][5]==oppRole))and gameState['Board'][4]==" "):
        move = 4
    elif(((gameState['Board'][2]==oppRole and gameState['Board'][8]==oppRole)or(gameState['Board'][3]==oppRole and gameState['Board'][4]==oppRole))and gameState['Board'][5]==" "):
        move = 5
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][3]==oppRole)or(gameState['Board'][2]==oppRole and gameState['Board'][4]==oppRole)or(gameState['Board'][7]==oppRole and gameState['Board'][8]==oppRole))and gameState['Board'][6]==" "):
        move = 6
    elif(((gameState['Board'][1]==oppRole and gameState['Board'][4]==oppRole)or(gameState['Board'][6]==oppRole and gameState['Board'][8]==oppRole))and gameState['Board'][7]==" "):
        move = 7
    elif(((gameState['Board'][0]==oppRole and gameState['Board'][4]==oppRole)or(gameState['Board'][2]==oppRole and gameState['Board'][5]==oppRole)or(gameState['Board'][6]==oppRole and gameState['Board'][7]==oppRole))and gameState['Board'][8]==" "):
        move = 8
    else:
        move = -1
    return move

def MyTwoInRow(gameState): #Returns the (first) location that will give you three in a row, returns -1 if none exist
    myRole = gameState["Role"]
    gameState['Board'] = gameState['Board']  # Simplify code
    if(((gameState['Board'][1]==myRole and gameState['Board'][2]==myRole)or(gameState['Board'][3]==myRole and gameState['Board'][6]==myRole)or(gameState['Board'][4]==myRole and gameState['Board'][8]==myRole))and gameState['Board'][0]==" "):
        move = 0
    elif(((gameState['Board'][0]==myRole and gameState['Board'][2]==myRole)or(gameState['Board'][4]==myRole and gameState['Board'][7]==myRole))and gameState['Board'][1]==" "):
        move = 1
    elif(((gameState['Board'][0]==myRole and gameState['Board'][1]==myRole)or(gameState['Board'][4]==myRole and gameState['Board'][6]==myRole)or(gameState['Board'][5]==myRole and gameState['Board'][8]==myRole))and gameState['Board'][2]==" "):
        move = 2
    elif(((gameState['Board'][0]==myRole and gameState['Board'][6]==myRole)or(gameState['Board'][4]==myRole and gameState['Board'][5]==myRole))and gameState['Board'][3]==" "):
        move = 3
    elif(((gameState['Board'][0]==myRole and gameState['Board'][8]==myRole)or(gameState['Board'][1]==myRole and gameState['Board'][7]==myRole)or(gameState['Board'][2]==myRole and gameState['Board'][6]==myRole)or(gameState['Board'][3]==myRole and gameState['Board'][5]==myRole))and gameState['Board'][4]==" "):
        move = 4
    elif(((gameState['Board'][2]==myRole and gameState['Board'][8]==myRole)or(gameState['Board'][3]==myRole and gameState['Board'][4]==myRole))and gameState['Board'][5]==" "):
        move = 5
    elif(((gameState['Board'][0]==myRole and gameState['Board'][3]==myRole)or(gameState['Board'][2]==myRole and gameState['Board'][4]==myRole)or(gameState['Board'][7]==myRole and gameState['Board'][8]==myRole))and gameState['Board'][6]==" "):
        move = 6
    elif(((gameState['Board'][1]==myRole and gameState['Board'][4]==myRole)or(gameState['Board'][6]==myRole and gameState['Board'][8]==myRole))and gameState['Board'][7]==" "):
        move = 7
    elif(((gameState['Board'][0]==myRole and gameState['Board'][4]==myRole)or(gameState['Board'][2]==myRole and gameState['Board'][5]==myRole)or(gameState['Board'][6]==myRole and gameState['Board'][7]==myRole))and gameState['Board'][8]==" "):
        move = 8
    else:
        move = -1
    return move
