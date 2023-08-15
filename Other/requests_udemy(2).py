import json
import requests

# class Tounament(json.JSONEncoder):

#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     @classmethod
#     def from_json(cls, json_data: dict):
#         return cls(**json_data)
    
# class ChessPlayer:

#     def __init__(self, tournaments):
#         self.tournaments = tournaments
    
#     @classmethod
#     def from_json(cls, json_data: dict):
#         tounaments = list(map(Tounament.from_json, json_data['tounaments']))
#         return cls(tounaments)

# t1 = Tounament("Aeroflot Open", 2010)
# t2 = Tounament("FIDE World Cup", 2018)
# t3 = Tounament("FIDE Grand Prix", 2016)

# p1 = ChessPlayer([t1,t2,t3])

# json_data = json.dumps(p1, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# response = requests.post('https://www.httpbin.org/post', json=json_data)
# json_response = response.json()

# print(json_response['data'])
# print(json_response['headers']['Content-Type'])





# from getpass import getpass
# auth_response = requests.get('https://api.github.com/user', auth=('timurxboy', getpass()))
# print(auth_response.json())




# from requests.exceptions import Timeout

# try:
#     response = requests.get('https://www.engineerspock.com', timeout=2)

# except Timeout:
#     print('The request timed out')

# print(response)






from requests.adapters import HTTPAdapter
from getpass import getpass
adapter = HTTPAdapter(max_retries=3)

with requests.Session() as session:
    session.mount('https://api.gituhb.com', adapter)
    session.auth = ('timurxboy', getpass())

    try:
        session.get('https://api.gituhb.com/users')
    except ConnectionError as err:
        print(f'Failed connection:{err}')
    else:
        print('OK')


