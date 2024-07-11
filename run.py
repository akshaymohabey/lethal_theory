"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Run File
"""
from model import Model
import parameters as p

main_instance = Model(p.No_of_Citizens,p.No_of_Militants,p.No_of_MilitarySquad)

for i in range(10):
    main_instance.step()

