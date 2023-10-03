import cadquery as cq
from cadquery import exporters
from jupyter_cadquery import stepreader

# Task 1: Export STL files
# Whole file
step = cq.importers.importStep("./C270_assembly.step")
exporters.export(step, "./C270_blumenthal.stl")

# Task 2: Export SVG files
# Whole file
exporters.export(step, "./C270_blumenthal.svg")

def traverse(assembly):
    if isinstance(assembly, cq.Assembly):
        for o, assm in assembly.traverse():
            print(assm)
            traverse(assm)
    else:
        print(assembly)

print("starting")
x = stepreader.StepReader()
x.load("./C270_assembly.step")
a = x.to_cadquery()
print("done")

# ALL PARTS 
for o, oo in a.traverse():
    print(o)
    print(oo)
    exporters.export(oo.toCompound(), f"./stl_parts/{o}.stl") # STL by part
    exporters.export(oo.toCompound(), f"./svg_parts/{o}.svg") # SVG by part

# # Rotate mount
for o, oo in a.traverse():
    if o == 'C270_mount_0':
        rotated = oo.toCompound().rotate((0, 0, 0), (1, 0, 0), 180)
        exporters.export(rotated, f"./stl_parts/{o}_Rotated.stl")
        exporters.export(rotated, f"./svg_parts/{o}_Rotated.svg")
        break

# Rotate Logitech
for o, oo in a.traverse():
    if o == 'Logitech_c270_Assembly_v2_0' or o == 'Logitech_C270_0':
        rotated = oo.toCompound().rotate((0, 60, 40), (1, 0, 0), -45)
        exporters.export(rotated, f"./stl_parts/{o}_Rotated.stl")
        exporters.export(rotated, f"./svg_parts/{o}_Rotated.svg")
        break

# Task 3: multiple parts in one SVG
parts = cq.Assembly(None)
for o, oo in a.traverse():
    if o == 'Focus_wheel_0':
        for s in oo.shapes:
            parts = parts.add(s, loc=cq.Location((0, -30, 10)))
    if o == 'C270_mount_0':
        for s in oo.shapes:
            parts = parts.add(s, loc=cq.Location((-40, 0, 0)))
exporters.export(parts.toCompound(), f"./svg_parts/{o}_multiple_parts.svg")