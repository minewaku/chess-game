from piece import Piece
from piece import Pawn
from side import Side
from point import Point


class Board:
    # location for Points and defined size of board
    board = [[None] * 8 for Point in range(8)]
    player1 = None
    player2 = None
    selectedPiece = None
    
    #list of moves
    logger = []
    turn = player1

    def __init__(self):
        self.initialize()

    def initialize(self):
        realY = 1
        for i, row in enumerate(self.board):
            realX = 1
            for j, col in enumerate(row):
                self.board[i][j] = Point(realX, realY)
                realX = realX + 1

            realY = realY + 1

        self.board[1][0].piece = Pawn(Side.WHITE) 
        self.board[1][1].piece = Pawn(Side.WHITE) 
        self.board[1][2].piece = Pawn(Side.WHITE) 
        self.board[1][3].piece = Pawn(Side.WHITE) 
        self.board[1][4].piece = Pawn(Side.WHITE) 
        self.board[1][5].piece = Pawn(Side.WHITE) 
        self.board[1][6].piece = Pawn(Side.WHITE) 
        self.board[1][7].piece = Pawn(Side.WHITE) 

        self.board[6][0].piece = Pawn(Side.BLACK) 
        self.board[6][1].piece = Pawn(Side.BLACK) 
        self.board[6][2].piece = Pawn(Side.BLACK) 
        self.board[6][3].piece = Pawn(Side.BLACK) 
        self.board[6][4].piece = Pawn(Side.BLACK) 
        self.board[6][5].piece = Pawn(Side.BLACK) 
        self.board[6][6].piece = Pawn(Side.BLACK) 
        self.board[6][7].piece = Pawn(Side.BLACK) 


    #only for test
    def printboardByLocation(self):
        for row in reversed(self.board):
            for col in row:
                print("(" + str(col.x) + ", " + str(col.y) + ")", end = ' ')
            print()

    #only for test
    def printboardByPiece(self):
        for row in reversed(self.board):
            for col in row:
                if col.piece != None:
                    print(str(type(col.piece).__name__) + '.' + str(col.piece.side), end = ' ')
                else:
                     print("-", end = ' ')
            print()

    def movePiece(self, point):
        if point.piece != None:
            pass
            
            
    def selectPoint(self, point):
        # Point calls Piece to check valid Move
        if point.piece != None:
            if self.selectedPiece != None:
                if self.selectedPiece == point.piece:
                    # deselecting piece
                    self.selectedPiece = None
                else:
                    # making an attack, override piece 
                    self.movePiece(point)

            else:
                # picking a piece -> calling some methods to hint valid moves
                self.selectedPiece = point.piece
        else:
            if self.selectedPiece != None:
                # making a move -> check valid move
                self.movePiece(point)
            else:
                # random click on board makes by player, do nothing
                pass
        

    

item = Board()
item.printboardByLocation()
item.printboardByPiece()