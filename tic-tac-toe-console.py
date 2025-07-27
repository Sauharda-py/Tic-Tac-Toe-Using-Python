#create the board

board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}
player = 'O'
comp = 'X'

def printBoard():
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])

def spaceIsFree(position):

    if position<1 or position>9:
        return False
    elif board[position] == ' ':
        return True
    else:
        return False
    
def insertLetter(position,letter):
    if spaceIsFree(position):
        board[position] = letter
        
        if checkDraw():
            printBoard()
            print("Draw!")
            exit()
        if checkWin():
            if letter=='X':
                printBoard()
                print("Bot Wins!")
                exit()
            else:
                printBoard()
                print("Player Wins!")
                exit()
    else:
        print("Invalid Position! ")
        position = int(input("Enter the correct position:= "))
        insertLetter(position,letter)
        return

#Game end logic 

def checkWin():
    #Horizontal
    if board[1]==board[2] and board[1]==board[3] and board[1]!=' ':
        return True
    if board[4]==board[5] and board[4]==board[6] and board[4]!=' ':
        return True
    if board[7]==board[8] and board[7]==board[9] and board[7]!=' ':
        return True
    #Vertical
    if board[1]==board[4] and board[1]==board[7] and board[1]!=' ':
        return True
    if board[2]==board[5] and board[2]==board[8] and board[2]!=' ':
        return True
    if board[3]==board[6] and board[3]==board[9] and board[3]!=' ':
        return True
    #Diagonal
    if board[1]==board[5] and board[1]==board[9] and board[1]!=' ':
        return True
    if board[3]==board[5] and board[3]==board[7] and board[3]!=' ':
        return True
    
    return False

def checkDraw():
    for i in board.keys():
        if board[i]==' ':
            return False
    return True

#Check who wins

def checkWhichMarkWon(letter):
    #Horizontal
    if board[1]==board[2] and board[1]==board[3] and board[1]==letter:
        return True
    if board[4]==board[5] and board[4]==board[6] and board[4]==letter:
        return True
    if board[7]==board[8] and board[7]==board[9] and board[7]==letter:
        return True
    #Vertical
    if board[1]==board[4] and board[1]==board[7] and board[1]==letter:
        return True
    if board[2]==board[5] and board[2]==board[8] and board[2]==letter:
        return True
    if board[3]==board[6] and board[3]==board[9] and board[3]==letter:
        return True
    #Diagonal
    if board[1]==board[5] and board[1]==board[9] and board[1]==letter:
        return True
    if board[3]==board[5] and board[3]==board[7] and board[3]==letter:
        return True

    return False



#Moves

def playerMove():
    position = int(input("Enter the position for O: "))
    insertLetter(position,player)
    return

def compMove():
    bestScore = -999
    bestMove = 0
    for i in board.keys():
        if board[i]==' ':
            board[i] = comp
            score = minMax(False)
            board[i] = ' '
            if score>=bestScore:
                bestScore = score
                bestMove = i
    insertLetter(bestMove,comp)
    printBoard()
    return


def minMax(isMax):
    if checkWhichMarkWon(player):
        return -1
    if checkWhichMarkWon(comp):
        return 1
    if checkDraw():
        return 0

    if isMax:
        bestScore = -999
        for i in board.keys():
            if board[i]==' ':
                board[i] = comp
                score = minMax(False)
                board[i] = ' '
                if score>bestScore:
                    bestScore = score
        return bestScore
    else: #player's move (must be minimized) 
        bestScore = 999
        for i in board.keys():
            if board[i]==' ':
                board[i]=player
                score = minMax(True)
                board[i] = ' '
                if score<bestScore:
                    bestScore = score
        return bestScore



    

#Game loop

while not checkWin():
    compMove()
    playerMove()