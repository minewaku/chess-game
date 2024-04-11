class Point():

    def __init__(self, x: int, y: int, piece = None):
        self.__x = x
        self.__y = y
        self.__piece = piece

    # getter / setter of x 
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x: int):
        self.__x = x


    # getter / setter of y 
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y: int):
        self.__y = y


    # getter / setter of piece
    @property
    def piece(self):
        return self.__piece
    
    @piece.setter
    def piece(self, piece):
        self.__piece = piece