
class Column:
  def __init__(self, _id, _amountOfFloors, _amountOfElevators):
    self.ID = _id
    self.status = 'idle'
    self.elevatorsList = []
    self.callButtonsList = []
    self.elevatorInAction = []
    self.amountOfElevators = _amountOfElevators
    self.amountOfFloors = _amountOfFloors


############## FONCTION D'APELLE ################
  def requestElevator(self, requestedFloor, direction):

    score = 0
############### CRÉE ELEVATOR ################
    for i in range(-1, (self.amountOfElevators - 1)):
      i = i + 1
      self.elevatorsList.append(Elevator(i + 1, self.amountOfFloors, 10, 5))
############### INITIALISER LES ÉTAGES ################
    self.elevatorsList[0].idle = 2  
    self.elevatorsList[1].idle = 9
############### CREATION DU SCORE ################
    for i in range(-1, (len(self.elevatorsList) - 1)):
      i = i + 1

      self.elevatorsList[i].currentFloor = self.elevatorsList[i].idle

      if self.elevatorsList[i].currentFloor > requestedFloor:
        score = (self.elevatorsList[i].currentFloor + 10) - requestedFloor
      else:
        score = (requestedFloor + 10) - self.elevatorsList[i].currentFloor

      if direction == self.elevatorsList[i].direction:
        score = score + 2

      self.elevatorsList[i].score = score
   
############### REGLE ET SELECTION ################

      
      if self.elevatorsList[i].score < self.elevatorsList[0].score:
        selectedElevator = self.elevatorsList[i]
      else:
        selectedElevator = self.elevatorsList[0] 

    print(f'elevator : {selectedElevator}')
 
############### REGLE ET SELECTION ################

    if selectedElevator.currentFloor < requestedFloor:
      selectedElevator.status = 'moving'
      selectedElevator.direction = 'up'
      print(f"Elevator {selectedElevator.ID} is {selectedElevator.status} {selectedElevator.direction}")

      for selectedElevator.currentFloor in range(selectedElevator.currentFloor, requestedFloor):
        selectedElevator.currentFloor = selectedElevator.currentFloor + 1
        print(f"Floor : {selectedElevator.currentFloor}")

    else:
      selectedElevator.status = 'moving'
      selectedElevator.direction = 'down'
      print(f"Elevator {selectedElevator.ID} is {selectedElevator.status} {selectedElevator.direction}")
      distance = selectedElevator.currentFloor - requestedFloor
      for i in range(i - 1, distance):
              selectedElevator.currentFloor = selectedElevator.currentFloor - 1
              print(f"Floor : {selectedElevator.currentFloor}")

############### MOUVEMENT DES PORTED ################

    selectedElevator.direction = 'idle'
    selectedElevator.status = 'on idle'
    selectedElevator.door = 'open'

    print(f"Elevator {selectedElevator.ID} is {selectedElevator.status}")
    print(f"The door is {selectedElevator.door}")

    self.elevatorInAction = selectedElevator

class Elevator:
  def __init__(self, _id, _amountOfFloors, _currentFloor, _idle):
    self.ID = _id
    self.status = 'idle'
    self.direction = 'on idle'
    self.currentFloor = _currentFloor
    self.idle = 0
    self.door = None    #temporaire
    self.floorRequestButtonList = []
    self.floorRequestList = []
    self.score = 0

  def requestFloor(self, requestedFloor):
    print('dans la function requested floor ')  
    print(requestedFloor)
    print(self.currentFloor)

class Door:
  def __init__(self, _id):
    self.ID = _id
    self.status = 'closed'

class CallButton:
  def __init__(self, _id, _floor, _direction):
    self.ID = _id
    self.status = 'idle'
    self.floor = _floor
    self.direction = _direction

class FloorRequestButton:
  def __init__(self, _id, _floor):
    self.ID = _id
    self.status = 'idle'
    self.floor = _floor


#               scénario 1


column1 = Column(1, 10, 2)





column1.requestElevator(6, 'up')
column1.elevatorInAction.requestFloor(2)

