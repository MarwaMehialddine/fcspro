# List of drivers with their ID, name, and starting city
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

# Dictionary of cities with neighboring citiesncjiuowcheiuvbh
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
# fnerjigeirughiu