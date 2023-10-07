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

Choose the **Generic ABS** material profile if it has not already been selected.

## Profile Settings

Create a default print profile based off an existing profile. All
setting names are highlighted in **bold** below. If you do not see
these settings in newer versions of Cura, click **Custom Settings** to
reveal them. Once you've made these changes, you can save the profile.

### Material Flow

Change the **Flow** to 92%. You can leave the Initial layer flow to 100%.

You may want to read up on [Ellis' Print Tuning Guide for Extrusion
Multiplier](https://ellis3dp.com/Print-Tuning-Guide/articles/extrusion_multiplier.html)
and conduct the test.


### Material

The filaments we use (MG Chemicals, KVP) print fine at **Printing Temperature** of 230C.

Set the **Build plate temperature** to 105C.


### Speed

The printer has been tested with a **Print Speed** of 200mm/s, with
first layer speed running around 50mm/s.

This is almost certainly too fast for small models (where each layer
may print in less than 10s), and for features like internal threads.

For such models, choose a more conservative speed of around
120mm/s. Internal threads may require a more significant slowdown.

Higher speeds _are_ possible, but are limited by the 0.4 nozzle and
the maximum flow rate of the Rapido HF hotend.

## References

[Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide)
is a nice collection of tuning information.

The course printer has:

  - had its extruder calibrated,
  - first layer z-offset set,
  - pressure advance tuned

Please do not change these printer settings (or if you do, please do
not make them permanent.)


