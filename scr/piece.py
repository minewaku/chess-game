import os

from copy import deepcopy
from .side import Side
from abc import ABC, abstractmethod
class Piece:

    transparentImg = os.path.join("assets", "img", "pieces", "transparent_img.png")

    def __init__(self, side, moveSet):
        self.side = side
        self.moveSet = moveSet
        self.moveCount = 0


    # Checking if this move is valid or not (check if it still in range of board)
    def isValidCoordinate(self, BOARD_SIZE, x, y):
        if x <= BOARD_SIZE - 1 and x >= 0 and y <= BOARD_SIZE - 1 and y >= 0:
            return True
    
        return False
    

    #check if as there is an move that can attack enemies king. True if it can attack that king
    def isCheckMate(self, board):
        for move in self.moveSet:
            x, y = move
            if isinstance(board.board[x][y].point.piece, King):
                return True
            
        return False
    
    # check if the piece on the square is in attack range of enemies or not
    # def isInDanger(self, square, board):
    #     for i, row in enumerate(board.board):
    #         for j, col in enumerate(row):
    #             if board.board[i][j].point.piece != None and board.board[i][j].point.piece.side != square.point.piece.side:
    #                 moveSet = board.board[i][j].point.piece.generateMoveSet(board, i, j)
    #                 for move in moveSet:
    #                     x, y = move
    #                     if x == square.point.x and y == square.point.y:
    #                         return True
            
    #     return False
    
    def isInDanger(self, square, side, board):
        for i, row in enumerate(board.board):
            for j, col in enumerate(row):
                if board.board[i][j].point.piece != None and board.board[i][j].point.piece.side != side and i != square.point.x and j != square.point.y: 
                    moveSet = board.board[i][j].point.piece.generateMoveSet(board=board, originX=i, originY=j)
                    for move in moveSet:
                        x, y = move
                        if x == square.point.x and y == square.point.y:
                            return True

        return False

    # unused method
    def removeSuicideMove(self, originX, originY, moveSet, board):
        suicideMove = []
        for move in moveSet:
            finalX, finalY = move
            board.selectedSquare = board.board[originX][originY]
            board.doMove(square=board.board[finalX][finalY])
            if board.checkCheckMateForAllPieces(side=self.side):
                suicideMove.append(move)

            board.undoMove()

        for move in suicideMove:
            self.moveSet.remove(move)

            # print(f"{board.board[originX][originY].point.piece} move from {(originX, originY)} to {(finalX, finalY)}")

        return self.moveSet


