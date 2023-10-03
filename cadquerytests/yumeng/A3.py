#!/usr/bin/python3

import cadquery as cq
from cadquery import exporters
from jupyter_cadquery import stepreader


def traverse(assembly):
    if isinstance(assembly, cq.Assembly):
        for o, assm in assembly.traverse():
            print(assm)
            traverse(assm)
    else:
        print(assembly)

print("starting")
#result = cq.importers.importStep("/home/sree/voron/c270-mount/CAD/C270_assembly.step")
x = stepreader.StepReader()
x.load("C270_assembly.step")
a = x.to_cadquery()
print("done")


# Task 1 & 2:
for o, oo in a.traverse():
    print(o)
    print(oo)
    if o == 'C270_mount_0':
        rotated = oo.toCompound().rotate((0, 0, 0), (1, 0, 0), 180)
        exporters.export(rotated, f"/Users/yumenghe/Desktop/CSC293/A3/{o}_Rotated.stl")
        exporters.export(rotated, f"/Users/yumenghe/Desktop/CSC293/A3/{o}_Rotated.svg")
        break
    elif o == 'Focus_wheel_0':
        exporters.export(oo.toCompound(), f"/Users/yumenghe/Desktop/CSC293/A3/{o}.stl")

    exporters.export(oo.toCompound(), f"/Users/yumenghe/Desktop/CSC293/A3/{o}.svg")


# Task 3:
parts = cq.Assembly(None)
for o, oo in a.traverse():
    # print(o)
    if o == 'Focus_wheel_0':
        for s in oo.shapes:
            parts = parts.add(s, loc=cq.Location((0, -10, 10)))
    if o == 'SOLID_0':
        for s in oo.shapes:
            parts = parts.add(s, loc=cq.Location((-40, 0, 0)))
exporters.export(parts.toCompound(), f"/Users/yumenghe/Desktop/CSC293/A3/multiple_parts.svg")

