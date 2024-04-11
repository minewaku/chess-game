class Player:
  
  def __init__(self, side, username):
    self.__side = side
    self.__username = username
    self.__capturedList = []

  @property
  def side(self):
    return self.__side
  
  @property
  def username(self):
    return self.__username
  
  @username.setter
  def username(self, username):
    self.__username = username

  def addCapturedPiece(self, piece):
    self.__capturedList.append(piece)
  