from .side import Side
class Pawn(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_pawn.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_pawn.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = Pawn.blackImg
        else:
            self.img = Pawn.whiteImg
       
            
    # create bunch of moves without thinking about how valid they are. Using isValidCoordinate method for each move
    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []

        # just moving pattern of this type of piece
        if self.side == Side.WHITE:
            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY) and board.board[originX - 1][originY].point.piece == None:
                self.moveSet.append((originX - 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY - 1) and board.board[originX - 1][originY - 1].point.piece != None and board.board[originX - 1][originY - 1].point.piece.side != self.side:
                self.moveSet.append((originX - 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY + 1) and board.board[originX - 1][originY + 1].point.piece != None and board.board[originX - 1][originY + 1].point.piece.side != self.side:
                self.moveSet.append((originX - 1, originY + 1))
            
            if originX == 6 and board.board[originX - 1][originY].point.piece == None and board.board[originX - 2][originY].point.piece == None:
                self.moveSet.append((originX - 2, originY))


        elif self.side == Side.BLACK:
            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY) and board.board[originX + 1][originY].point.piece == None:
                self.moveSet.append((originX + 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY - 1) and board.board[originX + 1][originY - 1].point.piece != None and board.board[originX + 1][originY - 1].point.piece.side != self.side:
                self.moveSet.append((originX + 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY + 1) and board.board[originX + 1][originY + 1].point.piece != None and board.board[originX + 1][originY + 1].point.piece.side != self.side:
                self.moveSet.append((originX + 1, originY + 1))
            
            if originX == 1 and  board.board[originX + 1][originY].point.piece == None and board.board[originX + 2][originY].point.piece == None:
                self.moveSet.append((originX + 2, originY))
            
        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet
    


from .side import Side
class Queen(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_queen.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_queen.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = Queen.blackImg
        else:
            self.img = Queen.whiteImg


    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []
        #diagonal
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY - i): 
                if board.board[originX - i][originY - i].point.piece != None:
                    if board.board[originX - i][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY - i))
            else:
                break

        for i in range(1, 8):        
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY + i): 
                if board.board[originX - i][originY + i].point.piece != None:
                    if board.board[originX - i][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY + i))
            else:
                break

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY - i): 
                if board.board[originX + i][originY - i].point.piece != None:
                    if board.board[originX + i][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY - i))
            else:
                break        

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY + i): 
                if board.board[originX + i][originY + i].point.piece != None:
                    if board.board[originX + i][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY + i))
            else:
                break


        #vertical
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY):
                if board.board[originX + i][originY].point.piece != None:
                    if board.board[originX + i][originY].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY))
            else:
                break

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY):
                if board.board[originX - i][originY].point.piece != None: 
                    if board.board[originX - i][originY].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY))
            else:
                break


        #horizontal
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX, originY + i): 
                if board.board[originX][originY + i].point.piece != None:
                    if board.board[originX][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX, originY + i))

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX, originY - i): 
                if board.board[originX][originY - i].point.piece != None:
                    if board.board[originX][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX, originY - i))

        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet



from .side import Side
class Horse(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_horse.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_horse.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = Horse.blackImg
        else:
            self.img = Horse.whiteImg


    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []

        # just moving pattern of this type of piece
        if self.isValidCoordinate(board.BOARD_SIZE, originX + 2, originY - 1):
            if board.board[originX + 2][originY - 1].point.piece != None:
                if board.board[originX + 2][originY - 1].point.piece.side != self.side:
                    self.moveSet.append((originX + 2, originY - 1))
            else:
                self.moveSet.append((originX + 2, originY - 1))


        if self.isValidCoordinate(board.BOARD_SIZE, originX + 2, originY + 1):
            if board.board[originX + 2][originY + 1].point.piece != None:
                if board.board[originX + 2][originY + 1].point.piece.side != self.side:
                    self.moveSet.append((originX + 2, originY + 1))
            else:
                self.moveSet.append((originX + 2, originY + 1))


        if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY + 2):
            if board.board[originX + 1][originY + 2].point.piece != None:
                if board.board[originX + 1][originY + 2].point.piece.side != self.side:
                    self.moveSet.append((originX + 1, originY + 2))
            else:
                self.moveSet.append((originX + 1, originY + 2))


        if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY + 2):
            if board.board[originX - 1][originY + 2].point.piece != None:
                if board.board[originX - 1][originY + 2].point.piece.side != self.side:
                    self.moveSet.append((originX - 1, originY + 2))
            else:
                self.moveSet.append((originX - 1, originY + 2))

        
        if self.isValidCoordinate(board.BOARD_SIZE, originX - 2, originY + 1):
            if board.board[originX - 2][originY + 1].point.piece != None:
                if board.board[originX - 2][originY + 1].point.piece.side != self.side:
                    self.moveSet.append((originX - 2, originY + 1))
            else:
                self.moveSet.append((originX - 2, originY + 1))  


        if self.isValidCoordinate(board.BOARD_SIZE, originX - 2, originY - 1):
            if board.board[originX - 2][originY - 1].point.piece != None:
                if board.board[originX - 2][originY - 1].point.piece.side != self.side:
                    self.moveSet.append((originX - 2, originY - 1))
            else:
                self.moveSet.append((originX - 2, originY - 1))      


        if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY - 2):
            if board.board[originX - 1][originY - 2].point.piece != None:
                if board.board[originX - 1][originY - 2].point.piece.side != self.side:
                    self.moveSet.append((originX - 1, originY - 2))
            else:
                self.moveSet.append((originX - 1, originY - 2))     


        if self.isValidCoordinate(board.BOARD_SIZE, originX  + 1, originY - 2):
            if board.board[originX + 1][originY - 2].point.piece != None:
                if board.board[originX  + 1][originY - 2].point.piece.side != self.side:
                    self.moveSet.append((originX  + 1, originY - 2))
            else:
                self.moveSet.append((originX  + 1, originY - 2))     
            
        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet



