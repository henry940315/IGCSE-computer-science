#String list
letter_grades = ["A","A-","A","B","B","C","C-","A-","B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")
number_of_A_grade = letter_grades.count("A")
print("number of grades A: ",number_of_A_grade)
#interger list
numbers = [0,0,1,1,2,3,4,0,0,1,1,0,0,1,0,0]
zero_frequency = numbers.count(0)
print("number of zero", zero_frequency)
#boolean list
has_complete_work = [True, True, False, True, False, False, True]
numbers_of_complete_hw = has_complete_work.count(True)
print("number of people who did hw",numbers_of_complete_hw)