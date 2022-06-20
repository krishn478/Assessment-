tablet = ["fever","cold","cough","headache,joint pain"]
TabPos = { "fever": "Shelf 1",
           "cold" : "Shelf 2",
           "cough": "Shelf 3",
           "headache":"Shelf 4",
           "joint pain":"Shelf 5"}
symp=input("Enter symptom (Enter in lower case)\t")
if symp in tablet:
    print("The tablets you are searching for are in",TabPos[symp])
else:
    print("Sorry, we do not have the tablets you are searching for")
