import os

from .side import Side

from abc import ABC, abstractmethod
class Piece:

    transparentImg = os.path.join("assets", "img", "pieces", "transparent_img.png")

    def __init__(self, side):
        self.side = side

    def isValidCoordinate(self, BOARD_SIZE, x, y):
        if x > BOARD_SIZE - 1 or y > BOARD_SIZE - 1:
            return False
    
        return True


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
       
            
    #create bunch of moves without thinking about how valid they are. Checking for later
    def generateMoveSet(self, side, board, originX, originY):
        moveSet = []
        if side == Side.BLACK:
            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY):
                moveSet.append((originX - 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY - 1) and board[originX - 1, originY - 1].point.piece != None and board[originX - 1, originY - 1].point.piece.side != self.side:
                moveSet.append((originX - 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX - 1, originY + 1) and board[originX - 1, originY + 1].point.piece != None and board[originX - 1, originY + 1].point.piece.side != self.side:
                moveSet.append((originX - 1, originY + 1))
            
            if originX == 6:
                moveSet.append((originX - 2, originY))


        elif side == Side.WHITE:
            moveSet.append((originX + 1, originY))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY - 1) and board[originX + 1, originY - 1].point.piece != None and board[originX + 1, originY - 1].point.piece.side != self.side:
                moveSet.append((originX + 1, originY - 1))

            if self.isValidCoordinate(board.BOARD_SIZE, originX + 1, originY + 1) and board[originX + 1, originY + 1].point.piece != None and board[originX + 1, originY + 1].point.piece.side != self.side:
                moveSet.append((originX + 1, originY + 1))
            
            if originX == 1 :
                moveSet.append((originX + 2, originY))
            
        return moveSet
    
