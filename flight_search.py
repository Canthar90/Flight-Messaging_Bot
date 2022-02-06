import requests
import datetime

TEQUILA_SEARH = "tequila-api.kiwi.com"
API_KEY = "APIKeY"
HEADER = {"apikey": API_KEY}

# endpoint = f"http://tequila-api.kiwi.com/locations/query"
# query = {
#     "term": "New York",
#     "location_types": "city"
# }
# response = requests.get(url=endpoint, headers=HEADER, params=query)
# print(response.json()["locations"][0]["code"])

class FlightSearch:
    """Gets the codes of cities """
    # / locations / query
    def find_codes(self, countries):
        endpoint = f"http://tequila-api.kiwi.com/locations/query"
        codes = []
        for country in countries:
            query = {
                "term": country,
                "location_types": "city"
            }
            response = requests.get(url=endpoint, headers=HEADER, params=query)
            codes.append(response.json()["locations"][0]["code"])
        return codes
        # print(response.json()["locations"][0]["code"])
    #This class is responsible for talking to the Flight Search API.
    pass

    def find_flights(self, codes, names):
        """Looks for flights from tequila docs takes codes of cities, and names from current date to 6 months
        Puting it into dictionary with keyword as contry code and prices with data in dictionary """
        now = datetime.datetime.now()
        current_date = now.strftime(f"%d/%m/%Y")
        future_date = now + datetime.timedelta(days=182)
        future_date_formated = future_date.strftime(f"%d/%m/%Y")
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        end_data = {}
        data_to_work = []
        price = []
        local_arr = []
        local_dep = []
        deep_link = []
        counter = 0
        for name in names:
            parameters = {
                "fly_from": "WAW",
                "fly_to": codes[counter],
                "date_from": current_date,
                "date_to": future_date_formated,
                "curr": "GBP"
            }
            deals = requests.get(url=search_endpoint, headers=HEADER, params=parameters)
            # print(deals.json())
            # end_data[name] = deals.json()
            data_to_work = deals.json()["data"]
            # print(data_to_work[0])
            for pice in data_to_work:
                price.append(pice["price"])
                local_arr.append(pice["local_arrival"])
                local_dep.append(pice["local_departure"])
                deep_link.append(pice["deep_link"])
                # end_data[name]["price"].append(pice["price"])
                # end_data[name]["local_arrival"].append(pice["local_arrival"])
                # end_data[name]["local_departure"].append(pice["local_departure"])
            end_data[name] = {
                "price": price,
                "local_arrival": local_arr,
                "local_departure": local_dep,
                "deep_link": deep_link
            }
            counter += 1
        return end_data
        # form WAW  curr GBP