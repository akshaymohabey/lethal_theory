"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Sever/Vizualization File
""" 
# Importing Dependencies
import mesa
from agents import Citizen, Militant

def agent_portrayal(agent):
    return {
        "color" : "tab:blue",
        "size" : 50
    }

model_params = {
    "N": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "width": 10,
    "height": 10,
}


page = JupyterViz(
    boltzmann_wealth_model,
    model_params,
    measures=["Gini"],
    name="Money Model",
    agent_portrayal=agent_portrayal,
)


# Visualization File

