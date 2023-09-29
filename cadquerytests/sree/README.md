# README

This requires an install of cadquery

It also requires an install of `jupyter_cadquery`, which provides a
StepReader class that can be used to read Step files into CadQuery
assemblies. It might be possible to just use this file instead of the
whole jupyter_cadquery package.

This script can produce both STL and SVG files by changing the
extension in the `export` command.

Still todo:
  - Limit export to specific objects
  - Orientation, and other parameters.

