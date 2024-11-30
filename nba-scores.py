from requests import get
from pprint import PrettyPrinter 

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()
printer.pprint(data)

#Project tạm dừng vì data.nba.net's sever is down. 27/11