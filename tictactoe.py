def win(board):
    if board[1] == board[2] == board[3]:
        return True, board[3]
    elif board[4] == board[5] == board[6]:
        return True, board[6]
    elif board[7] == board[8] == board[9]:
        return True, board[9]
    elif board[1] == board[4] == board[7]:
        return True, board[7]
    elif board[2] == board[5] == board[8]:
        return True, board[8]
    elif board[3] == board[6] == board[9]:
        return True, board[9]
    elif board[1] == board[5] == board[9]:
        return True, board[9]
    elif board[3] == board[5] == board[7]:
        return True, board[7]
    else:
        count = 0
        for i in board:
            if i.isalpha():
                count = count + 1
        if count < 9:
            return False, ""
        else:
            return True, "Its a draw, so nobody wins."



            


def switchturn(turn):
    if turn == "x":
        return "o"
    else:
        return "x"



def getinput(turn, board):
    while True:
    
        print(turn + "'s turn")
        
        pos = input("What position do you want to play?")
        if not pos.isdigit():
            print("You are supposed to write a number between 1 and 9.")
        elif not 1 <= int(pos) <= 9:
            print("You are supposed to write a number between 1 and 9.")
        elif not board[int(pos)].isdigit():
            print("Position already taken. Do another one.")
        else:
            return int(pos)
    

def printboard(board):
    print()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('- + - + -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- + - + -')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def main():
    turn = "x"
    board = ['0','1','2','3','4','5','6','7','8','9']
    printboard(board)
    gameover = False
    while not gameover:
        p = getinput(turn, board)
        board[p] = turn 
        printboard(board)
        turn = switchturn(turn)
        gameover, winner = win(board)
    print(winner, "wins")

    
             

main() 