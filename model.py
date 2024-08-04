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
            x = agents.Citizen(LethalModel.next_id(self),self)  
            # Adding agent to the schedule
            self.schedule.add(x)
            self.citizens_list.append(x)

            # Addding Militans to a random cell
            coord_x = self.random.randrange(self.grid.width)  
            coord_y = self.random.randrange(self.grid.height)
            self.grid.place_agent(x,(coord_x,coord_y))

        
        # Creating Militants
        for j in range(self.num_of_militants):
            y = agents.Militant(LethalModel.next_id(self),self)

            # Adding militants to te schedule 
            self.schedule.add(y)
            self.militants_list.append(y)

            # Addding Militans to a random cell
            coord_x = self.random.randrange(self.grid.width)  
            coord_y = self.random.randrange(self.grid.height)
            self.grid.place_agent(y,(coord_x,coord_y))

        
        # Creating Military Squad
        for k in range(self.num_of_msquad):
            z = agents.MSquad(LethalModel.next_id(self),self)

            #Adding Military Squad to the schedule
            self.schedule.add(z)
            self.military_squads_list.append(z)

            # Addding Militans to a random cell
            coord_x = self.random.randrange(self.grid.width)  
            coord_y = self.random.randrange(self.grid.height)
            self.grid.place_agent(z,(coord_x,coord_y))

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
    
    def get_militatnts_list(self):
        return self.militants_list
    
    def get_msquad_list(self):
        return self.military_squads_list
        