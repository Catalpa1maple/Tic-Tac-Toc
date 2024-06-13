import os
import random

#play = 'Y'
count = 1
board = [' ' for x in range(10)]

def printBoard(board):
    print()
    print("Game",count)
    print()
    print('')
    print('')
    print('')
    print("-----------")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-----------")
    print('')
    print('')

def isBoardFull(board):
    return not board.count(' ') >= 2

def hasSpace(board,position):
    return board[position] == ' '

    
def playerMove():
    move = int(input("Please select a position."))
    while move < 1 or move > 9:
        move = int(input("Please input 1 to 9."))
    while not hasSpace(board,move):
        move = int(input("Sorry the space had occupied. Please select other place."))
    board[move] = 'O'
    

    
def hasWinner(board,letter):
    return(
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter)
    )

def cpuMove():
    move = random.randint(1,9)
    while not hasSpace(board,move):
        move = random.randint(1,9)
    board[move] = 'X'




def GamePlay():
    printBoard(board)

    while not(isBoardFull(board)):
        print("Player's Turn")
        print('')
        playerMove()
        os.system('clear')
        printBoard(board)

        if hasWinner(board,'O'):
            os.system('clear')
            
            print('')
            print("You Win!")
            print('---------')
            #play = input("Want a new game?(Y/N)")
            return
        
        if isBoardFull(board):
            break
        
        print("CPU's Turn")
        print('')
        cpuMove()
        os.system('clear')
        printBoard(board)

        if hasWinner(board,'O'):
            os.system('clear')
            
            print('')
            print("You Lose!")
            print('---------')
            #play = input("Want a new game?(Y/N)")
            return
    os.system('clear')
    print("The Game is draw")
    #play = input("Want a new game?(Y/N)")

os.system('clear')
while True:
   # if play == 'Y':
    board = [' ' for x in range(10)]
    GamePlay()
    count+=1
   # elif play == 'N':
   #     break


