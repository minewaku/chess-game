class Logger:
    firstPlayerHistory = {"player": None, "moveHistory": []}
    secondPlayerHistory = {"player": None, "moveHistory": []}

    def __init__(self, player1, player2):
        self.firstPlayerHistory['player'] = player1
        self.secondPlayerHistory['player'] = player2

    def addMove(self, player, move):
        if self.firstPlayerHistory['player'].side == player.side:
            self.firstPlayerHistory['moveHistory'].append(move)
        if self.secondPlayerHistory['player'].side == player.side:
            self.secondPlayerHistory['moveHistory'].append(move) 
    

