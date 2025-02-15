def read(): #reads the FEN code inside of "fen.txt"
    with open("fen.txt", "r") as f:
        fen_code = f.read()
        ending = fen_code[-10:]
        print(f"\n{fen_code}")
        turn(ending)

def turn(ending): #figures out whos turn it is to play
    if "w" in ending:
        turn = "white"
    else:
        turn = "black"
    print(f"{turn}'s turn to move")

def init_board(): #sets each row to the value given

    with open("fen.txt", "r") as f:
        line = (f.read())[:-10]
        line = line.split("/")

        for i in range(len(line)):
            chess_row = []
            for j in (line[i]):
                if j.isdigit() == True:
                    for k in range(int(j)):
                        chess_row.append(".")
                else:
                    chess_row.append(str(j))

            if len(chess_row) == 8:
                chess_board.append(chess_row)

def display_board(): #prints chess board
    for i in range(len(chess_board)):
        print(f"{chess_board[i]}")
    print()

def ammend():
    print("would you like to make ammends (y/n) : ")
    answer = str(input())
    if answer.lower() == "y":
        print("enter coordinate and piece seperated by a comma or a space:")
        answer = str(input())
        if "," in answer:
            coordinates = answer.split(",")
            make_ammend(coordinates[0],coordinates[1])
        elif " " in answer:
            coordinates = answer.split(" ")
            make_ammend(coordinates[0],coordinates[1])
        else:
            print("invalid coordinates")
            return

def make_ammend(coordinate,piece):
    row = 8 - int(coordinate[1])
    column = (ord(coordinate[0])-96) - 1
    print(f"\n{chess_board[row][column]} --> {piece}")
    chess_board[row][column] = piece
    display_board()


global chess_board
chess_board = [] #initialising the board to be blank






read() #reads the FEN code inside of "fen.txt"
init_board() #sets each row to the value given
display_board() #prints chess board
ammend()