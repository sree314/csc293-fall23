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

test = cq.Assembly()
for i, (o, oo) in enumerate(a.traverse()):
    print(o)
    print(oo)
    for oos in oo.shapes:
        print("**", oos)
    #exporters.export(oo.toCompound(), f"/tmp/{o}.stl")

    if i == 0 or i == 3:
        if i == 0: continue
        for j, oos in enumerate(oo.shapes):
            print(oos.Center())
            if i == 3:
                test.add(oos.scale(5), color=(1,0,0,0))
            else:
                test.add(oos)



exporters.export(test.toCompound(), f"/tmp/x.svg")
