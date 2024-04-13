import os

from .side import Side

from abc import ABC, abstractmethod
class Piece:

    transparentImg = os.path.join("assets", "img", "pieces", "transparent_img.png")

    def __init__(self, side, moveSet):
        self.side = side
        self.moveSet = moveSet

    def isValidCoordinate(self, BOARD_SIZE, x, y):
        if x <= BOARD_SIZE - 1 and x >= 0 and y <= BOARD_SIZE - 1 and y >= 0:
            return True
    
        return False
    
    def isCheckMate(self, board):
        for move in self.moveSet:
            x, y = move
            if isinstance(board.board[x][y].point.piece, King):
                return True
            
        return False


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
       
            
    #create bunch of moves without thinking about how valid they are. Checking for later
    def generateMoveSet(self, board, originX, originY):
        self.moveSet = []
        if self.side == Side.BLACK:
            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY) and board.board[originX - 1][originY].point.piece == None:
                self.moveSet.append((originX - 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY - 1) and board.board[originX - 1][originY - 1].point.piece != None and board.board[originX - 1][originY - 1].point.piece.side != self.side:
                self.moveSet.append((originX - 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY + 1) and board.board[originX - 1][originY + 1].point.piece != None and board.board[originX - 1][originY + 1].point.piece.side != self.side:
                self.moveSet.append((originX - 1, originY + 1))
            
            if originX == 6:
                self.moveSet.append((originX - 2, originY))


        elif self.side == Side.WHITE:
            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY) and board.board[originX + 1][originY].point.piece == None:
                self.moveSet.append((originX + 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY - 1) and board.board[originX + 1][originY - 1].point.piece != None and board.board[originX + 1][originY - 1].point.piece.side != self.side:
                self.moveSet.append((originX + 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY + 1) and board.board[originX + 1][originY + 1].point.piece != None and board.board[originX + 1][originY + 1].point.piece.side != self.side:
                self.moveSet.append((originX + 1, originY + 1))
            
            if originX == 1 :
                self.moveSet.append((originX + 2, originY))

        return self.moveSet
    

    # #for test only
    # def printMoveSet(self, moveSet):
    #     for item in moveSet:
    #         print(item)
    


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
       
            
    #create bunch of moves without thinking about how valid they are. Checking for later
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

        return self.moveSet


