#!/usr/bin/env python3

import json
import argparse
from math import sqrt
from svg3d import *
import numpy
import pyrr
import matplotlib.pyplot as plt

def octahedron():
    """Construct an eight-sided polyhedron"""
    f =  sqrt(2.0) / 2.0
    verts = numpy.float32([ ( 0, -1,  0), (-f,  0,  f), ( f,  0,  f), ( f,  0, -f), (-f,  0, -f), ( 0,  1,  0) ])
    triangles = numpy.int32([ (0, 2, 1), (0, 3, 2), (0, 4, 3), (0, 1, 4), (5, 1, 2), (5, 2, 3), (5, 3, 4), (5, 4, 1) ])

    return verts[triangles]

def from_tjs(tjs):
    v = tjs['vertices']
    f = tjs['faces']
    print(len(v))
    print(len(f))

    nf = int(tjs['metadata']['faces'])

    verts = numpy.float32([v[i:i+3] for i in range(0, len(v), 3)])
    triangles = numpy.int32([f[i:i+3] for i in range(1, len(f), 4)])

    return verts[triangles]

def shader(face_index, winding):
    if winding < 0: return None
    return dict(
        fill='white', fill_opacity='0.75',
        stroke='black', stroke_linejoin='round', stroke_width='0.005')

def svg3d_render(verts):
    bb1 = numpy.min(numpy.min(verts, 0), 0)  # bottom left
    bb2 = numpy.max(numpy.max(verts, 0), 0)  # top  right

    print(bb1, bb2)

    left = bb1[0]- 1
    right = bb2[0] + 1
    top = bb2[1] + 1
    bottom = bb1[1] - 1
    near =  bb2[2]+5
    far = bb1[2]-10

    projection_matrix = pyrr.matrix44.create_orthogonal_projection(left,right,top,bottom,near,far)
    view_matrix = pyrr.matrix44.create_look_at(eye=[(left+right)/2, 1, -5],
                                               target=[0, 0, 0], up=[-1, 1, -1])

    camera = Camera(view_matrix, projection_matrix)

    style = dict(
        fill='blue', fill_opacity='1.0',
        stroke='blue', stroke_linejoin='round', stroke_width='0.0005')

    mesh = Mesh(verts, style=style)
    view = View(camera, Scene([mesh]))
    Engine([view]).render('test.svg')

def mp_render(verts):
    vertf = verts.flatten()
    x = [vertf[i] for i in range(0, len(vertf), 3)]
    y = [vertf[i] for i in range(1, len(vertf), 3)]
    z = [vertf[i] for i in range(2, len(vertf), 3)]

    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(x, y, z)
    plt.show()

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Render a ThreeJS file using svg3d")
    p.add_argument("tjsfile", help="ThreeJS file")

    args = p.parse_args()

    with open(args.tjsfile, "r") as f:
        tjs = json.load(f)

    for x in tjs:
        try:
            print(x, len(tjs[x]))
        except:
            pass

    verts = from_tjs(tjs)
    #mp_render(verts)
    svg3d_render(verts)
