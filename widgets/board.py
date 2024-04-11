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
        self.selectedPiece = None

        self.initializeComponents()
        self.initializeVisual()


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

    def initializeVisual(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                self.board[i][j].updateVisual()


    def __getitem__(self, coordinate):
        x, y = coordinate
        return self.board[x][y]


    def movePiece(self, point):
        if point.piece != None:
            pass
            
    
    #
    def selectSquare(self, square):
        moveSet = []
        # Point calls Piece to check valid Move
        if square.point.piece != None:
            if self.selectedPiece != None:
                if self.selectedPiece == square.point.piece:
                    # deselecting piece
                    self.selectedPiece = None
                    self.resetHint()
                else:
                    if square.point.piece.side 
                    moveSet = square.point.piece.generateMoveSet(side=square.point.piece.side, board=self, originX=square.point.x, originY=square.point.y)

                    if self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                        

            else:
                self.selectedPiece = square.point.piece
                # check if user of that turn pick their piece
                if self.selectedPiece.side == self.turn.side:
                    moveSet = square.point.piece.generateMoveSet(side=square.point.piece.side, board=self, originX=square.point.x, originY=square.point.y)
                    self.generateHint(moveSet)
                
                else
                    

        else:
            if self.selectedPiece != None:
                # making a move -> check valid move
                self.movePiece(square.point)
            else:
                # random click on board makes by player, do nothing
                pass


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


    def isInMoveSet(moveSet, selectedX, selectedY):
        for move in moveSet:
            x, y = move
            if x == selectedX and y == selectedY:
                return True
            
        return False


    

        

    

    