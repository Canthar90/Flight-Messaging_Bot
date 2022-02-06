import pandas
import openpyxl


# flight_data = pandas.read_excel("flights.xlsx")
# flights_to_loock = flight_data.to_dict()
# print(flights_to_loock)
# counter = 0
# # for keys in flights_to_loock["IATA Code"]:
#     flights_to_loock["IATA Code"][counter] = "kopytko"
#     counter += 1
#
# to_save = pandas.DataFrame.from_dict(flights_to_loock)
# to_save.to_excel( "flights.xlsx", index=False)
class DataManager:

    def __init__(self):
        """Load the data from excel file with coun try names"""
        self.flight_data = pandas.read_excel("flights.xlsx", sheet_name="Sheet1")
        self.users_data = pandas.read_excel("flights.xlsx", sheet_name="Sheet2")
        self.flights_to_loock = self.flight_data.to_dict()
        self.users_to_send = self.users_data.to_dict()
        print(self.users_to_send)


    def add_users(self):
        add_someone = input("Do you want to add new person to the Flight club? print 'y' or 'n': ")
        if add_someone.lower() == 'y':
            first_name = input("Pliss enter your First name: ")
            last_name = input("Pliss enter your Second name: ")
            user_email = input("Pliss enter your email adress: ")
            user_validation = input("Pliss validate your email adress: ")
            if user_validation == user_email:
                full_name = first_name + ' ' + last_name
                new_key = len(self.users_to_send) + 1
                self.users_to_send["Name"][new_key] = full_name
                self.users_to_send["Email"][new_key] = user_email
                print(self.users_to_send)
                self.users_to_save = pandas.DataFrame.from_dict(self.users_to_send)
                question = input("Would you like to add another user? type 'y' or 'n'").lower()
                if question == 'y':
                    self.add_users()
            else:
                print("Invalid email validation")
        self.users_to_save = pandas.DataFrame.from_dict(self.users_to_send)
        return self.users_to_send


    def citynames(self):
        """Return city names from excel"""
        names = []
        for keys in self.flights_to_loock["City"]:
            names.append(self.flights_to_loock["City"][keys])

        return names


    def iata_write(self, codes):
        """Writes the Codes of the countries """
        contry_codes = []
        counter = 0
        for keys in self.flights_to_loock["IATA Code"]:
            self.flights_to_loock["IATA Code"][keys] = codes[keys]
            contry_codes.append(codes[counter])
            counter += 1

        to_save = pandas.DataFrame.from_dict(self.flights_to_loock)
        with pandas.ExcelWriter("flights.xlsx") as writer:
            to_save.to_excel(writer, sheet_name="Sheet1", index=False)
            self.users_to_save.to_excel(writer, sheet_name="Sheet2", index=False)
        return contry_codes


    def cheap_finder(self, flights_data):
        cheap_flights = {}
        final_flights = {}
        names_count = 0
        for name in flights_data:
            counter = 0
            mid_list = []
            for price in flights_data[name]["price"]:
                if int(price) < int(self.flights_to_loock["Lowest Price"][names_count]):
                    mid_list.append({
                            counter:
                                    {
                                "price": flights_data[name]["price"][counter],
                                "local_arrival" : flights_data[name]["local_arrival"][counter],
                                "local_departure": flights_data[name]["local_departure"][counter],
                                "deep_link": flights_data[name]["deep_link"][counter]
                    }
                    })
                    cheap_flights = {
                        name:
                            mid_list
                            # [{
                            # counter:
                    #                 {
                    #             "price": flights_data[name]["price"][counter],
                    #             "local_arrival" : flights_data[name]["local_arrival"][counter],
                    #             "local_departure": flights_data[name]["local_departure"][counter]
                    # }
                    # }]
                    }
                    final_flights.update(cheap_flights)
                counter += 1
            names_count += 1
        return final_flights



