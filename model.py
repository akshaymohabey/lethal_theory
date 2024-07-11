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

    def __init__(self, citizens, militants, military_squad):
        super().__init__()
        self.num_of_citizens = citizens
        self.citizens_list = []
        self.militants_list = []
        self.military_squads_list = []

        # Creating Military Squad
        for k in range(military_squad):
            z = agents.MilitarySquad(k,self)
            self.military_squads_list.append(z)

        # Creating Citizens
        for i in range(citizens):
            x = agents.Citizen(i,self)
            self.citizens_list.append(x)
        
        # Creating Militants
        for j in range(militants):
            y = agents.Militant(j,self)
            self.militants_list.append(y)

    # Setter and getter functions
    def get_citizens_list(self):
        return self.citizens_list
        


