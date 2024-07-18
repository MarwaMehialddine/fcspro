# adding drivers database
drivers = [
    {'id': 'ID001', 'name': 'Max Verstappen', 'start_city': 'Akkar'},
    {'id': 'ID002', 'name': 'Charles Leclerc', 'start_city': 'Saida'},
    {'id': 'ID003', 'name': 'Lando Norris', 'start_city': 'Jbeil'},
    {'id': 'ID004', 'name': 'Lewis Hamilton', 'start_city': 'Beirut'},
    {'id': 'ID005', 'name': 'Sebastian Vettel', 'start_city': 'Tripoli'},
    {'id': 'ID006', 'name': 'Daniel Ricciardo', 'start_city': 'Sidon'},
    {'id': 'ID007', 'name': 'Valtteri Bottas', 'start_city': 'Tyre'},
    {'id': 'ID008', 'name': 'Carlos Sainz', 'start_city': 'Byblos'},
    {'id': 'ID009', 'name': 'Pierre Gasly', 'start_city': 'Zahle'},
    {'id': 'ID010', 'name': 'Esteban Ocon', 'start_city': 'Baalbek'},
    {'id': 'ID011', 'name': 'Fernando Alonso', 'start_city': 'Keserwan'},
    {'id': 'ID012', 'name': 'Kimi Raikkonen', 'start_city': 'Jounieh'}
]

# adding cities database
cities = {
  'beirut': ['baabda', 'hazmieh', 'achrafieh'],
  'tripoli': ['el-minieh', 'zgharta', 'batroun'],
  'sidon': ['tyre', 'jezzine', 'nabatieh'],
  'tyre': ['sidon', 'bint jbeil', 'marjayoun'],
  'byblos': ['batroun', 'keserwan', 'jounieh'],
  'zahle': ['baalbek', 'anjar', 'chtaura'],
  'baalbek': ['zahle', 'hermel', 'anjar'],
  'keserwan': ['byblos', 'jounieh', 'metn'],
  'jounieh': ['keserwan', 'byblos', 'dora'],
  'batroun': ['tripoli', 'byblos', 'keserwan'],
  'baabda': ['beirut', 'hazmieh', 'choueifat'],
  'hazmieh': ['beirut', 'baabda', 'choueifat'],
  'achrafieh': ['beirut', 'hazmieh', 'sin el fil'],
  'choueifat': ['baabda', 'hazmieh', 'dahieh'],
  'dahieh': ['choueifat', 'hazmieh', 'beirut'],
  'jezzine': ['sidon', 'nabatieh', 'beirut'],
  'nabatieh': ['jezzine', 'tyre', 'marjayoun'],
  'bint jbeil': ['tyre', 'marjayoun', 'nabatieh'],
  'marjayoun': ['nabatieh', 'bint jbeil', 'tyre'],
  'hermel': ['baalbek', 'anjar', 'zahle'],
  'anjar': ['zahle', 'baalbek', 'hermel'],
  'cthaura': ['zahle', 'baalbek', 'anjar'],
  'metn': ['keserwan', 'beirut', 'baabda'],
  'dora': ['jounieh', 'metn', 'achrafieh'],
}

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

# generating id for the drivers when added by user
def generateId():
  max_id = max(int(driver['id'][2:]) for driver in drivers)
  new_id = max_id + 1
  return f'ID{new_id:03d}'

# looking if cities entered by the user are in the database
def city_exist(city):
  return cities.get(city.lower(), None)

# adding drivers to the database from the user
def addDriver():
  driver_name = input("Enter the drivers name: ")
  start_city = input("Enter the driver's start city: ")
  start_city_exist = city_exist(start_city)
  if start_city_exist is None:
     enter_city = input("The city you entered is not in the database. Do you want to add it? Answer with yes or no: ")
     if enter_city == 'yes':
       cities[start_city] = []
       print(cities)
     else:
       print("We cannot add the driver if the start city is not in the database. Driver not added.")
  driver_id = str(generateId())
  driver = {'id':driver_id, 'name':driver_name, 'start_city':start_city}
  drivers.append(driver)
  print('Drive with id', driver_id,', name', driver_name, 'and start city', 
  start_city, 'is added to the drivers database')
  for drive in drivers:
    print(drive['id'],drive['name'],drive['start_city'])

# introducing the cities menu
def citiesMenu():
  startcity = input("Enter:\n\n1. Show cities\n2. Print neighboring cities\n3. Print drivers delivering to city\n")
  if startcity == '1':
    showCities()
  elif startcity == '2':
    showNeighCities()
  elif startcity == '3':
    showDriversDelToCity()
  else:
    print("Invalid Input")
    startcity = input("Enter:\n\n1. Show cities\n2. Print neighboring cities\n3. Print drivers delivering to city\n")

# show cities in the database
def showCities():
  for city in cities.keys():
    print(city.capitalize())

# showing the neighboring cities
def showNeighCities():
  neighOfCity = input("Enter the city you want to see the neighboring cities of: ")
  neigh_of_city_exist = city_exist(neighOfCity)
  if neigh_of_city_exist is None:
    print(neighOfCity, 'is not in the database')
  else:
    neighboring_cities = cities[neighOfCity]
    print('Neighboring cities to', neighOfCity, 'are', '-'.join(neighboring_cities))
  
# check the drivers delivering to city
def showDriversDelToCity():
    # Show drivers who can deliver to a specified city
    city_input = input("Enter a city name to find drivers nwho deliver to: ")
    drivers_near_city = []
    for driver in drivers:
        if driver['start_city'].lower() == city_input:
            drivers_near_city.append(driver)
    if not drivers_near_city:
        if city_input in cities:
            neighboring_cities = cities[city_input]
            for driver in drivers:
                if driver['start_city'].lower() in neighboring_cities:
                    drivers_near_city.append(driver)
