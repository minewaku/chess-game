from piece import Piece

class Move:

    def __init__(self, originX: int, originY: int, finalX: int, finalY: int, piece = None, capturedPiece = None, isValid: bool = True):
        self.originX = originX
        self.originY = originY
        self.finalX = finalX
        self.finalY = finalY
        self.piece = piece
        self.capturedPiece = capturedPiece
        self.isValid = isValid

    def checkDirection(self):
        self.dx = self.finalX - self.originX
        self.dy = self.finalY - self.originY

        if self.dx == 0 and self.dy == 0:
            self.isStatic = False 

        if self.dx == 0 and self.dy != 0:
            self.isVertical = True
        
        if self.dx != 0 and self.dy == 0:
            self.isHorizontal = True

        if abs(self.dx) == abs(self.dy) and self.dx != 0:
            self.isDiagonal = True

    @property
    def dx(self):
        return self.dx

    @property
    def dy(self):
        return self.dy
    

    @property
    def isStatic(self):
        return self.isStatic
    
    @isStatic.setter
    def isStatic(self, isStatic):
        self.isStatic = isStatic


    @property
    def isVertical(self):
        return self.isVertial
    
    @isVertical.setter
    def isVertical(self, isVertical):
        self.isVertical = isVertical


    @property
    def isHorizontal(self):
        return self.isHorizontal
    
    @isHorizontal.setter
    def isHorizontal(self, isHorizontal):
        self.isHorizontal = isHorizontal


    @property
    def isDiagonal(self):
        return self.isDiagonal
    
    @isDiagonal.setter
    def isDiagonal(self, isDiagonal):
        self.isDiagonal = isDiagonal


    @property
    def isValid(self):
        return self.isValid
    
    @isValid.setter
    def isValid(self, isValid):
        self.isValid = isValid

        
    



