sorted_student_score = [89,90,96,97,98,99,100]

#count how many number() in this list
how_much_90 = sorted_student_score.count(90)
print(how_much_90)


#insert number 68 at the position of 2
sorted_student_score.insert(2,68)
print(sorted_student_score)

#delete a number
sorted_student_score.remove(90)
print(sorted_student_score)

#add a number
sorted_student_score.append(58)
print(sorted_student_score)

#reserve the list
sorted_student_score.reverse()
print(sorted_student_score)

#sort the list from small to big

sorted_student_score.sort()
print(sorted_student_score)

#find the position of 100
where_is_position_100 = sorted_student_score.index(100)
print(where_is_position_100)

#find the number in what position
which_number_in_position_0 = sorted_student_score[0]
print(which_number_in_position_0)

pop = sorted_student_score.pop(0)
print(pop)