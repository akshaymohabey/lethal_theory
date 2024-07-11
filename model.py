"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Model File
"""

import mesa
import networkx
import agents

class Model(mesa.Model):

    def __init__(self, citizens,militants,military_squad):
        super().__init__()
        self.num_of_citizens = citizens
        self.num_of_militants = militants
        self.num_of_msquad = military_squad

        self.citizens_list = []
        self.militants_list = []
        self.military_squads_list = []

        # Create scheduler and assign it to Model
        self.schedule = mesa.time.RandomActivation(self)

        # Creating Citizens
        for i in range(self.num_of_citizens):
            x = agents.Citizen(i,self)  
            # Print Agent Type
            print(type(x))
            self.schedule.add(x)
            self.citizens_list.append(x)
        
        # Creating Militants
        for j in range(self.num_of_militants):
            y = agents.Militant(j,self)
            # Print Agent Type
            print(type(y))
            self.schedule.add(y)
            self.militants_list.append(y)
        
        # Creating Military Squad
        for k in range(self.num_of_msquad):
            z = agents.MSquad(k,self)
            # Print Agent Type
            print(type(z))
            self.schedule.add(z)
            self.military_squads_list.append(z)

        # Adding agents to the schedule 
        # Adding Citizens
        """
        for i in range(len(self.citizens_list)):
            self.schedule.add(self.schedule[i])
            print("Agent added to the schedule: ",self.citizens_list[i])
        """


    def step(self):
        self.schedule.step()

    # Setter and getter functions
    def get_citizens_list(self):
        return self.citizens_list
    
    def get_msquad_list(self):
        return self.military_squads_list
        