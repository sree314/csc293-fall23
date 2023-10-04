from jupyter_cadquery import stepreader
import cadquery as cq
from svgutils import compose

# Reading step file with parts
step = stepreader.StepReader()
step.load('C270_assembly.step')
step_cq_assem = step.to_cadquery()

# iterating subassemblies
# add wanted parts to a new assembly while specifying color
assem = cq.Assembly()
for name, child in step_cq_assem.traverse():
    if name == 'Focus_wheel_0':
        assem.add(child, color=cq.Color('red')) # see comments below for SVG coloring
    if name == 'SOLID_0':
        assem.add(child, color=cq.Color('green'))

# export assembly to svg
# NOTE: apparently colored SVG is still an open issue 
# https://github.com/CadQuery/cadquery/issues/645
# TODO: compute the appropriate width and height
width = 400 
height = 400
parts_filename = 'parts'
cq.exporters.export(assem.toCompound(), 
                    parts_filename + '.svg', 
                    opt={'width': width, 'height': height})

# Add logo 
# not sure how to do this in cadquery, but 3rd party libraries come in handy
# Voron logo downloaded from 
# https://github.com/GadgetAngel/Cricut_Voron_Logos/blob/main/Voron_2.4_Logo/1_Color_Layer/Current_Design_Files/Voron2.4_1Color.svg
# Python logo from
# https://www.python.org/static/community_logos/python-logo-generic.svg
compose.Figure(
    width,
    height,
    compose.SVG(parts_filename + '.svg'),
    # compose.SVG('Voron2.4_1Color.svg').scale(0.2), # somehow could not read voron logo
    compose.SVG('python-logo-generic.svg').scale(0.2),
).save(parts_filename + '_with_logo.svg')
