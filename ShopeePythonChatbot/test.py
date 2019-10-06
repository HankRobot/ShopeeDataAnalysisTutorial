food_selection = input("Enter what are you going to eat for lunch: ") 

if food_selection.lower() == "amk":
    print("nice place")
elif food_selection.lower() == "orchard":
    print("lots of nice food")
elif food_selection.lower() == "punggol":
    print("bit far but I like it")
elif food_selection.lower() == "changi":
    print("can go Jewel everyday")
else:
    print("Sorry, not sure what to suggest for", food_selection)