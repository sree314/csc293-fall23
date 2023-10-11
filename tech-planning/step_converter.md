Step to STL design
Need: 
- Output path
- Output names 
- Part information 
- Orientation
- Cura → manual rotation, face plant
- Structural, cosmetic (infill)
- Project name
- Selection of printable parts
- Automatic? 

Focus wheel:
- Rotate (angle x, y, z)
Slicing
- Layer width (STL generation)
- Nozzle width
- Infill
- Perimeters walls
- Bottom layers 
- Human readable note
- Filament color 
- Material 
- Count to print 

Implementation:
Tool 
- init jsonfile stepfile 
Names 
Step
Part info file
- Version
- general
- sources: 
    Step file:
        Type: STEP
            Parts: [ 
            {
            Rotation
            Material
            Print params 
            tolerance/angular tolerance
            select_if: expression (handle choices)
            }
            ]

- User choices file (optional)
    - Var = value 



step converter
- step files = 3D parts
- json files = sources, step file, part info
- text files

Classes:
- Source
    - stepfile
    - partInfo
    - to_dict()
    - from_dict()
- PartInfo
    - id/name
    - orientation 
    - to_dict()
    - from_dict()