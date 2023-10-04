#Samantha Kriegsman - CSC293 - Assignment #3

import os
import cadquery as cq
from jupyter_cadquery import stepreader

sr = stepreader.StepReader()
fileName = "C270_assembly"
sr.load(fileName+".step")
stepFile = sr.to_cadquery()

if not os.path.exists("tmp"):
    print("Setup: Creating tmp folder for new files")
    os.makedirs("tmp")

# Enable and disable parts as needed for testing
doTask1 = True
doTask2 = False
doTask3 = False
doTask4 = False

# <-- Task 1: Export STEP as STL -->
# Each part in the STEP should be placed into its own STL
if doTask1:
    print("Task 1: ")

    tol = 0.001
    angTol = 0.1
    doAscii = False

    for name, part in stepFile.traverse():
        if len(part.children) == 0:
            print("    Exporting: " + name + " to .stl")
            cq.exporters.export(part.toCompound(), name+".stl")
            #cq.exporters.export(part.toCompound(), "/tmp/"+name+".stl")
                # Creates folder throws no error but files cant be found in folder
            #part.exportStl("/tmp/"+name+".stl", tol, angTol, doAscii)
                # Could work but part variable needs to be Shape obj not Assembly obj

# <-- Task 2: Export STEP as SVG -->
# Export every part in the STEP to its own SVG file
if doTask2:
    print("Task 2: ")
    
    useOpt = False;
    for name, part in stepFile.traverse():
        if len(part.children) == 0:
            print("    Exporting: " + name + " to .svg")
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
    		},)
            else:
                cq.exporters.export(part.toCompound(), name+".svg")

# <-- Task 3: Export multiple parts from STEP to single SVG -->
# Export each part into a single svg
# Have options to reposition parts 
if doTask3:
    print("Task 3: ")

    tmpAssembly = cq.Assembly()
    gapX = 10
    gapY = 100

    i = 0
    for name, part in stepFile.traverse():
        if len(part.children) == 0:
            print("    Adding: " + name + " to .svg")
            tmpAssembly.add(part, loc=cq.Location(cq.Vector(gapX*i, 0, gapY*i)))
            i = i + 1
            cq.exporters.export(tmpAssembly.toCompound(), fileName+"_p3.svg",)

# <-- Task 4: Add arbitrary graphic support for SVG export -->
# Shading certain parts in the SVG
# Shading certain surfaces on specific part in SVG
# Add small SVG icons to exported file
if doTask4:
    print("Task 4: ")
    tmpAssembly = cq.Assembly()
    gapX = 10
    gapY = 100

    i = 0
    for name, part in stepFile.traverse():
        if len(part.children) == 0:
            print("    Adding: " + name + " to .svg")
            tmpAssembly.add(part, loc=cq.Location(cq.Vector(gapX*i, 0, gapY*i)), color=(0, 50*i, 0))
            i = i + 1
            cq.exporters.export(tmpAssembly.toCompound(), fileName+"_p4.svg",)

# <-- Task 5: MAke a list of STEP files for future testing -->
# 1. CoralFragPlugStand.STEP --> A part I made for my dads fish tank
# 2. 
# 3. 