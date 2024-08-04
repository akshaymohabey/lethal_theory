"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Sever/Vizualization File
""" 
# Importing Dependencies
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

#Import model
from model import LethalModel
import parameters as p

def agent_portrayal(agent):
    portrayal = {
      "Shape": "circle",
      "Filled": True}
    if agent.identity == '0':
      portrayal["r"] = 0.60
      portrayal["Color"] = "#a4c639" # Android Green
      portrayal["Layer"] = 0
    elif agent.identity == '1':
      portrayal["r"] = 0.50
      portrayal["Color"] = "#d3212d" # Amaranth Red
      portrayal["Layer"] = 1
    else:
      portrayal["r"] = 0.30
      portrayal["Color"] = "#e9d66b" # Arylide Yellow
      portrayal["Layer"] = 2
    return portrayal

grid = CanvasGrid(
  agent_portrayal,
  p.grid_x,
  p.grid_y,
  600,
  600)

# chart = ChartModule([{
#   'Label': 'Gini',
#   'Color': 'Black'}],
#   data_collector_name='datacollector')

server = ModularServer(
  LethalModel,
  [grid],
  "Money Model",
  {"citizens":p.No_of_Citizens, "militants":p.No_of_Militants, "military_squad":p.No_of_MilitarySquad}
  )
server.port = 8521 # Any non-80 port to appease replit
server.launch()