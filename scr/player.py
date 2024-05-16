class Player:
  
  def __init__(self, side, username):
    self.__side = side
    self.__username = username
    self.__ready = False
    self.__capturedList = []

  @property
  def side(self):
    return self.__side
  
  @side.setter
  def side(self, side):
    self.__side = side
  
  @property
  def username(self):
    return self.__username

  @property
  def capturedList(self):
    return self.__capturedList
  
  @capturedList.setter
  def capturedList(self, capturedList):
    self.__capturedList = capturedList

  @username.setter
  def username(self, username):
    self.__username = username

  def addCapturedPiece(self, piece):
    self.__capturedList.append(piece)

  @property
  def ready(self):
    return self.__ready
  
  @ready.setter
  def ready(self, ready):
    self.__ready = ready
  
  