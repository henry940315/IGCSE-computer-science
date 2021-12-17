has_done_HW = [True,False,True,False,True,False]
print(has_done_HW)
#sort
has_done_HW.sort()
print(has_done_HW)
#count False
number_Flase = has_done_HW.count(False)
print(number_Flase)

for student in has_done_HW:
    print(student)
