
# Class Define
class Bike():
  def __init__(self, tires, color, speed):
    self.tires = tires
    self.color = color
    self.num_speeds = speed

# Print Moving Forword
  def MoveForward(self):
    print('Moving Forward')

#    Print STOP
  def Brake(self):
    print('STOP')

  # Print Turning Right
  def TurnRight(self):
    print('Turning Right')

# Print Turning Left
  def TurnLeft(self):
    print('Turning Left')

# main
def main():
  MyRedBike = Bike('fat tires','red',7)
  MyRedBike.MoveForward()
  MyRedBike.TurnRight()
  MyRedBike.TurnLeft()
  MyRedBike.Brake()
  print(MyRedBike.color)
  print(MyRedBike.tires)
  print(MyRedBike.num_speeds)

main()
