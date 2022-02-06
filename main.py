#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager




message = NotificationManager()
data = DataManager()
flights = FlightSearch()

users = data.add_users()
print(users)
citynames = data.citynames()
# print(citynames)
codes = flights.find_codes(citynames)
# print(codes)
data.iata_write(codes)
search_data = flights.find_flights(codes=codes, names=citynames)
# print(search_data["Berlin"])
ocasions = data.cheap_finder(search_data)
message.ocasion_messages(ocasions=ocasions, users=users)

# trial["Berlin"]
# "price" "local_arrival" "local_departure"