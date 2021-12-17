
has_pets = {'Mars':False, "Henry":False,"Barbie":True,"Adrian":True,"Agellina":False}


# Data structure operation - add , delete , search , sort
student_has_pet = has_pets.get("Mars")
print("The student has a pet", student_has_pet)

for student in has_pets:
    print(student, "has a pet:", has_pets.get(student))


student_remove = has_pets.pop("Adrian")

print(has_pets)