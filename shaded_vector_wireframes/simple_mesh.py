import cadquery as cq
from cadquery import exporters
import numpy as np
step = cq.importers.importStep("../cadquerytests/blumenthal/C270_assembly.step")
tolerance = [0.001, 0.031, 0.051, 0.071, 0.091, 0.1]
angularTolerance = [0.07, 0.08, 0.09, 0.1]
# smallest size that is still accurate
# get a sense of what the parameters do to the size 
# focus wheel - individual parts 
# layer height for printing affects the angular tolerance -- how do the print settings affect tolerance/angular tolerance settings?
for t in tolerance:
    for a in angularTolerance:
        # print(t, a)
        exporters.export(step, f"../../simple_mesh_output/C270_{t}_{a}.stl", tolerance=t, angularTolerance=a)