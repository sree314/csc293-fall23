# Class Notes: October 25th, 2023

We discussed how to model the choices so that users can easily enter in the choice hierarchy and printers can easily select options.

## Choice Effect
Each part will have certain effect attributes that are used if it is selected
 - **Choice Selection Effect**: Tells us if the part has been selected as a part of the current choice
 - **Choice Count Effect**: Tell us the quantity of the part to be printed if selected
 - **Choice Scale Effect**: Tell us the parts scale if selected (100% default)

## Rough Pseudocode:
`parts = {list of parts}
selParts = {set of parts}
for p in parts:
	if p.selected(choice):
		selPart.add(p)`

## Choice Hierarchy and Structure:
 - Choices will be formed into a decsion tree where each node is a choice and each leaf is a set of parts to be printed based on those choices
 - There will be differnet types of choices at each node as well. They are ChoiceSingle, ChoiceBoolean, and ChoiceMultiple.
 - Users will input the type of choice and the result of it, this will be formed into the decison tree