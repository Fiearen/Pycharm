COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
           "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
           "aquamarine4": "#458b7", "azure1": "#f0ffff"}

colour_name = input("enter a colour name: ")
while colour_name not in COLOURS:
    print("That name is not in our dictionary")
    colour_name = input("enter a colour name: ")

print("Your colour code is", COLOURS[colour_name])
