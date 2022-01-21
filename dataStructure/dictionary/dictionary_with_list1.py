student_sibling = {
    "Howard":["Anthony","Barbie","Annie"],
    "Barbie":["Anthony","Howard","Annie"],
    "Anthony":["Barbie","Barbie","Annie"]
}

for sibilng in student_sibling:
    print(sibilng,"has the sibilng",student_sibling.get(sibilng))