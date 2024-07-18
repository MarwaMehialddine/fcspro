
# starting the system
def startProgram():
  print("Hello!")
  start = input("Please enter:\n\n1. To go to the drivers’ menu\n2. To go to the cities’ menu\n3. To exit the system\n")
  if start == '1':
    driversMenu()
  elif start == '2':
    citiesMenu()
  elif start == '3':
    print('You are out of the system. Thank you for visiting!')
  else:
    print("Invalid Input")
    start = input("Please enter:\n\n1. To go to the drivers’ menu\n2. To go to the cities’ menu\n3. To exit the system\n")

# to go to the drivers menu
def driversMenu():
  startdriver = input("Enter:\n\n1. To view all the drivers\n2. To add a driver\n3. To go back to the main menu\n")
  if startdriver == '1':
    viewDrivers()
  elif startdriver == '2':
    addDriver()
  elif startdriver =='3':
    startProgram()
  else:
    print("Invalid Input")
    startdriv = input("Enter:\n\n1. To view all the drivers\n2. To add a driver\n3. To go back to the main menu\n")


# to view the drivers
def viewDrivers():
  if len(drivers) == 0:
    print("No drivers")
  for driver in drivers:
    print(driver['id'],driver['name'],driver['start_city'])