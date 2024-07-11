"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Agents File
"""

# Importing dependencies
import mesa

# Citizen Class
class Citizen(mesa.Agent):
    def __init__(self,citizen_id, model):
        super().__init__(citizen_id, model)
        print("Hello, I am Citizen:",citizen_id)

    def step():
        pass

# Militant Class 
class Militant(mesa.Agent):
    def __init__(self, militant_id, model):
        super().__init__(militant_id,model)
        print("Hello, I am Militant:",militant_id)

    def step():
        pass

# Military Squad
class MilitarySquad(mesa.Agent):
    def __int__(self, military_id, model):
        super().__init__(military_id, model)
        print("Hello, We are Military Squad:", military_id)

    def step():
        pass