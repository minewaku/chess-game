from broad import Broad
from point import Point

def initialize(self):
        realX = 9
        realY = 10
        for i, row in enumerate(self.broad):
            for j, col in enumerate(row):
                self.broad[i][j] = Point(realX, realY)
                realX = realX - 1

            realY = realY - 1

        for i, row in enumerate(self.broad):
            for j, col in enumerate(row):
                print("(" + self.broad[i][j].x + ", " + self.broad[i][j].y + ")", end = ' ')
            print()

item = Broad()
item.initialize()