COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
          "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
          "aquamarine4": "#458b7", "azure1": "#f0ffff"}

valid = False

colour_name = input("enter a colour name: ")
while not valid:
    if colour_name in COLOURS:
        print("Your colour code is", COLOURS[colour_name])
        valid = True
    else:
        print("That name is not in our dictionary")
        colour_name = input("enter a colour name: ")
