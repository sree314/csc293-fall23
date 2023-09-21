# Background

Following the census results and discussion, we begin outlining
projects.

# Users

The community can be factored into:

  - Designers: produce CAD models and projects
  - Modders: produce modifications to projects
  - Documentation producers: Produce documentation
  - Printers: Print out 3D parts
  - Builders/Assemblers: Assemble 3D parts
  - End users: Uses the resulting 3D printed project

The list above is roughly in increasing order of estimated size.

# Technological Improvements

What we can hope to improve:

  - Expense
    - Time
    - Cost
    - Equipment
  - Quality
    - Reduce mistakes
  - Reducing repetitions
  - Reducing variation, inconsistencies by using standards
  - Broaden adoption
  - Add automation
  - Reduce labour

# Ideas/Motivation

  - Improve Documentation content
  - Documentation organization
  - Documentation per part generator
  - Step-by-step instructions for printing
  - Clear information, not 70 pages
  - "One click" printing
  - Support materials?

# Exploring a Solution

A checklist for:
  - error catching
  - best practices
  - design rules

Possibly implemented through a compiler-like tool.

But could also end up generating STL files, providing print settings per part, etc.

## How this would benefit the audience

### End users

Fewer mistakes, broader adoption, can communicate with others in standardized way (especially about configurations)

## Printers

Automatic selection of parts to print

## Builders

Better docs, shorter docs (since files contain a lot of information)

## Documentation Producers

Saves time, reduces work

## Designers

Produces output files (e.g. STLs) automatically and consistently

## Modders

Easier to modify with better documentation

## How we will implement this

We will create a database of settings (usually filled in by designers).

Then a tool, or a suite of tools will process that database to perform:

   - STL generation (requires: mesh density, scale, orientation, etc.)
   - produce STEP files
   - Generate documentation
   - Configurator
   - List of parts [cutoff]
   - Exploded views?



