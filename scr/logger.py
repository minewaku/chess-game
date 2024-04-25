import os

from scr.side import Side

from datetime import datetime
from itertools import zip_longest

class Logger:

    PATH_TO_STORAGE = os.path.join("data")

    def __init__(self, winner, player_1, player_2, log):
        self.__winner = winner
        self.__player_1 = player_1
        self.__player_2 = player_2
        self.__log = log


    def writeLog(self):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Create file name based on current time
        file_name = f"log_{current_time}.txt"
        # Combine file name with storage path
        file_path = os.path.join(self.PATH_TO_STORAGE, file_name)

        # Write content to the file
        with open(file_path, 'w') as file:
            file.write(f"Winner: {self.__winner.username}\n")
            if self.__player_1.side == Side.WHITE:
                file.write(f"{self.__player_1.username}    {self.__player_2.username}\n")
                file.write(f"{self.__player_1.side.name}     {self.__player_2.side.name}\n")
            else:
                file.write(f"{self.__player_2.username}    {self.__player_1.username}\n")
                file.write(f"{self.__player_2.side.name}     {self.__player_1.side.name}\n")

            for item in self.__log:
                file.write(f"{item.piece.side.name} {item.piece.__class__.__name__}: ({item.originX}, {item.originY}) to ({item.finalX}, {item.finalY})  captured: {item.capturedPiece}\n")

        

