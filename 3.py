board = [[" "] * 3 for _ in range(3)]
def printBoard():
    print()
    for i in board:
        print(" | ".join(i))
        print("_"*10)
def checkWinner(player):
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]==player):
            return True
        if(board[0][i]==board[1][i]==board[2][i]==player):
            return True
    if(board[0][0]==board[1][1]==board[2][2]==player)or(board[0][2]==board[1][1]==board[2][0]==player):
             return True
    return False
player="X"
moves=0
while(moves<9):
    m,n=map(int,input("\n player:{}  \n Coordinates:" .format(player)).split())
    if(board[m][n]!=" "):
        print("invalid maove")
        continue
    else:
        board[m][n]=player
        printBoard()
        moves+=1
        if(checkWinner(player)):
            print("player {} wins !".format(player))
            break
        if(player=="X"):
            player="O"
        else:
            player="X"
if(moves==9 and checkWinner("X")==False and checkWinner("O")==False):
    printBoard()
    print("Its a tie")