from .side import Side
class Bishop(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_bishop.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_bishop.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = Bishop.blackImg
        else:
            self.img = Bishop.whiteImg


    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []

        # just moving pattern of this type of piece
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY - i): 
                if board.board[originX - i][originY - i].point.piece != None:
                    if board.board[originX - i][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY - i))
            else:
                break

        for i in range(1, 8):        
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY + i): 
                if board.board[originX - i][originY + i].point.piece != None:
                    if board.board[originX - i][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY + i))
            else:
                break

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY - i): 
                if board.board[originX + i][originY - i].point.piece != None:
                    if board.board[originX + i][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY - i))
            else:
                break        

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY + i): 
                if board.board[originX + i][originY + i].point.piece != None:
                    if board.board[originX + i][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY + i))
            else:
                break
            
        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet



from .side import Side
class Rook(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_rook.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_rook.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = Rook.blackImg
        else:
            self.img = Rook.whiteImg


    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []
        
        #vertical
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX + i, originY):
                if board.board[originX + i][originY].point.piece != None:
                    if board.board[originX + i][originY].point.piece.side != self.side:
                        self.moveSet.append((originX + i, originY))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX + i, originY))
            else:
                break

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX - i, originY):
                if board.board[originX - i][originY].point.piece != None: 
                    if board.board[originX - i][originY].point.piece.side != self.side:
                        self.moveSet.append((originX - i, originY))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX - i, originY))
            else:
                break


        #horizontal
        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX, originY + i): 
                if board.board[originX][originY + i].point.piece != None:
                    if board.board[originX][originY + i].point.piece.side != self.side:
                        self.moveSet.append((originX, originY + i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX, originY + i))

        for i in range(1, 8):
            if self.isValidCoordinate(board.BOARD_SIZE, originX, originY - i): 
                if board.board[originX][originY - i].point.piece != None:
                    if board.board[originX][originY - i].point.piece.side != self.side:
                        self.moveSet.append((originX, originY - i))
                        break
                    else:
                        break
                else:
                    self.moveSet.append((originX, originY - i))

        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet



