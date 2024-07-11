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
    def __init__(self,citizen_id,model):
        super().__init__(citizen_id,model)
        print("Hello, I am Citizen:",citizen_id)


# Militant Class 
class Militant(mesa.Agent):
    def __init__(self,militant_id,model):
        super().__init__(militant_id,model)
        print("Hello, I am Militant:",militant_id)

# Military Squad
class MSquad(mesa.Agent):
    def __init__(self,msquad_id,model):
        super().__init__(msquad_id,model)
        print('Hello! this is the Military Squad',msquad_id)