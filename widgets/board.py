import sys

sys.path.append('../')
from scr.point import Point
from scr.piece import Piece
from scr.piece import Pawn
from scr.point import Point
from scr.side import Side

from kivy.uix.gridlayout import GridLayout
from .square import Square

class Board(GridLayout):

    BOARD_SIZE = 8
    
    def __init__(self, player1, player2, square_size, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.square_size = square_size
    
        self.board = [[None] * Board.BOARD_SIZE for _ in range(Board.BOARD_SIZE)]
        self.player2 = player1
        self.player1 = player2
        self.logger = []

        self.turn = player1
        self.selectedSquare = None

        self.initializeComponents()
        self.renderVisual()


    def initializeComponents(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#e2aa23", size_hint=(None, None), size=(self.square_size, self.square_size))
                    else:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#fffbe8", size_hint=(None, None), size=(self.square_size, self.square_size))
                else:
                    if j % 2 == 0:  
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#fffbe8", size_hint=(None, None), size=(self.square_size, self.square_size))
                    else:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#e2aa23", size_hint=(None, None), size=(self.square_size, self.square_size))

                self.add_widget(self.board[i][j])


        self.board[1][0].point.piece = Pawn(Side.WHITE) 
        self.board[1][1].point.piece = Pawn(Side.WHITE) 
        self.board[1][2].point.piece = Pawn(Side.WHITE) 
        self.board[1][3].point.piece = Pawn(Side.WHITE) 
        self.board[1][4].point.piece = Pawn(Side.WHITE) 
        self.board[1][5].point.piece = Pawn(Side.WHITE) 
        self.board[1][6].point.piece = Pawn(Side.WHITE) 
        self.board[1][7].point.piece = Pawn(Side.WHITE) 

        self.board[6][0].point.piece = Pawn(Side.BLACK) 
        self.board[6][1].point.piece = Pawn(Side.BLACK) 
        self.board[6][2].point.piece = Pawn(Side.BLACK) 
        self.board[6][3].point.piece = Pawn(Side.BLACK) 
        self.board[6][4].point.piece = Pawn(Side.BLACK) 
        self.board[6][5].point.piece = Pawn(Side.BLACK) 
        self.board[6][6].point.piece = Pawn(Side.BLACK) 
        self.board[6][7].point.piece = Pawn(Side.BLACK) 

    def renderVisual(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                self.board[i][j].updateVisual()


    def __getitem__(self, coordinate):
        x, y = coordinate
        return self.board[x][y]
            
    
    #
    def selectSquare(self, square):
        moveSet = []
        # Point calls Piece to check valid Move
        if square.point.piece != None:
            if self.selectedSquare != None:
                if self.turn.side == square.point.piece.side:
                    self.selectedSquare = square
                    self.resetHint()
                    moveSet = self.selectedSquare.point.piece.generateMoveSet(side=self.selectedSquare.point.piece.side, board=self, originX=square.point.x, originY=square.point.y)
                    self.generateHint(moveSet)
                    print("try to attack your bros huh, select him instead")

                else:
                    moveSet = self.selectedSquare.point.piece.generateMoveSet(side=self.selectedSquare.point.piece.side, board=self, 
                    originX=self.selectedSquare.point.x, originY=self.selectedSquare.point.y)

                    if self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                        self.makeAttack(square)
                        self.selectedSquare = None
                        self.resetHint()
                        print("attack")

                    if not self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                        self.selectedSquare = None
                        self.resetHint()
                        print("Bruh this move is not even in moveSet, try to attack air?")

            else:
                if self.turn.side == square.point.piece.side:
                    self.selectedSquare = square
                    moveSet = self.selectedSquare.point.piece.generateMoveSet(side=self.selectedSquare.point.piece.side, board=self, originX=square.point.x, originY=square.point.y)
                    self.generateHint(moveSet)
                    print("nothing get selected yet so im gonna pick this")
                else:
                    print("try to select enemy's piece huh, pls dont do that ")
                    
        else:
            if self.selectedSquare != None:
                moveSet = self.selectedSquare.point.piece.generateMoveSet(side=self.selectedSquare.point.piece.side, board=self, originX=self.selectedSquare.point.x, originY=self.selectedSquare.point.y)
                if self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                    self.doMove(square)
                    self.selectedSquare = None
                    self.resetHint()
                    print("move")
                else:
                    self.selectedSquare = None
                    self.resetHint()
                    print("Bruh this move is not even in moveSet, try to step in the air?")
            else:
                print("really nothing to do here")


    def generateHint(self, moveSet):
        for row in self.board:  # Iterate over each row
            for square in row:  # Iterate over each square in the row
                for move in moveSet:
                    x, y = move
                    if x == square.point.x and y == square.point.y:
                        square.hintDot.showHint()
                        break


    def resetHint(self):
        for row in self.board:  # Iterate over each row
            for square in row:  # Iterate over each square in the row
                square.hintDot.hideHint()


    def isInMoveSet(self, moveSet, selectedX, selectedY):
        for move in moveSet:
            x, y = move
            if x == selectedX and y == selectedY:
                print(f"Already in moveSet: {selectedX}, {selectedY}")
                return True
            
        return False
    
    def makeAttack(self, square):
        print("Attack yet?")

        if self.turn.side == self.player1.side and self.selectedSquare.point.piece.side ==  self.player1.side:
            self.player1.addCapturedPiece(square.point.piece)

        if self.turn.side == self.player2.side and self.selectedSquare.point.piece.side ==  self.player2.side:
            self.player2.addCapturedPiece(square.point.piece)

        self.board[square.point.x][square.point.y].point.piece = self.selectedSquare.point.piece
        self.board[self.selectedSquare.point.x][self.selectedSquare.point.y].point.piece = None

        self.renderVisual()


    def doMove(self, square):
        self.board[square.point.x][square.point.y].point.piece = self.selectedSquare.point.piece
        self.board[self.selectedSquare.point.x][self.selectedSquare.point.y].point.piece = None

        self.renderVisual()


    #for test only
    def printBoard(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j].point.piece)
    

        

    

    