from .side import Side
class King(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_king.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_king.png")

    def __init__(self, side):
        super().__init__(side=side, moveSet=[])
        
        if side == Side.BLACK:
            self.img = King.blackImg
        else:
            self.img = King.whiteImg
       
            
    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []
        if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY + 1):
            if board.board[originX - 1][originY + 1].point.piece != None:
                if board.board[originX - 1][originY + 1].point.piece.side != self.side:
                    self.moveSet.append((originX - 1, originY + 1))
            else:
                self.moveSet.append((originX - 1, originY + 1))

        if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY - 1):
            if board.board[originX - 1][originY - 1].point.piece != None:
                if board.board[originX - 1][originY - 1].point.piece.side != self.side:
                    self.moveSet.append((originX - 1, originY - 1))
            else:
                self.moveSet.append((originX - 1, originY - 1))

        if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY - 1):
            if board.board[originX + 1][originY - 1].point.piece != None:
                if board.board[originX + 1][originY - 1].point.piece.side != self.side:
                    self.moveSet.append((originX + 1, originY - 1))
            else:
                self.moveSet.append((originX + 1, originY - 1))

        if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY + 1):
            if board.board[originX + 1][originY + 1].point.piece != None:
                if board.board[originX + 1][originY + 1].point.piece.side != self.side:
                    self.moveSet.append((originX + 1, originY + 1))
            else:
                self.moveSet.append((originX + 1, originY + 1))


        if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY):
            if board.board[originX + 1][originY].point.piece != None:
                if board.board[originX + 1][originY].point.piece.side != self.side:
                    self.moveSet.append((originX + 1, originY))
            else:
                self.moveSet.append((originX + 1, originY))


        if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY):
            if board.board[originX - 1][originY].point.piece != None:
                if board.board[originX - 1][originY].point.piece.side != self.side:
                    self.moveSet.append((originX - 1, originY))
            else:
                self.moveSet.append((originX - 1, originY))


        if self.isValidCoordinate(board.BOARD_SIZE, originX, originY + 1):
            if board.board[originX][originY + 1].point.piece != None:
                if board.board[originX][originY + 1].point.piece.side != self.side:
                    self.moveSet.append((originX, originY + 1))
            else:
                self.moveSet.append((originX, originY + 1))


        if self.isValidCoordinate(board.BOARD_SIZE, originX, originY - 1):
            if board.board[originX][originY - 1].point.piece != None:
                if board.board[originX][originY - 1].point.piece.side != self.side:
                    self.moveSet.append((originX, originY - 1))
            else:
                self.moveSet.append((originX, originY - 1))

        # castling
        if self.moveCount == 0:
            if self.side == Side.WHITE and board.turn.side == Side.BLACK:
                if not self.isInDanger(square=board.board[originX][originY], side=Side.WHITE, board=board):
                    if board.board[7][0].point.piece != None and board.board[7][0].point.piece.moveCount == 0:
                        if board.board[7][1].point.piece == None and not self.isInDanger(square=board.board[7][1], side=Side.WHITE, board=board) and board.board[7][2].point.piece == None and not self.isInDanger(square=board.board[7][2], side=Side.WHITE, board=board) and board.board[7][3].point.piece == None and not self.isInDanger(square=board.board[7][3], side=Side.WHITE, board=board):
                            self.moveSet.append(((originX, originY - 2)))

                    if board.board[7][7].point.piece != None and board.board[7][7].point.piece.moveCount == 0:
                        if board.board[7][5].point.piece == None and not self.isInDanger(square=board.board[7][5], side=Side.WHITE, board=board) and board.board[7][6].point.piece == None and not self.isInDanger(square=board.board[7][6], side=Side.WHITE, board=board):
                            self.moveSet.append(((originX, originY + 2)))
                
            elif self.side == Side.BLACK and board.turn.side == Side.WHITE:
                if not self.isInDanger(square=board.board[originX][originY], side=Side.BLACK, board=board):
                    if board.board[0][0].point.piece != None and board.board[0][0].point.piece.moveCount == 0:
                        if board.board[0][1].point.piece == None and not self.isInDanger(square=board.board[0][1], side=Side.BLACK, board=board) and board.board[0][2].point.piece == None and not self.isInDanger(square=board.board[0][2], side=Side.BLACK, board=board) and board.board[0][3].point.piece == None and not self.isInDanger(square=board.board[0][3], side=Side.BLACK, board=board):
                            self.moveSet.append(((originX, originY - 2)))

                    if board.board[0][7].point.piece != None and board.board[0][7].point.piece.moveCount == 0:
                        if board.board[0][5].point.piece == None and not self.isInDanger(square=board.board[0][5], side=Side.BLACK, board=board) and board.board[0][6].point.piece == None and not self.isInDanger(square=board.board[0][6], side=Side.BLACK, board=board):
                            self.moveSet.append(((originX, originY + 2)))

        # return self.removeSuicideMove(originX=originX, originY=originY, moveSet=self.moveSet, board=board)
        return self.moveSet

