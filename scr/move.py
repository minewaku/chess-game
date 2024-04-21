from scr.piece import Piece

class Move:
    # each Move's instance stored a move history which is stored in a log array of the match

    def __init__(self, originX: int, originY: int, finalX: int, finalY: int, piece = None, capturedPiece = None):
        self.originX = originX
        self.originY = originY
        self.finalX = finalX
        self.finalY = finalY
        self.piece = piece
        self.capturedPiece = capturedPiece

        
    



