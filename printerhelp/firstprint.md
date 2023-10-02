# Your first 3D print

This is a quick start to using the Voron Trident printer.

## Install and configure the slicer

Make sure you have a slicer setup.

I recommend using the [Cura Slicer](https://ultimaker.com/software/ultimaker-cura/) if you don't have a
preference. Configure the [Printer's settings](cura-settings.md) in Cura.

You can take a look at the [Generic Settings](generic-settings.md) as well.

## Download an STL file

Select a small file that takes under an hour to print. I recommend
either the [3DBenchy](https://www.3dbenchy.com/download/) or the [Voron
Cube](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/STLs/Test_Prints/Voron_Design_Cube_v7.stl).

Slice the STL file in Cura to obtain G-code.

DO THE FOLLOWING STEPS IN FRONT OF THE PRINTER.

## Load Filament

If the printer does not contain the filament you want, do the following:

  0. Connect to the [printer](http://trident.thirdlaw.net).
  1. Heat the hotend to a temperature of 230C.
  2. Click the **Unload Filament** button to eject the filament.
  3. Pull the filament out through the PTFE tube once it's been ejected.
  4. Load the new filament into the PTFE tube.
  5. Once the new filament makes contact with the gears in the printhead, hit **Load Filament**
  6. Repeat **Load Filament** until the old filament is purged and the new filament is extruded.
  7. Hit the **Cooldown** button to cool the hotend.
  8. Once the hotend has reached a temperature < 100C, open the doors and use a tweezer to remove the extruded filament.
  9. Close the doors.

## Upload G-code and Print

Upload the G-code you prepared to the printer using the **Upload and
Print**. Make sure the doors are closed.

The printer will now begin printing. You should observe the following:

  1. The print head will home.
  2. The bed will start heating to a temperature of 105C -- this takes around 10 min.
  3. The printer will "heat soak" and try to reach a chamber temperature of around 40C. This takes around 10 minutes.
  4. The Z-tilt procedure will run to level the bed.
  5. The hotend will heat to 150C.
  6. The print head will probe the bed to create a bed mesh.
  7. The print head will move to the front of the printer and close to the bed to prevent oozing.
  7. The hotend will then heat to the target temperature (230C) for ABS.
  8. Once heated, a purge line will be printed first.
  9. Then, your object will start printing.

You can hit **Pause** to pause the print. You can then hit **Cancel** to cancel the print once it's paused.  These actions can take a while, especially if the printer is waiting for the bed or hotend to heat up.

If something goes wrong, hit **Emergency Stop**.

## Removing your printed object.

Once the printer has completed the print, the print head will move to the back of the printer.

DO NOT OPEN THE DOOR UNTIL the bed temperature is less than 60C. This takes around 10--15 minutes.

For additional safety, wait until the hotend has reached a temperature of less than 50C, and the hotend fan has stopped running.

The printed object should auto-release from print bed (you can hear
the object separating). However, if the object is still stuck to the
print bed:

   1. Remove the flex plate on top of the print bed AFTER making sure it is not hot.
   2. Flex the plate to release the object.
   3. Put the flex plate back.


