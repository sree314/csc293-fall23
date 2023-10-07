# A Little Course in 3D Printing

This self-paced course walks you through many situations encountered
when printing on the course's Trident Printer.

The sequence of lessons below follow from your [first
print](firstprint.md).

I have not printed many of these objects, so you may encounter
issues. Let me know.

Please suggest other interesting models.

I do not provide instructions on how to configure Cura profile
settings. Use the Cura manual or the various tutorials on the web.

## Printing Simple Objects

These objects should print without needing any adjustment to your
default print profile settings. Download the STL (or 3MF) files and
slice them.

  1. "[Einsteins](https://www.printables.com/model/430171-einstein-hat-worlds-first-aperiodic-monotile)", aperiodic tiles.
  2. [AT-ST Walker Kit Card](https://www.printables.com/model/527518-at-st-walker-kit-card), a great throwback to the age of injection molded plastic.
  3. [Flexi-Rex](https://www.printables.com/model/46241-flexi-rex-with-stronger-links), this is "print-in-place" model.
  4. [Spiral Planter](https://www.printables.com/model/225251-modern-spiral-planter/files)

## Printing Parts with Profile Changes

These parts need to the slicer to generate extra g-code or in a special manner.

### Supports

These parts require supports which may be removed after printing.

  1. [Jack O'Lantern](https://www.printables.com/model/285482-adorable-cute-halloween-pumpkin-jack-olantern).

### Vase Mode

You need to configure Cura to print in "Vase mode". Note: Cura calls this "Spiralize Outer Contour".

  1. [Last meters soap dish](https://www.printables.com/model/211599-last-meters-soap-dish)

## Print Complex Machines

These models have multiple parts that need to be put together, and may
need profile settings.

  1. [Strong Flying Propellor](https://www.printables.com/model/227852-strong-flying-propeller-pull-copter-no-supports)
  2. [Digital Sundial](https://www.printables.com/model/227852-strong-flying-propeller-pull-copter-no-supports) This takes a long time to print!

## Mods

This is a list of parts that can use to exercise your part modification skills.

TODO.


## Printing Test Objects

The [Voron Test
Prints](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/Test_Prints)
contains some deceptively simple prints that are hard to print without
tuning your profiles. The Voron Design Cube usually prints without much tuning.

You should use the [Voron print settings](https://docs.vorondesign.com/sourcing.html#print-settings) for these parts.

  1. [Filament Card](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/STLs/Test_Prints/Filament_Card.stl), this requires good first layer adhesion, so it should print easily.
  2. [Filament Card Caddy](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/STLs/Test_Prints/Filament_Card_Caddy_25.stl), this experiences stringing. Tune your retraction settings.
  3. [Thread Test 1](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/STLs/Test_Prints/Thread_Test_1_x1_Rev1.STL), this features a part with an internal thread which will be unusable if you print too fast (the threads will pull away from the print). The other thread test models have a similar issue.

There are many other test objects used to tune your slicer settings
available online.
