import os

from .side import Side

from abc import ABC, abstractmethod
class Piece:

    transparentImg = os.path.join("assets", "img", "pieces", "transparent_img.png")

    def __init__(self, side):
        self.side = side

    def isValidCoordinate(self, BOARD_SIZE, x, y):
        if x <= BOARD_SIZE - 1 and x >= 0 and y <= BOARD_SIZE - 1 and y >= 0:
            return True
    
        return False


from .side import Side
class Pawn(Piece):

    blackImg = os.path.join("assets", "img", "pieces", "black_pawn.png")
    whiteImg = os.path.join("assets", "img", "pieces", "white_pawn.png")

    def __init__(self, side):
        super().__init__(side)
        
        if side == Side.BLACK:
            self.img = Pawn.blackImg
        else:
            self.img = Pawn.whiteImg
        self.moveSet = []
       
            
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
            
        self.printMoveSet(self.moveSet)

        return self.moveSet
    

    #for test only
    def printMoveSet(self, moveSet):
        for item in moveSet:
            print(item)
    
