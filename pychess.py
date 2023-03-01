from os import system
from time import sleep

def clear():
    system("clear")

class pychess():
    def __init__(self) -> None:
        self.chessboard = [[0 for g in range(8)] for i in range(8)]
        self.white_move = True
        self.black_king_moved = False
        self.white_king_moved = False
        self.Playing = True
        self.game_result = ""
        self.moves = []

        self.Analysis_Mode = False
        self.Current_Move_Index = 0

    def initializeboard(self):
        self.white_move = True
        self.white_king_moved = False
        self.black_king_moved = False

        self.chessboard[0][0] = 15
        self.chessboard[7][0] = 15
        self.chessboard[1][0] = 4
        self.chessboard[6][0] = 4
        self.chessboard[2][0] = 3
        self.chessboard[5][0] = 3
        self.chessboard[3][0] = 2
        self.chessboard[4][0] = 1

        self.chessboard[0][7] = 16
        self.chessboard[7][7] = 16
        self.chessboard[1][7] = 10
        self.chessboard[6][7] = 10
        self.chessboard[2][7] = 9
        self.chessboard[5][7] = 9
        self.chessboard[3][7] = 8
        self.chessboard[4][7] = 7

        # Pawns 
        for i in range(8):
            self.chessboard[i][1] = 6
            self.chessboard[i][6] = 12

    def printboard(self,White_Perspective=False):
        for Row in range(8):
            Row_Str = ""
            for Column in range(8):
                if White_Perspective:
                    row = 7 - Row
                elif not White_Perspective:
                    row = Row

                Piece_Id = str(self.chessboard[Column][row])
                Get_Colour = ""

                if len(Piece_Id) > 2:
                    Get_Colour = Piece_Id[:5]
                    #print(Get_Colour)
                    #print(Piece_Id)
                    Piece_Id = Piece_Id[5:-2] # 8 -8
                    #print(Piece_Id)

                Piece_Id = Piece_Id.replace("19","@") # Place Holder
                
                Piece_Id = Piece_Id.replace("18","!") # Black Attacks
                Piece_Id = Piece_Id.replace("17","%") # White Attacks

                Piece_Id = Piece_Id.replace("16","♖")
                Piece_Id = Piece_Id.replace("15","♜")
                Piece_Id = Piece_Id.replace("14","♙")
                Piece_Id = Piece_Id.replace("13","♟︎")

                Piece_Id = Piece_Id.replace("7","♔")
                Piece_Id = Piece_Id.replace("8","♕")
                Piece_Id = Piece_Id.replace("9","♗")
                Piece_Id = Piece_Id.replace("10","♘")
                Piece_Id = Piece_Id.replace("11","♖")
                Piece_Id = Piece_Id.replace("12","♙")

                Piece_Id = Piece_Id.replace("1","♚")
                Piece_Id = Piece_Id.replace("2","♛")
                Piece_Id = Piece_Id.replace("3","♝")
                Piece_Id = Piece_Id.replace("4","♞")
                Piece_Id = Piece_Id.replace("5","♜")
                Piece_Id = Piece_Id.replace("6","♟︎")

                Piece_Id = Piece_Id.replace("0"," ")

                Row_Str += "\033[4m"+Get_Colour + Piece_Id + "\033[0m" + "|"
            # Replace characters with chess pieces
            # 0 = empty
            # White: 1 = King 2 = Queen 3 = Bishop 4 = Knight 5 = Rook 6 = Pawn
            # Black: 7 8 9 10 11 12
            # For En Passant
            # 13 = Double moved white pawn
            # 14 = Double moved black pawn
            # For Casell
            # 15 = Unused rook white
            # 16 = Unused rook black

            Row_Str += " "+str(row+1)
            print(Row_Str)
        print("a b c d e f g h")

    def printboard_ASCII(self,White_Perspective=False) -> None:
        for Row in range(8):
            Row_Str = ""
            for Column in range(8):
                if White_Perspective:
                    row = 7 - Row
                elif not White_Perspective:
                    row = Row

                Piece_Id = str(self.chessboard[Column][row])
                Get_Colour = ""

                if len(Piece_Id) > 2:
                    Get_Colour = Piece_Id[:5]
                    #print(Get_Colour)
                    #print(Piece_Id)
                    Piece_Id = Piece_Id[5:-2] # 8 -8
                    #print(Piece_Id)

                Piece_Id = Piece_Id.replace("19","@") # Place Holder
                
                Piece_Id = Piece_Id.replace("18","!") # Black Attacks
                Piece_Id = Piece_Id.replace("17","%") # White Attacks

                Piece_Id = Piece_Id.replace("16","r")
                Piece_Id = Piece_Id.replace("15","R")
                Piece_Id = Piece_Id.replace("14","p")
                Piece_Id = Piece_Id.replace("13","P")

                Piece_Id = Piece_Id.replace("7","k")
                Piece_Id = Piece_Id.replace("8","q")
                Piece_Id = Piece_Id.replace("9","b")
                Piece_Id = Piece_Id.replace("10","k")
                Piece_Id = Piece_Id.replace("11","r")
                Piece_Id = Piece_Id.replace("12","p")

                Piece_Id = Piece_Id.replace("1","K")
                Piece_Id = Piece_Id.replace("2","Q")
                Piece_Id = Piece_Id.replace("3","B")
                Piece_Id = Piece_Id.replace("4","K")
                Piece_Id = Piece_Id.replace("5","R")
                Piece_Id = Piece_Id.replace("6","P")

                Piece_Id = Piece_Id.replace("0"," ")

                Row_Str += "\033[4m"+Get_Colour + Piece_Id + "\033[0m" + "|"
            # Replace characters with chess pieces
            # 0 = empty
            # White: 1 = King 2 = Queen 3 = Bishop 4 = Knight 5 = Rook 6 = Pawn
            # Black: 7 8 9 10 11 12
            # For En Passant
            # 13 = Double moved white pawn
            # 14 = Double moved black pawn
            # For Casell
            # 15 = Unused rook white
            # 16 = Unused rook black

            Row_Str += " "+str(row+1)
            print(Row_Str)
        print("a b c d e f g h")

    def Piece_Position_To_Coordinate(self,Piece_Position:str) -> str:
        if len(Piece_Position) != 2:
            return "Invalid"
        try:
            validification = int(Piece_Position[1])
        except ValueError:
            input(Piece_Position)
            return "Invalid"
        if not (Piece_Position[0] == "a" or Piece_Position[0] == "b" or Piece_Position[0] == "c" or Piece_Position[0] == "d" or Piece_Position[0] == "e" or Piece_Position[0] == "f" or Piece_Position[0] == "g" or Piece_Position[0] == "h"):
            
            return "Invalid"
        if Piece_Position[0] == "a":
            Piece_Coordinate = Piece_Position.replace("a","0",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "b":
            Piece_Coordinate = Piece_Position.replace("b","1",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "c":
            Piece_Coordinate = Piece_Position.replace("c","2",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "d":
            Piece_Coordinate = Piece_Position.replace("d","3",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "e":
            Piece_Coordinate = Piece_Position.replace("e","4",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "f":
            Piece_Coordinate = Piece_Position.replace("f","5",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "g":
            Piece_Coordinate = Piece_Position.replace("g","6",1)[0] + str(int(Piece_Position[1])-1)
        elif Piece_Position[0] == "h":
            Piece_Coordinate = Piece_Position.replace("h","7",1)[0] + str(int(Piece_Position[1])-1)
        else:
            input(Piece_Position)
            return "Invalid"
        return Piece_Coordinate

    def Is_Empty(self,Board_Coordinate:str) -> bool:
        if self.chessboard[int(Board_Coordinate[0])][int(Board_Coordinate[1])] == 0:
            return True
        else:
            return False

    def Is_Coord_Valid(self,Coordinate:str) -> bool:
        try:
            if 0 <= int(Coordinate[0]) <= 7:
                if 0 <= int(Coordinate[1]) <= 7:
                    return True
            return False
        except ValueError:
            return False

    def Get_Piece(self,Coordinate:str) -> int:
        """
        Parameter takes in coordinate
        This function returns the chess piece type in that coordinate on the board
        """
        if self.Is_Coord_Valid(Coordinate):
            return self.chessboard[int(Coordinate[0])][int(Coordinate[1])]
        return -1

    def Replace_Piece(self,Coordinate:str,Replace_With):
        """
        Force change position on the board with other string
        Does not check any thing!
        """
        self.chessboard[int(Coordinate[0])][int(Coordinate[1])] = Replace_With

    def Is_White_Piece(self,Coordinate_Or_Piece) -> bool:
        if type(Coordinate_Or_Piece) == str:
            Piece = self.Get_Piece(Coordinate_Or_Piece)
        else:
            Piece = Coordinate_Or_Piece
        if Piece == 1 or Piece == 2 or Piece == 3 or Piece == 4 or Piece == 5 or Piece == 6 or Piece == 13 or Piece == 15 or Piece == 18:
            return True
        return False
    
    def Is_Black_Piece(self,Coordinate_Or_Piece) -> bool:
        if type(Coordinate_Or_Piece) == str:
            Piece = self.Get_Piece(Coordinate_Or_Piece)
        else:
            Piece = Coordinate_Or_Piece
        if Piece == 7 or Piece == 8 or Piece == 9 or Piece == 10 or Piece == 11 or Piece == 12 or Piece == 14 or Piece == 16 or Piece == 17:
            return True
        return False

    def Avaliable_Moves(self,Piece_Coordinate:str, Check=True):
        Moving_Piece = self.Get_Piece(Piece_Coordinate)
        Avaliable_Moves = [] # Take in Piece Coordinate NOT Piece Position!

        if Check == True:
            if self.white_move:
                if not self.Is_White_Piece(Piece_Coordinate):
                    return Avaliable_Moves
            if not self.white_move:
                if self.Is_White_Piece(Piece_Coordinate):
                    return Avaliable_Moves

        # Pawn
        if Moving_Piece == 6: # White 
            # Pawn diagonal capture
            Left_Diagonal = str(int(Piece_Coordinate[0])-1)+str(int(Piece_Coordinate[1])+1)
            Right_Diagonal = str(int(Piece_Coordinate[0])+1)+str(int(Piece_Coordinate[1])+1)
            if self.Is_Coord_Valid(Left_Diagonal):
                if not self.Is_Empty(Left_Diagonal):
                    if not self.Is_White_Piece(Left_Diagonal):
                        Avaliable_Moves.append(Left_Diagonal)
            if self.Is_Coord_Valid(Right_Diagonal):
                if not self.Is_Empty(Right_Diagonal):
                    if not self.Is_White_Piece(Right_Diagonal):
                        Avaliable_Moves.append(Right_Diagonal)
            # En passant
            if Piece_Coordinate[1] == "4":
                if self.Is_Coord_Valid(str(int(Piece_Coordinate[0])-1) + Piece_Coordinate[1]):
                    if self.chessboard[int(Piece_Coordinate[0]) - 1][int(Piece_Coordinate[1])] == 14: # Left
                        Avaliable_Moves.append(Left_Diagonal)
                if self.Is_Coord_Valid(str(int(Piece_Coordinate[0])+1) + Piece_Coordinate[1]):
                    if self.chessboard[int(Piece_Coordinate[0]) + 1][int(Piece_Coordinate[1])] == 14: # Right
                        Avaliable_Moves.append(Right_Diagonal)

            if Piece_Coordinate[1] == "1": # First Move
                if self.Is_Empty(Piece_Coordinate[0]+"2"):
                    Avaliable_Moves.append(Piece_Coordinate[0]+"2")
                    if self.Is_Empty(Piece_Coordinate[0]+"3"):
                        Avaliable_Moves.append(Piece_Coordinate[0]+"3")
            else:
                try:
                    if int(Piece_Coordinate[1]) + 1 < 8:
                        if self.Is_Empty(Piece_Coordinate[0]+str(int(Piece_Coordinate[1])+1)):
                            Avaliable_Moves.append(Piece_Coordinate[0]+str(int(Piece_Coordinate[1])+1))
                except KeyError:
                    pass
        
        if Moving_Piece == 12: # Black 
            # Pawn diagonal capture
            Left_Diagonal = str(int(Piece_Coordinate[0])-1)+str(int(Piece_Coordinate[1])-1)
            Right_Diagonal = str(int(Piece_Coordinate[0])+1)+str(int(Piece_Coordinate[1])-1)
            if self.Is_Coord_Valid(Left_Diagonal):
                if not self.Is_Empty(Left_Diagonal):
                    if self.Is_White_Piece(Left_Diagonal):
                        Avaliable_Moves.append(Left_Diagonal)
            if self.Is_Coord_Valid(Right_Diagonal):
                if not self.Is_Empty(Right_Diagonal):
                    if self.Is_White_Piece(Right_Diagonal):
                        Avaliable_Moves.append(Right_Diagonal)
            # En passant
            if Piece_Coordinate[1] == "3":
                if self.Is_Coord_Valid(str(int(Piece_Coordinate[0])-1) + Piece_Coordinate[1]):
                    if self.chessboard[int(Piece_Coordinate[0]) - 1][int(Piece_Coordinate[1])] == 13: # Left
                        Avaliable_Moves.append(Left_Diagonal)
                if self.Is_Coord_Valid(str(int(Piece_Coordinate[0])+1) + Piece_Coordinate[1]):
                    if self.chessboard[int(Piece_Coordinate[0]) + 1][int(Piece_Coordinate[1])] == 13: # Right
                        Avaliable_Moves.append(Right_Diagonal)

            if Piece_Coordinate[1] == "6": # First Move
                if self.Is_Empty(Piece_Coordinate[0]+"5"):
                    Avaliable_Moves.append(Piece_Coordinate[0]+"5")
                    if self.Is_Empty(Piece_Coordinate[0]+"4"):
                        Avaliable_Moves.append(Piece_Coordinate[0]+"4")
            else:
                try:
                    if int(Piece_Coordinate[1]) - 1 >= 0:
                        if self.Is_Empty(Piece_Coordinate[0]+str(int(Piece_Coordinate[1])-1)):
                            Avaliable_Moves.append(Piece_Coordinate[0]+str(int(Piece_Coordinate[1])-1))
                except KeyError:
                    pass
        
        # Rook
        if Moving_Piece == 5 or Moving_Piece == 2 or Moving_Piece == 15: # White
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            # Move Left
            iterator = 1
            Coord = str(Column-iterator)+str(Row)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row)
                else:
                    Piece = self.Get_Piece(Coord)
                    if not self.Is_White_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Right
            iterator = -1
            Coord = str(Column-iterator)+str(Row)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator -= 1
                    Coord = str(Column - iterator) + str(Row)
                else:
                    Piece = self.Get_Piece(Coord)
                    if not self.Is_White_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Up
            iterator = 1
            Coord = str(Column)+str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if not self.Is_White_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down
            iterator = -1
            Coord = str(Column)+str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator -= 1
                    Coord = str(Column) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if not self.Is_White_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
        
        if Moving_Piece == 11 or Moving_Piece == 8 or Moving_Piece == 16: # Black
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            # Move Left
            iterator = 1
            Coord = str(Column-iterator)+str(Row)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece): # Capture White Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Right
            iterator = -1
            Coord = str(Column-iterator)+str(Row)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator -= 1
                    Coord = str(Column - iterator) + str(Row)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece): # Capture White Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Up
            iterator = 1
            Coord = str(Column)+str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece): # Capture White Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down
            iterator = -1
            Coord = str(Column)+str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator -= 1
                    Coord = str(Column) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece): # Capture White Pieces
                        Avaliable_Moves.append(Coord)
                    break

        # Knight
        if Moving_Piece == 4: # White
            def Knight_Move(Coord):
                if self.Is_Coord_Valid(Coord):
                    if self.Is_Empty(Coord):
                        Avaliable_Moves.append(Coord)
                    else:
                        Piece = self.Get_Piece(Coord)
                        if not self.Is_White_Piece(Piece): # Capture Black Pieces
                            Avaliable_Moves.append(Coord)
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            Coord = str(Column + 1) + str(Row + 2)
            Knight_Move(Coord)
            Coord = str(Column - 1) + str(Row + 2)
            Knight_Move(Coord)
            Coord = str(Column + 1) + str(Row - 2)
            Knight_Move(Coord)
            Coord = str(Column - 1) + str(Row - 2)
            Knight_Move(Coord)
            Coord = str(Column + 2) + str(Row + 1)
            Knight_Move(Coord)
            Coord = str(Column - 2) + str(Row + 1)
            Knight_Move(Coord)
            Coord = str(Column + 2) + str(Row - 1)
            Knight_Move(Coord)
            Coord = str(Column - 2) + str(Row - 1)
            Knight_Move(Coord)
        
        if Moving_Piece == 10: # Black
            def Knight_Move(Coord):
                if self.Is_Coord_Valid(Coord):
                    if self.Is_Empty(Coord):
                        Avaliable_Moves.append(Coord)
                    else:
                        Piece = self.Get_Piece(Coord)
                        if self.Is_White_Piece(Piece): # Capture Black Pieces
                            Avaliable_Moves.append(Coord)
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            Coord = str(Column + 1) + str(Row + 2)
            Knight_Move(Coord)
            Coord = str(Column - 1) + str(Row + 2)
            Knight_Move(Coord)
            Coord = str(Column + 1) + str(Row - 2)
            Knight_Move(Coord)
            Coord = str(Column - 1) + str(Row - 2)
            Knight_Move(Coord)
            Coord = str(Column + 2) + str(Row + 1)
            Knight_Move(Coord)
            Coord = str(Column - 2) + str(Row + 1)
            Knight_Move(Coord)
            Coord = str(Column + 2) + str(Row - 1)
            Knight_Move(Coord)
            Coord = str(Column - 2) + str(Row - 1)
            Knight_Move(Coord)
            
        # Bishop
        if Moving_Piece == 3 or Moving_Piece == 2: # White
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            # Move Up Left
            iterator = 1
            Coord = str(Column - iterator) + str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_Black_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Up Right
            iterator = 1
            Coord = str(Column + iterator) + str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column + iterator) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_Black_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down Left
            iterator = 1
            Coord = str(Column - iterator) + str(Row + iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row + iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_Black_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down Right
            iterator = 1
            Coord = str(Column + iterator) + str(Row + iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column + iterator) + str(Row + iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_Black_Piece(Piece): # Capture Black Pieces
                        Avaliable_Moves.append(Coord)
                    break
        
        if Moving_Piece == 9 or Moving_Piece == 8: # Black
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            # Move Up Left
            iterator = 1
            Coord = str(Column - iterator) + str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece):
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Up Right
            iterator = 1
            Coord = str(Column + iterator) + str(Row - iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column + iterator) + str(Row - iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece):
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down Left
            iterator = 1
            Coord = str(Column - iterator) + str(Row + iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column - iterator) + str(Row + iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece):
                        Avaliable_Moves.append(Coord)
                    break
            
            # Move Down Right
            iterator = 1
            Coord = str(Column + iterator) + str(Row + iterator)
            while self.Is_Coord_Valid(Coord):
                if self.Is_Empty(Coord):
                    Avaliable_Moves.append(Coord)
                    iterator += 1
                    Coord = str(Column + iterator) + str(Row + iterator)
                else:
                    Piece = self.Get_Piece(Coord)
                    if self.Is_White_Piece(Piece):
                        Avaliable_Moves.append(Coord)
                    break

        # King
        if Moving_Piece == 1 or Moving_Piece == 2: # White
            def King_Move(Coord:str):
                if self.Is_Coord_Valid(Coord):
                    if self.Is_Empty(Coord):
                        Avaliable_Moves.append(Coord)
                    else:
                        Piece = self.Get_Piece(Coord)
                        if not self.Is_White_Piece(Piece): # Capture Black Pieces
                            Avaliable_Moves.append(Coord)
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            Coord = str(Column + 1) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column + 1) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column + 1) + str(Row)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row)
            King_Move(Coord)

            if Moving_Piece == 1: # Castling
                self.Mark_All_Black_Attacks
                if not self.white_king_moved: # Short
                    if self.Get_Piece("70") == 15:
                        if self.Get_Piece("60") == 0 and self.Get_Piece("50") == 0:
                            Avaliable_Moves.append("60")
                        
                if not self.white_king_moved: # Long
                    if self.Get_Piece("00") == 15:
                        if self.Get_Piece("10") == 0 and self.Get_Piece("20") == 0 and self.Get_Piece("30") == 0:
                            Avaliable_Moves.append("20")
                self.Remove_Marked_Black_Attacks()

        if Moving_Piece == 7 or Moving_Piece == 8: # Black
            def King_Move(Coord:str):
                if self.Is_Coord_Valid(Coord):
                    if self.Is_Empty(Coord):
                        Avaliable_Moves.append(Coord)
                    else:
                        Piece = self.Get_Piece(Coord)
                        if self.Is_White_Piece(Piece): # Capture Black Pieces
                            Avaliable_Moves.append(Coord)
            Column = int(Piece_Coordinate[0])
            Row = int(Piece_Coordinate[1])
            Coord = str(Column + 1) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column + 1) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column) + str(Row + 1)
            King_Move(Coord)
            Coord = str(Column) + str(Row - 1)
            King_Move(Coord)
            Coord = str(Column + 1) + str(Row)
            King_Move(Coord)
            Coord = str(Column - 1) + str(Row)
            King_Move(Coord)

            if Moving_Piece == 7: # Castling
                self.Mark_All_White_Attacks
                if not self.black_king_moved: # Short
                    if self.Get_Piece("77") == 16:
                        if self.Get_Piece("67") == 0 and self.Get_Piece("57") == 0:
                            Avaliable_Moves.append("67")
                        
                if not self.black_king_moved: # Long
                    if self.Get_Piece("07") == 16:
                        if self.Get_Piece("17") == 0 and self.Get_Piece("27") == 0 and self.Get_Piece("37") == 0:
                            Avaliable_Moves.append("27")
                self.Remove_Marked_White_Attacks()
        # Queen
        # Queen move = King move + Bishop move + Rook move
        if Moving_Piece == 2 or Moving_Piece == 8:
            Avaliable_Moves = list(dict.fromkeys(Avaliable_Moves)) # Remove duplicated moves
        return Avaliable_Moves

    def Find_Piece(self,Piece_Id:int) -> str:
        for i in range(8):
            for j in range(8):
                Coord = str(i) + str(j)
                if self.Get_Piece(Coord) == Piece_Id:
                    return Coord
        return "-1"

    def Is_White_Checking_Black(self) -> bool:
        Black_King_Coord = self.Find_Piece(7)
        for i in range(8):
            for j in range(8):
                Coord = str(i) + str(j)
                if self.Is_White_Piece(Coord):
                    Avaliable_Move = self.Avaliable_Moves(Coord, False)
                    #print(Black_King_Coord,"Avaliable: ",Avaliable_Move)
                    if Avaliable_Move.count(Black_King_Coord) >= 1:
                        return True
        return False

    def Is_Black_Checking_White(self) -> bool:
        White_King_Coord = self.Find_Piece(1)
        for i in range(8):
            for j in range(8):
                Coord = str(i) + str(j)
                if not self.Is_White_Piece(Coord):
                    Avaliable_Move = self.Avaliable_Moves(Coord, False)
                    if Avaliable_Move.count(White_King_Coord) >= 1:
                        return True
        return False

    def Mark_All_White_Attacks(self) -> None:
        Total_Attacks = []
        for i in range(8):
            for j in range(8):
                Coord = str(i) + str(j)
                if self.Is_White_Piece(Coord):
                    if self.Get_Piece(Coord) == 6 or self.Get_Piece(Coord) == 13: # Pawn Special attack
                        Attacks = []
                        Left_Diagonal = str(int(Coord[0])-1)+str(int(Coord[1])+1)
                        Right_Diagonal = str(int(Coord[0])+1)+str(int(Coord[1])+1)
                        if self.Is_Coord_Valid(Left_Diagonal):
                            Attacks.append(Left_Diagonal)
                        if self.Is_Coord_Valid(Right_Diagonal):
                            Attacks.append(Right_Diagonal)
                    else:
                        Attacks = self.Avaliable_Moves(Coord, Check=False)
                    for attack in Attacks:
                        if self.Is_Empty(attack):
                            Total_Attacks.append(attack)
        Total_Attacks = list(dict.fromkeys(Total_Attacks)) # Remove duplicated moves
        for attack in Total_Attacks:
            self.Replace_Piece(attack,17)

    def Remove_Marked_White_Attacks(self) -> None:
        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] == 17:
                    self.chessboard[i][j] = 0

    def Mark_All_Black_Attacks(self) -> None:
        Total_Attacks = []
        for i in range(8):
            for j in range(8):
                Coord = str(i) + str(j)
                if not self.Is_White_Piece(Coord):
                    if self.Get_Piece(Coord) == 12 or self.Get_Piece(Coord) == 14: # Pawn Special attack
                        Attacks = []
                        Left_Diagonal = str(int(Coord[0])-1)+str(int(Coord[1])-1)
                        Right_Diagonal = str(int(Coord[0])+1)+str(int(Coord[1])-1)
                        if self.Is_Coord_Valid(Left_Diagonal):
                            Attacks.append(Left_Diagonal)
                        if self.Is_Coord_Valid(Right_Diagonal):
                            Attacks.append(Right_Diagonal)
                    else:
                        Attacks = self.Avaliable_Moves(Coord, Check=False)
                    for attack in Attacks:
                        if self.Is_Empty(attack):
                            Total_Attacks.append(attack)
        Total_Attacks = list(dict.fromkeys(Total_Attacks)) # Remove duplicated moves
        for attack in Total_Attacks:
            self.Replace_Piece(attack,18)

    def Remove_Marked_Black_Attacks(self) -> None:
        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] == 18:
                    self.chessboard[i][j] = 0

    def Legal_Moves(self,Piece_Coordinate:str) -> list:
        if self.Get_Piece(Piece_Coordinate) == 1:
            self.Mark_All_Black_Attacks()
        if self.Get_Piece(Piece_Coordinate) == 7:
            self.Mark_All_White_Attacks()
        Avaliable_Move = self.Avaliable_Moves(Piece_Coordinate, False)
        self.Remove_Marked_Black_Attacks()
        self.Remove_Marked_White_Attacks()

        moving_black = self.Is_Black_Piece(Piece_Coordinate)
        moving_white = self.Is_White_Piece(Piece_Coordinate)

        Legal_Move = []
        for move in Avaliable_Move:
            Pre_Move = self.Get_Piece(move)
            Moving_Piece = self.Get_Piece(Piece_Coordinate)
            self.Replace_Piece(move,Moving_Piece)
            self.Replace_Piece(Piece_Coordinate,0)
            if not self.white_move:
                if moving_black:
                    if not self.Is_White_Checking_Black():
                        Legal_Move.append(move)
                if moving_white:
                    if not self.Is_Black_Checking_White():
                        Legal_Move.append(move)
            if self.white_move:
                if moving_white:
                    if not self.Is_Black_Checking_White():
                        Legal_Move.append(move)
                if moving_black:
                    if not self.Is_White_Checking_Black():
                        Legal_Move.append(move)
            self.Replace_Piece(move,Pre_Move)
            self.Replace_Piece(Piece_Coordinate,Moving_Piece)
        return Legal_Move

    def Move(self,Piece_Position:str, Pre_Defined_Move = "", Translate_Position = True, Auto_Promote = 0):
        if Translate_Position:
            Piece_Coordinate = self.Piece_Position_To_Coordinate(Piece_Position)
        else:
            Piece_Coordinate = Piece_Position

        if self.white_move:
            print("White's turn")
            Piece = self.Get_Piece(Piece_Coordinate)
            if Piece == 7 or Piece == 8 or Piece == 9 or Piece == 10 or Piece == 11 or Piece == 12 or Piece == 14 or Piece == 16:
                input("You can only move your own pieces!")
                self.moves.pop()
                return
        if not self.white_move:
            print("Black's turn")
            Piece = self.Get_Piece(Piece_Coordinate)
            if Piece == 1 or Piece == 2 or Piece == 3 or Piece == 4 or Piece == 5 or Piece == 6 or Piece == 13 or Piece == 15:
                input("You can only move your own pieces!")
                self.moves.pop()
                return
        #
        if Piece_Coordinate == "Invalid":
            input("You cannot move this piece!")
            self.moves.pop()
            return

        # Mark avaliable moves
        Avaliable_Move = self.Legal_Moves(Piece_Coordinate)

            # Mark en passant red
        if self.Get_Piece(Piece_Coordinate) == 6:
            if Piece_Coordinate[1] == "4":
                Left = str(int(Piece_Coordinate[0]) - 1) + Piece_Coordinate[1]
                if self.Get_Piece(Left) == 14:
                    self.Replace_Piece(Left,f"\033[91m{self.Get_Piece(Left)}\033[0m")
                Right = str(int(Piece_Coordinate[0]) + 1) + Piece_Coordinate[1]
                if self.Get_Piece(Right) == 14:
                    self.Replace_Piece(Right,f"\033[91m{self.Get_Piece(Right)}\033[0m")

        if self.Get_Piece(Piece_Coordinate) == 12:
            if Piece_Coordinate[1] == "3":
                Left = str(int(Piece_Coordinate[0]) - 1) + Piece_Coordinate[1]
                if self.Get_Piece(Left) == 13:
                    self.Replace_Piece(Left,f"\033[91m{self.Get_Piece(Left)}\033[0m")
                Right = str(int(Piece_Coordinate[0]) + 1) + Piece_Coordinate[1]
                if self.Get_Piece(Right) == 13:
                    self.Replace_Piece(Right,f"\033[91m{self.Get_Piece(Right)}\033[0m")

        self.Replace_Piece(Piece_Coordinate,f"\033[92m{self.Get_Piece(Piece_Coordinate)}\033[0m") # Mark moving piece green
        for move in Avaliable_Move:
            if self.Is_Empty(move):
                self.Replace_Piece(move,"X")
            else:
                self.Replace_Piece(move,f"\033[91m{self.Get_Piece(move)}\033[0m") # Mark avaliable captures red

        self.printboard(True)
        
        # Reset board
        for i in range(8):
            for j in range(8):
                Piece = self.chessboard[i][j]
                if Piece == "X":
                    self.chessboard[i][j] = 0
                if type(Piece) == str:
                    if len(Piece) > 2:
                        self.chessboard[i][j] = int(Piece[5:-4])
        if Pre_Defined_Move == "":
            Target_Coordinate = self.Piece_Position_To_Coordinate(input("To "))
        else:
            Target_Coordinate = Pre_Defined_Move
        if Target_Coordinate == "Invalid":
            input("Move cancelled!")
            self.moves.pop()
            return

        if len(self.moves[-1]) == 2:
            self.moves[-1] += Target_Coordinate

        # Move piece
        if Avaliable_Move.count(Target_Coordinate) >= 1:
            # Pawn Promotion
            if self.Get_Piece(Piece_Coordinate) == 6: # White
                if Target_Coordinate[1] == "7":
                    print("Pawn Promotion: \n1: ♛ \n2: ♞ \n3: ♝ \n4: ♜")
                    try:
                        Selection = int(input("Promote to: "))
                    except ValueError:
                        Selection = 1
                    if Auto_Promote != 0:
                        Selection = Auto_Promote
                    if Selection == 1:
                        self.Replace_Piece(Piece_Coordinate,2)
                    elif Selection == 2:
                        self.Replace_Piece(Piece_Coordinate,4)
                    elif Selection == 3:
                        self.Replace_Piece(Piece_Coordinate,3)
                    elif Selection == 4:
                        self.Replace_Piece(Piece_Coordinate,5)
                    else:
                        self.Replace_Piece(Piece_Coordinate,2)
                    self.moves[-1] += str(Selection)
            if self.Get_Piece(Piece_Coordinate) == 12: # Black
                if Target_Coordinate[1] == "0":
                    print("Pawn Promotion: \n1: ♕ \n2: ♘ \n3: ♗ \n4: ♖")
                    try:
                        Selection = int(input("Promote to: "))
                    except ValueError:
                        Selection = 1
                    if Auto_Promote != 0:
                        Selection = Auto_Promote
                    if Selection == 1:
                        self.Replace_Piece(Piece_Coordinate,8)
                    elif Selection == 2:
                        self.Replace_Piece(Piece_Coordinate,10)
                    elif Selection == 3:
                        self.Replace_Piece(Piece_Coordinate,9)
                    elif Selection == 4:
                        self.Replace_Piece(Piece_Coordinate,11)
                    else:
                        self.Replace_Piece(Piece_Coordinate,8)
                    self.moves[-1] += str(Selection)
            
            self.Replace_Piece(Target_Coordinate,self.Get_Piece(Piece_Coordinate))
            # Special moves

            # Enable En passant
            if self.Get_Piece(Piece_Coordinate) == 6:
                if Target_Coordinate[1] == "3":
                    self.Replace_Piece(Target_Coordinate,13)

            if self.Get_Piece(Piece_Coordinate) == 12:
                if Target_Coordinate[1] == "4":
                    self.Replace_Piece(Target_Coordinate,14)

            # En passant capture
            if self.Get_Piece(Piece_Coordinate) == 6:
                if Piece_Coordinate[1] == "4":
                    Left = str(int(Piece_Coordinate[0]) - 1) + Piece_Coordinate[1]
                    if self.Get_Piece(Left) == 14:
                        if Target_Coordinate == Left[0] + str(int(Left[1]) + 1):
                            self.Replace_Piece(Left,0)
                    Right = str(int(Piece_Coordinate[0]) + 1) + Piece_Coordinate[1]
                    if self.Get_Piece(Right) == 14:
                        if Target_Coordinate == Right[0] + str(int(Right[1]) + 1):
                            self.Replace_Piece(Right,0)

            if self.Get_Piece(Piece_Coordinate) == 12:
                if Piece_Coordinate[1] == "3":
                    Left = str(int(Piece_Coordinate[0]) - 1) + Piece_Coordinate[1]
                    if self.Get_Piece(Left) == 13:
                        if Target_Coordinate == Left[0] + str(int(Left[1]) - 1):
                            self.Replace_Piece(Left,0)
                    Right = str(int(Piece_Coordinate[0]) + 1) + Piece_Coordinate[1]
                    if self.Get_Piece(Right) == 13:
                        if Target_Coordinate == Right[0] + str(int(Right[1]) - 1):
                            self.Replace_Piece(Right,0)
            
            # Disable rook to castle if moved
            if self.Get_Piece(Piece_Coordinate) == 15:
                self.Replace_Piece(Target_Coordinate,5)
            if self.Get_Piece(Piece_Coordinate) == 16:
                self.Replace_Piece(Target_Coordinate,11)
            
            if self.Get_Piece(Piece_Coordinate) == 1:
                self.white_king_moved = True
            if self.Get_Piece(Piece_Coordinate) == 7:
                self.black_king_moved = True

            # Castling
            if self.Get_Piece(Piece_Coordinate) == 1: # White
                if Target_Coordinate == "20":
                    self.Replace_Piece("00",0)
                    self.Replace_Piece("30",5)
                elif Target_Coordinate == "60":
                    self.Replace_Piece("70",0)
                    self.Replace_Piece("50",5)
            elif self.Get_Piece(Piece_Coordinate) == 7: # Black
                if Target_Coordinate == "27":
                    self.Replace_Piece("07",0)
                    self.Replace_Piece("37",11)
                elif Target_Coordinate == "67":
                    self.Replace_Piece("77",0)
                    self.Replace_Piece("57",11)

            self.Replace_Piece(Piece_Coordinate,0)
        else:
            return
        
        # Check checkmate
        if self.white_move:
            if self.Is_White_Checking_Black():
                Is_Checkmate = True
                self.white_move = False
                for i, j in ((i, j) for i in range(8) for j in range(8)):
                    Coord = str(i) + str(j)
                    if not self.Is_White_Piece(Coord):
                        Avaliable_Move = self.Legal_Moves(Coord)
                        if len(Avaliable_Move) != 0:
                            Is_Checkmate = False
                            break
                if Is_Checkmate:
                    self.game_result = "White win by checkmate!"
                    self.Playing = False
                self.white_move = True
            else:
                Is_Stalemate = True
                self.white_move = False
                for i, j in ((i, j) for i in range(8) for j in range(8)):
                    Coord = str(i) + str(j)
                    if not self.Is_White_Piece(Coord):
                        Avaliable_Move = self.Legal_Moves(Coord)
                        if len(Avaliable_Move) != 0:
                            Is_Stalemate = False
                            break
                if Is_Stalemate:
                    self.game_result = "White drew by stalemate!"
                    self.Playing = False
                self.white_move = True
        elif not self.white_move:
            if self.Is_Black_Checking_White():
                Is_Checkmate = True
                self.white_move = True
                for i, j in ((i, j) for i in range(8) for j in range(8)):
                    Coord = str(i) + str(j)
                    if self.Is_White_Piece(Coord):
                        Avaliable_Move = self.Legal_Moves(Coord)
                        if len(Avaliable_Move) != 0:
                            Is_Checkmate = False
                            break
                if Is_Checkmate:
                    self.game_result = "Black win by checkmate!"
                    self.Playing = False
                self.white_move = False
            else:
                Is_Stalemate = True
                self.white_move = True
                for i, j in ((i, j) for i in range(8) for j in range(8)):
                    Coord = str(i) + str(j)
                    if self.Is_White_Piece(Coord):
                        Avaliable_Move = self.Legal_Moves(Coord)
                        if len(Avaliable_Move) != 0:
                            Is_Stalemate = False
                            break
                if Is_Stalemate:
                    self.game_result = "Black drew by stalemate!"
                    self.Playing = False
                self.white_move = False
        # Castle
        self.white_move = not self.white_move
    
    def Load_Position(self, play_mode=False, time_per_move=1) -> None:
        """
        This function loads position from the moves given.
        """

        self.chessboard = [[0 for g in range(8)] for i in range(8)]
        self.white_move = True
        self.black_king_moved = False
        self.white_king_moved = False
        self.Playing = True
        self.game_result = ""
        self.initializeboard()

        #input(self.moves)
        if play_mode:
            for move in self.moves:
                if type(move) != list:
                    sleep(time_per_move)
                    clear()
                    if len(move) == 4:
                        self.Move(Piece_Position=move[0]+move[1],Pre_Defined_Move=move[2]+move[3], Translate_Position=False)
                    else:
                        self.Move(Piece_Position=move[0]+move[1],Pre_Defined_Move=move[2]+move[3], Translate_Position=False, Auto_Promote=move[4])
        else:
            for move in self.moves:
                if type(move) != list:
                    if len(move) == 4:
                        self.Move(Piece_Position=move[0]+move[1],Pre_Defined_Move=move[2]+move[3], Translate_Position=False)
                    else:
                        self.Move(Piece_Position=move[0]+move[1],Pre_Defined_Move=move[2]+move[3], Translate_Position=False, Auto_Promote=move[4])

    def Piece_Value(self,piece_id: int) -> int:
        """
        Returns a pieces value
        """
        VALUE = {
            0 : 0,
            1 : 0,
            2 : 9,
            3 : 3,
            4 : 3,
            5 : 5,
            6 : 1,
            7 : 0,
            8 : 9,
            9 : 3,
            10: 3,
            11: 5,
            12: 1,
            13: 1,
            14: 1,
            15: 5,
            16: 5
        }

        return VALUE[piece_id]

    def Is_Same_Type(self,piece_id:int, piece_id2:int) -> bool:
        TYPE = {
            1 : 1,
            2 : 2,
            3 : 3,
            4 : 4,
            5 : 5,
            6 : 6,
            7 : 1,
            8 : 2,
            9 : 3,
            10: 4,
            11: 5,
            12: 6,
            13: 6,
            14: 6,
            15: 5,
            16: 5
        }
        if TYPE[piece_id] == TYPE[piece_id2]:
            return True
        return False

    def Is_Draw_By_Repetition(self) -> bool:
        """
        This function enables the rule draw by repetition.
        """
        pass

    def Previous_Move(self) -> None:
        if self.Current_Move_Index == 0:
            self.Current_Move_Index = len(self.moves)
            self.Load_Position(False)
        else:
            self.Current_Move_Index -= 1
            coord = self.moves[self.Current_Move_Index]
            pass

    def user_interface(self) -> None:
        clear()
        if self.white_move:
            print("White's turn")
        else:
            print("Black's turn")

        # Disable unused En passant after a round
        if self.white_move:
            for i in range(8):
                Piece = self.chessboard[i][3]
                if Piece == 13:
                    self.chessboard[i][3] = 6
        if not self.white_move:
            for i in range(8):
                Piece = self.chessboard[i][4]
                if Piece == 14:
                    self.chessboard[i][4] = 12

        self.printboard(True)

        # Reset board
        for i in range(8):
            for j in range(8):
                Piece = self.chessboard[i][j]
                if Piece == "X":
                    self.chessboard[i][j] = 0
                if type(Piece) == str:
                    if len(Piece) > 2:
                        self.chessboard[i][j] = int(Piece[5:-4])
        #

        Move_Piece = input("Move chess piece on ")

        #Special command:

        if Move_Piece == "/analysis":
            self.Analysis_Mode = True
            self.Current_Move_Index = len(self.moves)
            return

        if Move_Piece == "/pop": # 
            self.moves.pop()
            self.Load_Position()
            return
        elif Move_Piece == "/play":
            self.Load_Position(True)
            return
        elif Move_Piece == "/mba":
            self.Mark_All_Black_Attacks()
            return
        elif Move_Piece == "/mwa":
            self.Mark_All_White_Attacks()
            return
        elif Move_Piece == "/moves":
            print(self.moves)
            input("Press Enter to continue...")
            return

        #
        self.moves.append(self.Piece_Position_To_Coordinate(Move_Piece))
        clear()
        self.Move(Move_Piece)

    def start_game(self) -> None:

        self.chessboard = [[0 for g in range(8)] for i in range(8)]
        self.white_move = True
        self.black_king_moved = False
        self.white_king_moved = False
        self.Playing = True
        self.game_result = ""

        clear()
        self.initializeboard()

        while self.Playing:
            self.user_interface()
        clear()
        self.printboard(True)
        print(self.game_result)

A_Chess_Game = pychess()
A_Chess_Game.start_game()