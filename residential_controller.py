class Column:
  def __init__(self, _id, _status, _amountOfFloors, _amountOfElevators):
    self.ID = _id
    self.status = _status
    self.elevatorsList = []
    self.callButtonsList = []

class Elevator:
  def __init__(self, _id, _status, _amountOfFloors, _currentFloor):
    self.ID = _id
    self.status = _status
    self.direction = None
    self.currentFloor = _currentFloor
    self.door = None    #temporaire
    self.floorRequestButtonList = []
    self.floorRequestList = []

class Door:
  def __init__(self, _id, _status):
    self.ID = _id
    self.status = _status

class CallButton:
  def __init__(self, _id, _status, _floor, _direction):
    self.ID = _id
    self.status = _status
    self.floor = _floor
    self.direction = _direction

class FloorRequestButton:
  def __init__(self, _id, _status, _floor):
    self.ID = _id
    self.status = _status
    self.floor = _floor

#               scénario 1


column1 = Column(1, 'idle', 10 , 2)


print(column1.__dict__)