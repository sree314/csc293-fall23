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
x.load("/home/sree/voron/c270-mount/CAD/C270_assembly.step")
a = x.to_cadquery()
print("done")

for o, oo in a.traverse():
    print(o)
    print(oo)
    exporters.export(oo.toCompound(), f"/tmp/{o}.stl")
