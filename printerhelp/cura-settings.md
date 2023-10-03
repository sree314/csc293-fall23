# Cura Settings

In recent versions of Cura, add a Voron Trident 300 printer.

Change the Z volume to 290mm.

Change the Start G-code to:

```
PRINT_START EXTRUDER={material_print_temperature_layer_0} BED={material_bed_temperature_layer_0} CHAMBER={build_volume_temperature}
```

Change the End G-code to:

```
PRINT_END
```

The Printhead Settings don't really matter on this printer, but for reference:

  - X min: -35
  - Y min: -40.5
  - X max: 35
  - Y max: 73.5
  - Gantry height: 51
  - Number of Extruders: 1

This printer does support meshing only the print area. If you want to
do that, make sure you have followed the [instructions for installing
the post-processing plugin in
Cura](https://github.com/Turge08/print_area_bed_mesh). Your Start
G-code will then look like this:

```
PRINT_START EXTRUDER={material_print_temperature_layer_0} BED={material_bed_temperature_layer_0} CHAMBER={build_volume_temperature} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```
The printer has been tested with a print speed of 200mm/s, with first layer running around 50mm/s.

