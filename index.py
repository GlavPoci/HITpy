from tkinter import *
from Modules.Math import *


Objects = read_object('Maps/Map1.txt')
for i in range(len(Objects)):
    print(i)
    print(Objects[i].get_position())
#print(Generate_resistor(100,100))
#Generate_file('Maps/MapGen.txt')
print(find_res_map(Objects))
#print(check_connect(Objects[3],Objects[4]))
