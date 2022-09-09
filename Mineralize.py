#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.lines  as mlines
import numpy as np
import csv
import math
import os
from scipy.interpolate import interp1d

size = 10000000 #20000
bondLength = 14


cutoffs = [9.08,9.05,9.02]
cutoffs = [x/10 for x in cutoffs]

for i in cutoffs:
	with open('badcontact.tcl','w') as file:
		distance = i
		file.write("mol load gro 4-MT-Mineralized.gro\n")
       		file.write("set sel [atomselect top all]\n")
        	file.write("$sel set beta 0\n")
        	file.write("set bad [atomselect top {type HA ")
        	file.write(" and ( within ")
        	file.write("{}".format(distance))
        	file.write(" of type CL")
        	file.write(")}]\n")
        	file.write("$bad set beta 1\n")
        	file.write("set out [atomselect top {beta 0}]\n")
		file.write("$out writegro 4-MT-Mineralized-{}.gro\n".format(distance))
		file.write("mol delete top\n")
		file.write("exit\n")
	os.system("vmd -dispdev text -eofexit -e badcontact.tcl")


