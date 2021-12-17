student_score = {
    "Adrian":[90,91,88],
    "Charlie":[80,85,78],
    "Mandy":[50,28,70],
    "Henry":[98,91,92],
    "Leon":[58,98,65],
    "Mike":[87,58,60]
}
Mike_score = student_score.get("Mike")
print(Mike_score)


for student in student_score:
    print(student,"has a score of",student_score.get(student))




