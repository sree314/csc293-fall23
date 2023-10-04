#Samantha Kriegsman - CSC293 - Assignment #3

import os
import cadquery as cq
from jupyter_cadquery import stepreader

sr = stepreader.StepReader()
fileName = "C270_assembly"
sr.load(fileName+".step")
stepFile = sr.to_cadquery()

# <-- Couldnt get this to work, exporting created errors -->
#if not os.path.exists("tmp"):
#    print(Creating tmp folder for new files)
#    os.makedirs("tmp")

# <-- Task 1: Export STEP as STL -->
# Each part in the STEP should be placed into its own STL

for name, part in stepFile.traverse():
    if len(part.children) == 0:
        print("Exporting: " + name + " to .stl")
        cq.exporters.export(part.toCompound(), name+".stl")

# <-- Task 2: Export STEP as SVG -->
# Export every part in the STEP to its own SVG file

useOpt = False;

for name, part in stepFile.traverse():
    if len(part.children) == 0:
        print("Exporting: " + name + " to .svg")
        if useOpt:
            cq.exporters.export(part.toCompound(), name+".svg", opt={
                "width": 500,
        	"height": 500,
        	"marginLeft": 100,
        	"marginTop": 100,
        	"showAxes": True,
        	"projectionDir": (0.5, 0.5, 0.5),
        	"strokeWidth": 0.05,
        	"strokeColor": (0, 0, 0),
        	"hiddenColor": (80, 80, 80),
        	"showHidden": True,
    		},
	    )
        else:
            cq.exporters.export(part.toCompound(), name+".svg")

# <-- Task 3: Export multiple parts from STEP to single SVG -->
# Export each part into a single svg
# Have options to reposition parts 

tmpAssembly = cq.Assembly()
startMargin = 15
gap = 50

for name, part in stepFile.traverse():
    if len(part.children) == 0:
        print("Adding: " + name + " to .svg")
        tmpAssembly.add(part)
cq.exporters.export(tmpAssembly.toCompound(), fileName+"_custom.svg",)

# <-- Task 4: Add arbitrary graphic support for SVG export -->
# Shading certain parts in the SVG
# Shading certain surfaces on specific part in SVG
# Add small SVG icons to exported file

# <-- Task 5: MAke a list of STEP files for future testing -->
# 1. 
# 2. 
# 3. 