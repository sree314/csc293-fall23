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


parts = cq.Assembly(None)
for o, oo in a.traverse():
    print(o)
    if o == 'Focus_wheel_0':
        for s in oo.shapes:
            parts = parts.add(s, loc=cq.Location((5, 0, 0)))
        parts = parts.toCompound()
        print(parts.Center())
        exporters.export(parts, f"/Users/yumenghe/Desktop/CSC293/A3/{o}.json", exportType=exporters.ExportTypes.TJS)
        break
