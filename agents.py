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
import random
import networkx as nx
import parameters as p

# Citizen Class
class Citizen(mesa.Agent):
    def __init__(self,citizen_id,model):
        super().__init__(citizen_id,model)
        # print("Hello, I am Citizen:",citizen_id)
        self.identity = '0'
    
    def step(self):
        pass

# Militant Class 
class Militant(mesa.Agent):
    def __init__(self,militant_id,model):
        super().__init__(militant_id,model)
        # print("Hello, I am Militant:",militant_id)
        self.identity = '1'
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def step(self):
        self.move()


# Military Squad
class MSquad(mesa.Agent):
    def __init__(self,msquad_id,model):
        super().__init__(msquad_id,model)
        # print('Hello! this is the Military Squad',msquad_id)
        self.identity = '2'

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def step(self):
        self.move()


    

