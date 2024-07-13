"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Model File
"""
# Importing Dependencies
import mesa
import parameters as p
import networkx as nx
import agents
import copy
import random

class LethalModel(mesa.Model):

    def __init__(self, citizens,militants,military_squad):
        super().__init__()
        self.num_of_citizens = citizens
        self.num_of_militants = militants
        self.num_of_msquad = military_squad

        self.citizens_list = []
        self.militants_list = []
        self.military_squads_list = []

        # Add grid
        self.grid = mesa.space.MultiGrid(p.grid_x,p.grid_y,False)

        # Create scheduler and assign it to Model
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        # Creating Citizens
        for i in range(self.num_of_citizens):
            x = agents.Citizen(i,self)  

            # Print Agent Type
            print(type(x))
            self.schedule.add(x)
            self.citizens_list.append(x)

            # # Addding Citizens/Family to a random cell
            # coord_x = self.random.randrange(self.grid.width)  
            # coord_y = self.random.randrange(self.grid.height)
            # self.grid.place_agent(x,(coord_x,coord_y))

        
        # Creating Militants
        for j in range(self.num_of_militants):
            y = agents.Militant(j,self)
            # Print Agent Type
            print(type(y))
            self.schedule.add(y)
            self.militants_list.append(y)

            # # Addding Militans to a random cell
            # coord_x = self.random.randrange(self.grid.width)  
            # coord_y = self.random.randrange(self.grid.height)
            # self.grid.place_agent(x,(coord_x,coord_y))

        
        # Creating Military Squad
        for k in range(self.num_of_msquad):
            z = agents.MSquad(k,self)
            # Print Agent Type
            print(type(z))
            self.schedule.add(z)
            self.military_squads_list.append(z)

            self.datacollector = mesa.DataCollector(
            model_reporters={"Citizens": "num_of_agents"},
            agent_reporters={"Money": "money"},
            )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    # Setter and getter functions
    def get_citizens_list(self):
        return self.citizens_list
    
    def get_msquad_list(self):
        return self.military_squads_list
        