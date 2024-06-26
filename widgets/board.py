import sys

sys.path.append('../')
from scr.piece import Piece
from scr.piece import Pawn
from scr.piece import Queen
from scr.piece import King
from scr.piece import Rook
from scr.piece import Horse
from scr.piece import Bishop


from scr.point import Point
from scr.side import Side
from scr.move import Move

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from .square import Square
from .promotionPopup import promotionPopup

class Board(GridLayout):

    # Handling all rules and mechanisms that necessary for Chess

    BOARD_SIZE = 8
    
    def __init__(self, player_panel_black, player_panel_white, square_size, player_1, player_2, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.square_size = square_size
    
        self.board = [[None] * Board.BOARD_SIZE for _ in range(Board.BOARD_SIZE)]
        self.player_panel_black = player_panel_black
        self.player_panel_white = player_panel_white
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = self.player_panel_white.player
        self.log = []

        self.player_panel_black.timeCounter.stop_counter()
        self.selectedSquare = None

        self.initializeComponents()
        self.renderVisual()
        self.updateMoveSetForAllPieces()


    def initializeComponents(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#fffbe8", size_hint=(None, None), size=(self.square_size, self.square_size))
                    else:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#e2aa23", size_hint=(None, None), size=(self.square_size, self.square_size))
                else:
                    if j % 2 == 0:  
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#e2aa23", size_hint=(None, None), size=(self.square_size, self.square_size))
                    else:
                        self.board[i][j] = Square(point=Point(i, j), board=self, background_color="#fffbe8", size_hint=(None, None), size=(self.square_size, self.square_size))

                self.add_widget(self.board[i][j])


        self.board[6][0].point.piece = Pawn(Side.WHITE) 
        self.board[6][1].point.piece = Pawn(Side.WHITE) 
        self.board[6][2].point.piece = Pawn(Side.WHITE) 
        self.board[6][3].point.piece = Pawn(Side.WHITE) 
        self.board[6][4].point.piece = Pawn(Side.WHITE) 
        self.board[6][5].point.piece = Pawn(Side.WHITE) 
        self.board[6][6].point.piece = Pawn(Side.WHITE) 
        self.board[6][7].point.piece = Pawn(Side.WHITE) 

        self.board[7][0].point.piece = Rook(Side.WHITE)
        self.board[7][1].point.piece = Horse(Side.WHITE)
        self.board[7][2].point.piece = Bishop(Side.WHITE)
        self.board[7][3].point.piece = Queen(Side.WHITE)
        self.board[7][4].point.piece = King(Side.WHITE)
        self.board[7][5].point.piece = Bishop(Side.WHITE)
        self.board[7][6].point.piece = Horse(Side.WHITE)
        self.board[7][7].point.piece = Rook(Side.WHITE)

        self.board[1][0].point.piece = Pawn(Side.BLACK) 
        self.board[1][1].point.piece = Pawn(Side.BLACK) 
        self.board[1][2].point.piece = Pawn(Side.BLACK) 
        self.board[1][3].point.piece = Pawn(Side.BLACK) 
        self.board[1][4].point.piece = Pawn(Side.BLACK) 
        self.board[1][5].point.piece = Pawn(Side.BLACK) 
        self.board[1][6].point.piece = Pawn(Side.BLACK) 
        self.board[1][7].point.piece = Pawn(Side.BLACK) 

        self.board[0][0].point.piece = Rook(Side.BLACK)
        self.board[0][1].point.piece = Horse(Side.BLACK)
        self.board[0][2].point.piece = Bishop(Side.BLACK)
        self.board[0][3].point.piece = Queen(Side.BLACK)
        self.board[0][4].point.piece = King(Side.BLACK)
        self.board[0][5].point.piece = Bishop(Side.BLACK)
        self.board[0][6].point.piece = Horse(Side.BLACK)
        self.board[0][7].point.piece = Rook(Side.BLACK)


    # render all pieces in the current board position
    def renderVisual(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                self.board[i][j].updateVisual()
    

    # decide what to do when picking a piece
    def selectSquare(self, square):
        # Point calls Piece to check valid Move
        if square.point.piece != None:
            if self.selectedSquare != None:
                if self.turn.side == square.point.piece.side:
                    self.resetHint(moveSet=self.selectedSquare.point.piece.moveSet)
                    self.selectedSquare = square
                    moveSet = self.selectedSquare.point.piece.moveSet
                    self.renderHint(moveSet=moveSet)
                    # print("switch selected piece from your side")

                else:
                    moveSet = self.selectedSquare.point.piece.moveSet

                    if self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                        self.doMove(square)
                        self.selectedSquare = None
                        self.resetHint(moveSet=moveSet)
                        self.updateMoveSetForAllPieces()
                        if self.turn.side == Side.BLACK:
                            if self.checkCheckingForAllPieces(side=Side.WHITE):
                                Popup(title='Alert', content=Label(text="You're in checkmate!"), size_hint=(None, None), size=(300, 200)).open()
                                self.undoMove()
                            elif self.checkCheckingForAllPieces(side=Side.BLACK):
                                print("Checkmate!")

                        elif self.turn.side == Side.WHITE:
                            if self.checkCheckingForAllPieces(side=Side.BLACK):
                                Popup(title='Alert', content=Label(text="You're in checkmate!"), size_hint=(None, None), size=(300, 200)).open()
                                self.undoMove()
                            elif self.checkCheckingForAllPieces(side=Side.WHITE):
                                print("Checkmate!")


                        self.checkForPromotion(square=square)
                        self.switchTurn()
                        # print("attack")

                    if not self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                        self.selectedSquare = None
                        self.resetHint(moveSet=moveSet)
                        # print("try to move to a move that is not in moveSet, unable to do that")

            else:
                if self.turn.side == square.point.piece.side:
                    self.selectedSquare = square
                    moveSet = self.selectedSquare.point.piece.moveSet
                    self.renderHint(moveSet=moveSet)
                    # print("nothing get selected, selected this piece")
                else:
                    # print("select enemy's piece, unable to do that")
                    pass
                    
        else:
            if self.selectedSquare != None:
                moveSet = self.selectedSquare.point.piece.generateMoveSet(board=self, originX=self.selectedSquare.point.x, originY=self.selectedSquare.point.y)
                if self.isInMoveSet(moveSet=moveSet, selectedX=square.point.x, selectedY=square.point.y):
                    self.doMove(square)
                    self.selectedSquare = None
                    self.resetHint(moveSet=moveSet)
                    self.updateMoveSetForAllPieces()
                    if self.turn.side == Side.BLACK:
                        if self.checkCheckingForAllPieces(side=Side.WHITE):
                            Popup(title='Alert', content=Label(text="You're in checkmate!"), size_hint=(None, None), size=(300, 200)).open()
                            self.undoMove()
                        elif self.checkCheckingForAllPieces(side=Side.BLACK):
                            print("Checkmate!")

                    elif self.turn.side == Side.WHITE:
                        if self.checkCheckingForAllPieces(side=Side.BLACK):
                            Popup(title='Alert', content=Label(text="You're in checkmate!"), size_hint=(None, None), size=(300, 200)).open()
                            self.undoMove()
                        elif self.checkCheckingForAllPieces(side=Side.WHITE):
                            print("Checkmate!")

                    self.checkForPromotion(square=square)
                    self.switchTurn()
                    # print("move")
                else:
                    self.selectedSquare = None
                    self.resetHint(moveSet=moveSet)
                    # print("try to make a attack that is not in moveSet, unable to do that")
            else:
                # print("really nothing to do here")
                pass


    # display all dotHints from moveSet
    def renderHint(self, moveSet):
        for move in moveSet:
            x, y = move
            self.board[x][y].hintDot.showHint()


    # reset all dotHints from moveSet
    def resetHint(self, moveSet):
        for move in moveSet:
            x, y = move
            self.board[x][y].hintDot.hideHint()


    # check if selected coordinate is in moveSet or not. This method helps us to know the selected coordinates is valid to make a move or not
    def isInMoveSet(self, moveSet, selectedX, selectedY):
        for move in moveSet:
            x, y = move
            if x == selectedX and y == selectedY:
                return True
            
        return False
    

    # make a move
    def doMove(self, square):
        self.selectedSquare.point.piece.moveCount = self.selectedSquare.point.piece.moveCount + 1

        if square.point.piece != None:
            if self.turn.side == self.player_2.side and self.selectedSquare.point.piece.side == self.player_2.side:
                self.player_2.addCapturedPiece(square.point.piece)

            if self.turn.side == self.player_1.side and self.selectedSquare.point.piece.side == self.player_1.side:
                self.player_1.addCapturedPiece(square.point.piece)

            self.log.append(Move(originX=self.selectedSquare.point.x, originY=self.selectedSquare.point.y, finalX=square.point.x, finalY=square.point.y, piece=self.selectedSquare.point.piece, capturedPiece=square.point.piece))

        else:
            self.log.append(Move(originX=self.selectedSquare.point.x, originY=self.selectedSquare.point.y, finalX=square.point.x, finalY=square.point.y, piece=self.selectedSquare.point.piece))

        self.board[square.point.x][square.point.y].point.piece = self.selectedSquare.point.piece
        self.board[self.selectedSquare.point.x][self.selectedSquare.point.y].point.piece = None
        self.checkForCastling(square=square)
        self.renderVisual()


    # undo a move, getting that move from log array of current match
    def undoMove(self):
        move = self.log[-1]
        self.updateMoveSetForAllPieces()
        self.selectedSquare = self.board[move.finalX][move.finalY]
        self.selectedSquare.point.piece.moveCount = self.selectedSquare.point.piece.moveCount - 1
        moveSet = self.selectedSquare.point.piece.moveSet
        self.doMove(square=self.board[move.originX][move.originY])
        self.selectedSquare = None
        self.resetHint(moveSet=moveSet)
        if move.capturedPiece != None:
            self.board[move.finalX][move.finalY].point.piece = move.capturedPiece
        self.updateMoveSetForAllPieces()
        self.log.pop()
        self.switchTurn()
        self.renderVisual()


    def checkForPromotion(self, square):
        if isinstance(square.point.piece, Pawn) and (square.point.x == 7 or square.point.x == 0) and square.point.piece != None:
            self.promotion(square=square)


    def promotion(self, square):
        self.parent.add_widget(promotionPopup(square=square, pos_hint={'center_x': 0.5, 'center_y': 0.5}))

    
    def checkForCastling(self, square):
        if isinstance(square.point.piece, King) and (square.point.y == 2 or square.point.y == 6) and square.point.piece.moveCount == 1:
            self.castling(square=square)


    def castling(self, square):
        if square.point.piece.side == Side.WHITE:
            if square.point.y == 2:
                self.selectedSquare = self.board[7][0]
                self.doMove(self.board[7][3]) 

            elif square.point.y == 6:
                self.selectedSquare = self.board[7][7]
                self.doMove(self.board[7][5])

            self.updateMoveSetForAllPieces()
            if self.checkCheckingForAllPieces(side=Side.BLACK):
                # need to undo move twice cause we need to undo move for both king and rook
                self.undoMove()
                self.undoMove()
                
        elif square.point.piece.side == Side.BLACK:
            if square.point.y == 2:
                self.selectedSquare = self.board[0][0]
                self.doMove(self.board[0][3]) 

            elif square.point.y == 6:
                self.selectedSquare = self.board[0][7]
                self.doMove(self.board[0][5])

            self.updateMoveSetForAllPieces()
            if self.checkCheckingForAllPieces(side=Side.WHITE):
                self.undoMove()
                self.undoMove()



    # switch turn
    def switchTurn(self):
        if self.turn.side == self.player_panel_white.player.side:
            self.turn = self.player_panel_black.player
            self.player_panel_white.timeCounter.stop_counter()
            self.player_panel_white.timeCounter.reset_counter()
            self.player_panel_white.update_captured_panel()
            self.player_panel_white.surrenderButton.disabled = True

            self.player_panel_black.timeCounter.start_counter()
            if self.checkCheckingForAllPieces(side=self.player_panel_white.player.side):
                self.player_panel_black.surrenderButton.disabled = False

        elif self.turn.side == self.player_panel_black.player.side:
            self.turn = self.player_panel_white.player
            self.player_panel_black.timeCounter.stop_counter()
            self.player_panel_black.timeCounter.reset_counter()
            self.player_panel_black.update_captured_panel()
            self.player_panel_black.surrenderButton.disabled = True
            
            self.player_panel_white.timeCounter.start_counter()
            if self.checkCheckingForAllPieces(side=self.player_panel_black.player.side):
                self.player_panel_white.surrenderButton.disabled = False

    
    # after a move, this method would be called to update all possible move of every pieces on the board and stored them into their moveSet. This helps us to know that the current board position has checkmate or not
    def updateMoveSetForAllPieces(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if self.board[i][j].point.piece != None:
                    self.board[i][j].point.piece.generateMoveSet(board=self, originX=self.board[i][j].point.x, originY=self.board[i][j].point.y)


    #check checkmate status based on which side you send into. If side=BLACK, check if black pieces are checkmate the white King. True if there is at least one checkmate move 
    def checkCheckingForAllPieces(self, side):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if self.board[i][j].point.piece != None and self.board[i][j].point.piece.side==side == side and self.board[i][j].point.piece.isCheckMate(self):
                    return True
                
        return False

    

        

    

    